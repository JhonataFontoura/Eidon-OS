# Changelog

## [0.5.0] — Eidon Web

### Adicionado
- aplicação web com FastAPI;
- comando `eidon-web`;
- dashboard web responsivo;
- API local para métricas, atividades e metas;
- endpoint `/health`;
- AI Gateway desacoplado do domínio;
- integração inicial com OpenAI / ChatGPT via OpenAI API;
- painel visual para configurar provedor, modelo e chave de API;
- chat visual integrado ao Eidon Web;
- ferramentas de IA para leitura de dashboard, atividades, metas, projetos e conhecimento;
- ferramentas de IA para criação de atividades, metas, projetos e conhecimento;
- exclusões controladas com autorização visual por mensagem;
- testes da camada de ferramentas da IA.

### Alterado
- a v0.5.0 passa a incluir a fundação de integração com IA antes do refinamento visual;
- o roadmap reserva a v0.5.1 para identidade visual, navegação e experiência web;
- dependência oficial `openai` adicionada ao projeto;
- README atualizado com arquitetura e configuração da IA.

### Segurança
- a IA não recebe conexão SQL bruta;
- a chave informada pela interface não é persistida no banco e nunca é devolvida pela API;
- exclusões permanecem bloqueadas até autorização explícita na interface.

### Mantido
- Personal Intelligence Core da v0.4.0;
- persistência SQLite local;
- Activities, Goals, analytics, relatórios e exportações;
- princípio: "A IA acessa o Eidon; o Eidon não pertence à IA."

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
