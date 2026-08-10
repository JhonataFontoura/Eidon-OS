# 🏛️ Eidon OS

**Eidon OS** é uma plataforma pessoal de conhecimento e evolução. O núcleo pertence ao próprio Eidon: memória, projetos, atividades, metas, analytics e dados permanecem independentes de qualquer provedor de inteligência artificial.

> **Missão:** construir, preservar e transformar contexto em decisões.

## Estado atual — v0.4.0 Personal Intelligence Core

A v0.4.0 fecha a fase em que o Eidon deixa de apenas armazenar informação e passa a registrar e medir evolução.

- [x] SQLite local em `data/eidon.db`;
- [x] memórias, arquivos, projetos, pessoas, empresas e conhecimento;
- [x] relacionamentos genéricos;
- [x] Activities com duração, categoria, origem e data;
- [x] registro automático de Activities em cadastros do núcleo;
- [x] analytics com filtros por período e categoria;
- [x] timeline semanal e mensal;
- [x] relatórios Markdown semanais e mensais;
- [x] metas persistentes no SQLite;
- [x] dashboard no terminal;
- [x] Excel por áreas + Base Geral + Metas;
- [x] documentação e runbooks;
- [x] testes de persistência de Activities e Metas.

## Comandos principais

```bash
eidon activity-add --title "Estudo de SQL" --category "Estudos" --duration-minutes 60
eidon goal-add --area "Academia de Código" --indicator "Desafios concluídos" --target 40 --unit desafios
eidon goal-list
eidon dashboard
eidon dashboard --category Estudos --start 2026-08-01T00:00:00+00:00
eidon dashboard-export
eidon report weekly
eidon report monthly
```

## Papel do Excel

O Excel é uma camada de exportação e análise, não a interface principal do produto. O arquivo contém Dashboard Geral, Metas, Estudos, Projetos, Academia de Código, Carreira, Base Geral, configurações e instruções.

## Roadmap revisado

1. **v0.4.0 — Personal Intelligence Core** — núcleo local, Activities, Metas, analytics, relatórios e exportações.
2. **v0.5.0 — Eidon Web** — aplicação web própria e visualização central do sistema.
3. **v0.6.0 — AI Gateway** — provedores de IA intercambiáveis e permissões de acesso.
4. **v0.7.0 — Semantic Memory / RAG** — embeddings, busca semântica e recuperação de contexto.
5. **v0.8.0 — Agents & Automation** — especialistas e automações controladas.
6. **v1.0.0 — Eidon OS** — plataforma pessoal estável e integrada.

## Princípio arquitetural para a próxima fase

> **A IA acessa o Eidon; o Eidon não pertence à IA.**

O Eidon Web será a interface principal. OpenAI, Anthropic, Google ou modelos locais poderão ser conectados posteriormente por um AI Gateway, sem mover a memória ou o domínio para o provedor.

## Como executar

Requisito: Python 3.11+.

```bash
git clone https://github.com/JhonataFontoura/Eidon-OS.git
cd Eidon-OS
git checkout feat/personal-intelligence-v0.4.0
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -e .
py -m unittest discover -s tests
```

## Frase de ativação

> **Está na hora do show.**

## Licença

MIT.
