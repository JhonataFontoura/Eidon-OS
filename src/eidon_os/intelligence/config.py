from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(slots=True)
class AISettings:
    """Runtime configuration for the selected AI provider.

    API keys are intentionally kept out of the database and are never returned
    by the web API. A key entered through the local UI lives only in memory for
    the current Eidon Web process. OPENAI_API_KEY remains the recommended
    persistent configuration mechanism.
    """

    provider: str = "openai"
    model: str = "gpt-5"
    api_key: str | None = None

    @classmethod
    def from_environment(cls) -> "AISettings":
        return cls(
            provider=os.getenv("EIDON_AI_PROVIDER", "openai"),
            model=os.getenv("EIDON_AI_MODEL", "gpt-5"),
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    @property
    def configured(self) -> bool:
        if self.provider == "openai":
            return bool(self.api_key)
        return False

    def update(self, *, provider: str, model: str, api_key: str | None = None) -> None:
        provider = provider.strip().lower()
        model = model.strip()
        if provider != "openai":
            raise ValueError("Only the OpenAI provider is available in this foundation")
        if not model:
            raise ValueError("model cannot be empty")
        self.provider = provider
        self.model = model
        if api_key is not None and api_key.strip():
            self.api_key = api_key.strip()
