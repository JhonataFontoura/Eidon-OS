from __future__ import annotations

import json
from typing import Any

from openai import OpenAI

from eidon_os.intelligence.config import AISettings
from eidon_os.intelligence.tools import EidonToolRegistry


SYSTEM_INSTRUCTIONS = """
You are Eidon, the intelligence layer of Eidon OS.
Use Eidon tools whenever the answer depends on data stored in Eidon.
The Eidon database is the source of truth. Do not invent projects, goals, activities or knowledge.
You may create records when the user asks you to store or register information.
Deletion is destructive. Only attempt delete_record when the user clearly asks for deletion; the Eidon UI must also authorize destructive actions for that message.
Keep answers concise, practical and in the user's language.
""".strip()


class OpenAIProvider:
    def __init__(self, settings: AISettings, tools: EidonToolRegistry) -> None:
        self.settings = settings
        self.tools = tools

    def chat(self, message: str, *, allow_destructive: bool = False) -> dict[str, Any]:
        if not self.settings.api_key:
            raise RuntimeError("OpenAI is not configured. Add an API key in Eidon IA or set OPENAI_API_KEY.")

        client = OpenAI(api_key=self.settings.api_key)
        conversation: list[Any] = [{"role": "user", "content": message}]
        actions: list[dict[str, Any]] = []

        for _ in range(8):
            response = client.responses.create(
                model=self.settings.model,
                instructions=SYSTEM_INSTRUCTIONS,
                input=conversation,
                tools=self.tools.schemas(),
                store=False,
            )
            conversation.extend(response.output)
            calls = [item for item in response.output if getattr(item, "type", None) == "function_call"]
            if not calls:
                return {"message": response.output_text, "actions": actions, "model": self.settings.model}

            for call in calls:
                try:
                    arguments = json.loads(call.arguments or "{}")
                    result = self.tools.execute(call.name, arguments, allow_destructive=allow_destructive)
                    actions.append({"tool": call.name, "arguments": arguments, "result": result})
                    output = json.dumps(result, ensure_ascii=False, default=str)
                except Exception as exc:
                    output = json.dumps({"error": str(exc)}, ensure_ascii=False)
                    actions.append({"tool": call.name, "error": str(exc)})
                conversation.append({"type": "function_call_output", "call_id": call.call_id, "output": output})

        raise RuntimeError("Eidon AI exceeded the maximum tool-call cycle for one message")
