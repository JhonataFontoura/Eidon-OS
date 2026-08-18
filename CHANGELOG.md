# Changelog

## [0.5.0] — Eidon Web

### Adicionado
- aplicação web com FastAPI;
- comando `eidon-web`;
- dashboard web responsivo;
- API local para métricas, atividades e metas;
- endpoint `/health`;
- testes da fundação web.

### Alterado
- versão do pacote atualizada para `0.5.0`;
- interface web passa a ser a direção principal de visualização do projeto;
- CLI e Excel permanecem como interfaces complementares;
- README atualizado com execução e arquitetura da v0.5.0.

### Mantido
- Personal Intelligence Core da v0.4.0;
- persistência SQLite local;
- Activities, Goals, analytics, relatórios e exportações;
- independência entre o domínio e provedores de IA.

## [0.4.0] — Personal Intelligence Core

### Adicionado
- entidade Activity e persistência SQLite;
- registro automático de atividades em operações de cadastro;
- analytics e timeline semanal/mensal;
- filtros por período e categoria no dashboard de terminal;
- relatórios semanais e mensais em Markdown;
- entidade Goal com persistência SQLite;
- comandos `goal-add` e `goal-list`;
- dashboard Excel dividido por áreas, Base Geral e Metas;
- documentação de desenvolvimento e runbooks;
- testes de Activities e Metas.

### Alterado
- Excel reposicionado como camada de exportação, não interface principal;
- visão do produto revisada para independência de provedores de IA;
- roadmap reorganizado para iniciar a v0.5.0 com Eidon Web.

## [0.3.0] — Knowledge Core
- projetos, arquivos, pessoas, empresas, conhecimento e relacionamentos;
- arquitetura em camadas e persistência SQLite.

## [0.2.0]
- memória local, CLI e primeiros testes de persistência.
