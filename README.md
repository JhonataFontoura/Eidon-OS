# 🏛️ Eidon OS

**Eidon OS** é uma plataforma pessoal de conhecimento e evolução. O núcleo pertence ao próprio Eidon: memória, projetos, atividades, metas, analytics e dados permanecem independentes de qualquer provedor de inteligência artificial.

> **Missão:** construir, preservar e transformar contexto em decisões.

## Estado atual — v0.5.0 Eidon Web

A v0.5.0 inicia a transição do Eidon de uma aplicação centrada em CLI para uma plataforma com interface web própria, sem acoplar o domínio a um framework ou a um provedor de IA.

### Entregas desta fase

- [x] preservação do Personal Intelligence Core da v0.4.0;
- [x] versão do pacote atualizada para `0.5.0`;
- [x] aplicação web com FastAPI;
- [x] comando `eidon-web` para iniciar a interface;
- [x] dashboard visual responsivo;
- [x] visão consolidada de projetos, conhecimentos, atividades e horas registradas;
- [x] listagem de atividades recentes;
- [x] listagem de metas ativas;
- [x] API local para dashboard, atividades e metas;
- [x] endpoint de health check;
- [x] testes da fundação web.

## Arquitetura

```text
Eidon OS
├── Domain
├── Application
├── Infrastructure
│   ├── SQLite
│   └── Excel
├── CLI
└── Web                ← v0.5.0
    ├── FastAPI
    ├── Dashboard
    └── API local
```

A camada `web` consome os casos de uso e repositórios existentes. O domínio continua independente da interface web.

## Executar a v0.5.0

Requisito: Python 3.11+.

```powershell
git clone https://github.com/JhonataFontoura/Eidon-OS.git
cd Eidon-OS
git switch v0.5.0
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m unittest discover -s tests -v
eidon-web
```

Depois acesse no navegador:

```text
http://127.0.0.1:8000
```

Documentação automática da API:

```text
http://127.0.0.1:8000/docs
```

## Endpoints iniciais

```text
GET /                Dashboard web
GET /health          Estado do serviço
GET /api/dashboard   Métricas consolidadas
GET /api/activities  Atividades recentes
GET /api/goals       Metas ativas
```

## CLI e exportações

A interface web não substitui o núcleo nem remove os recursos existentes. A CLI e as exportações continuam disponíveis:

```powershell
eidon dashboard
eidon activity-list
eidon goal-list
eidon report weekly
eidon report monthly
eidon dashboard-export
```

O Excel permanece como camada de exportação e análise. O Eidon Web passa a ser a principal direção de interface do projeto.

## Roadmap

1. **v0.4.0 — Personal Intelligence Core** — Activities, metas, analytics, relatórios e exportações.
2. **v0.5.0 — Eidon Web** — interface web própria e visualização central do sistema.
3. **v0.6.0 — AI Gateway** — provedores de IA intercambiáveis e permissões de acesso.
4. **v0.7.0 — Semantic Memory / RAG** — embeddings, busca semântica e recuperação de contexto.
5. **v0.8.0 — Agents & Automation** — especialistas e automações controladas.
6. **v1.0.0 — Eidon OS** — plataforma pessoal estável e integrada.

## Princípio arquitetural

> **A IA acessa o Eidon; o Eidon não pertence à IA.**

OpenAI, Anthropic, Google ou modelos locais poderão ser conectados posteriormente por um AI Gateway, sem mover a memória ou o domínio para o provedor.

## Frase de ativação

> **Está na hora do show.**

## Licença

MIT.
