from __future__ import annotations

from typing import Any

from eidon_os.intelligence.config import AISettings
from eidon_os.intelligence.openai_provider import OpenAIProvider
from eidon_os.intelligence.tools import EidonToolRegistry


class EidonAIGateway:
    """Provider-neutral entry point for Eidon intelligence."""

    def __init__(self, settings: AISettings, tools: EidonToolRegistry) -> None:
        self.settings = settings
        self.tools = tools

    def chat(self, message: str, *, allow_destructive: bool = False) -> dict[str, Any]:
        if self.settings.provider == "openai":
            return OpenAIProvider(self.settings, self.tools).chat(
                message, allow_destructive=allow_destructive
            )
        raise ValueError(f"Unsupported AI provider: {self.settings.provider}")
