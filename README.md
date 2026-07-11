# 🏛️ Eidon OS

**Eidon OS** é uma Plataforma de Gestão do Conhecimento Pessoal baseada em inteligência artificial. O projeto combina características de **copiloto**, **agente** e **sistema operacional pessoal** para preservar contexto, organizar conhecimento e apoiar decisões.

> **Missão:** construir e preservar.

## Por que existe

Projetos evoluem, pessoas esquecem, conversas desaparecem e arquivos se espalham. O Eidon OS nasce para conectar memórias, arquivos, projetos, pessoas, empresas, conhecimento e decisões em um único ecossistema pessoal.

Leia o [Manifesto](docs/manifesto.md).

## Identidade

O Eidon OS atua como:

- **copiloto**, quando trabalha lado a lado com o usuário;
- **agente**, quando executa fluxos definidos por regras e permissões;
- **plataforma de orquestração**, quando coordena especialistas do Conselho do Palácio;
- **PKMS**, quando transforma informações isoladas em conhecimento relacionado.

## Arquitetura em quatro núcleos

```text
Eidon OS
├── Núcleo do Conhecimento
├── Núcleo de Inteligência
├── Núcleo do Sistema
└── Núcleo dos Especialistas
```

### Núcleo do Conhecimento — em desenvolvimento

Persistência local com SQLite para:

- memórias;
- arquivos e seus metadados;
- projetos;
- pessoas;
- empresas;
- itens de conhecimento;
- relações entre registros.

### Núcleo de Inteligência — planejado

Busca semântica, embeddings, classificação, recomendações e RAG.

### Núcleo do Sistema

CLI, banco local, futura API, dashboard, configurações e integrações.

### Núcleo dos Especialistas

Eidon, Asterion, Aion, Argus, Nareth, Soren, Solon, Magnus e Elarion.

Mais detalhes em [Arquitetura](docs/arquitetura.md).

## Estado atual

### Versão 0.3.0 — Era II: Conhecimento

- [x] SQLite local em `data/eidon.db`;
- [x] memória textual catalogada;
- [x] entidades de arquivos, projetos, pessoas, empresas e conhecimento;
- [x] relacionamentos genéricos entre entidades;
- [x] CLI para cadastro e consulta;
- [x] testes de persistência;
- [x] documentação viva e ADRs.

## Estrutura de software

```text
src/eidon_os/
├── domain/
│   ├── memory.py
│   └── knowledge.py
├── application/
│   ├── ports.py
│   ├── use_cases.py
│   ├── knowledge_ports.py
│   └── knowledge_use_cases.py
├── infrastructure/
│   ├── sqlite_repository.py
│   └── sqlite_knowledge_repository.py
└── cli.py
```

O domínio não depende do SQLite nem da interface de terminal. A aplicação define contratos e casos de uso; a infraestrutura fornece persistência; a CLI é apenas uma porta de entrada.

## Como executar

Requisito: Python 3.11 ou superior.

```bash
git clone https://github.com/JhonataFontoura/Eidon-OS.git
cd Eidon-OS
git checkout feat/knowledge-core
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -e .
```

### Memórias

```bash
eidon add --title "Primeira memória" --content "O Palácio foi iniciado." --category "Projetos" --source "Eidon OS"
eidon list
```

### Projetos

```bash
eidon project-add --name "Eidon OS" --description "Plataforma pessoal de conhecimento" --github-url "https://github.com/JhonataFontoura/Eidon-OS"
eidon project-list
```

### Arquivos

```bash
eidon file-add --name "README.md" --path "README.md" --category "documentação"
eidon file-list
```

### Pessoas, empresas e conhecimento

```bash
eidon person-add --name "Jhony Nunes" --role "Criador"
eidon company-add --name "Stellantis" --website "https://www.stellantis.com"
eidon knowledge-add --title "PKMS" --content "Sistema de gestão do conhecimento pessoal" --kind "conceito" --tags "conhecimento,organização"
```

### Relacionamentos

Use os IDs mostrados pelos comandos de listagem:

```bash
eidon relation-add --source-type project --source-id "UUID_DO_PROJETO" --target-type file --target-id "UUID_DO_ARQUIVO" --relation-type contains
```

### Testes

```bash
py -m unittest discover -s tests
```

## Documentação

- [Manifesto](docs/manifesto.md)
- [Filosofia de engenharia](docs/filosofia.md)
- [Arquitetura](docs/arquitetura.md)
- [Eras](docs/eras.md)
- [Roadmap](docs/roadmap.md)
- [Conselho do Palácio](docs/CONSELHO.md)
- [ADR-0001 — Evolução para PKMS](docs/adr/0001-evolucao-para-pkms.md)

## As Eras

1. **Fundação** — arquitetura, SQLite, CLI e memória.
2. **Conhecimento** — arquivos, projetos, pessoas, empresas e relações.
3. **Inteligência** — busca semântica, embeddings e RAG.
4. **Autonomia** — especialistas, automações e agentes.
5. **Ecossistema** — GitHub, Drive, Calendar, Gmail e outras integrações.

Consulte o [Roadmap completo](docs/roadmap.md).

## Princípios

Código Limpo, Arquitetura Limpa, O Codificador Limpo, SOLID, KISS, DRY, YAGNI, documentação como código e evolução incremental.

## Frase de ativação

> **Está na hora do show.**

## Licença

MIT.
