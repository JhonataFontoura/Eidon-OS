from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from eidon_os.application.personal_intelligence import PersonalAnalytics
from eidon_os.infrastructure.sqlite_activity_repository import SQLiteActivityRepository
from eidon_os.infrastructure.sqlite_goal_repository import SQLiteGoalRepository
from eidon_os.infrastructure.sqlite_knowledge_repository import SQLiteKnowledgeRepository
from eidon_os.intelligence.config import AISettings
from eidon_os.intelligence.gateway import EidonAIGateway
from eidon_os.intelligence.tools import EidonToolRegistry
from eidon_os.web.ui import DASHBOARD_HTML


class AIConfigRequest(BaseModel):
    provider: str = "openai"
    model: str = "gpt-5"
    api_key: str | None = None


class AIChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=10000)
    allow_destructive: bool = False


def create_app(database_path: str | Path = "data/eidon.db") -> FastAPI:
    database_path = Path(database_path)
    knowledge = SQLiteKnowledgeRepository(database_path)
    activities = SQLiteActivityRepository(database_path)
    goals = SQLiteGoalRepository(database_path)
    analytics = PersonalAnalytics(knowledge, activities)
    ai_settings = AISettings.from_environment()
    ai_tools = EidonToolRegistry(knowledge, activities, goals)
    ai_gateway = EidonAIGateway(ai_settings, ai_tools)

    app = FastAPI(
        title="Eidon OS Web",
        version="0.5.0",
        description="Interface web do Eidon OS sobre o Personal Intelligence Core.",
    )

    @app.get("/", response_class=HTMLResponse, include_in_schema=False)
    def dashboard() -> str:
        return DASHBOARD_HTML

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "service": "eidon-web", "version": "0.5.0"}

    @app.get("/api/dashboard")
    def dashboard_data() -> dict[str, object]:
        snapshot = analytics.snapshot()
        payload = asdict(snapshot)
        payload["total_hours"] = round(snapshot.total_minutes / 60, 1)
        return payload

    @app.get("/api/activities")
    def activity_data(limit: int = Query(default=20, ge=1, le=100)) -> list[dict[str, object]]:
        items = activities.list_all()[:limit]
        return [
            {
                "id": str(item.id), "title": item.title, "category": item.category,
                "description": item.description, "duration_minutes": item.duration_minutes,
                "source_type": item.source_type,
                "source_id": str(item.source_id) if item.source_id else None,
                "occurred_at": item.occurred_at.isoformat(),
            }
            for item in items
        ]

    @app.get("/api/goals")
    def goal_data() -> list[dict[str, object]]:
        return [
            {
                "id": str(item.id), "area": item.area, "indicator": item.indicator,
                "target": item.target, "unit": item.unit, "period": item.period,
                "active": item.active,
            }
            for item in goals.list_active()
        ]

    @app.get("/api/ai/status")
    def ai_status() -> dict[str, object]:
        return {
            "provider": ai_settings.provider,
            "model": ai_settings.model,
            "configured": ai_settings.configured,
            "key_source": "runtime/environment" if ai_settings.configured else None,
            "write_access": True,
            "destructive_requires_ui_authorization": True,
        }

    @app.post("/api/ai/config")
    def configure_ai(request: AIConfigRequest) -> dict[str, object]:
        try:
            ai_settings.update(
                provider=request.provider,
                model=request.model,
                api_key=request.api_key,
            )
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return {
            "provider": ai_settings.provider,
            "model": ai_settings.model,
            "configured": ai_settings.configured,
            "message": "Configuração aplicada apenas ao processo atual. Use OPENAI_API_KEY para persistir a chave com segurança.",
        }

    @app.post("/api/ai/chat")
    def ai_chat(request: AIChatRequest) -> dict[str, object]:
        try:
            return ai_gateway.chat(
                request.message,
                allow_destructive=request.allow_destructive,
            )
        except (RuntimeError, ValueError) as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        except Exception as exc:
            raise HTTPException(status_code=502, detail=f"AI provider error: {exc}") from exc

    return app


app = create_app()


def main() -> None:
    uvicorn.run("eidon_os.web.app:app", host="127.0.0.1", port=8000, reload=False)


if __name__ == "__main__":
    main()
