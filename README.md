# 🏛️ Eidon OS

**Eidon OS** é uma Plataforma de Gestão do Conhecimento Pessoal baseada em inteligência artificial. O projeto combina características de copiloto, agente e sistema operacional pessoal para preservar contexto, organizar conhecimento, acompanhar evolução e apoiar decisões.

> **Missão:** construir e preservar.

## Arquitetura em quatro núcleos

```text
Eidon OS
├── Núcleo do Conhecimento
├── Núcleo de Inteligência
├── Núcleo do Sistema
└── Núcleo dos Especialistas
```

## Estado atual

### Versão 0.4.0 — Personal Intelligence

A versão 0.4.0 transforma o Eidon de um sistema que apenas armazena conhecimento em uma plataforma que também registra, mede e apresenta a evolução do usuário.

- [x] SQLite local em `data/eidon.db`;
- [x] memórias, arquivos, projetos, pessoas, empresas e conhecimento;
- [x] relacionamentos genéricos entre entidades;
- [x] nova entidade `Activity`;
- [x] registro de duração, categoria, origem e data das atividades;
- [x] timeline semanal;
- [x] analytics pessoais;
- [x] relatórios no terminal;
- [x] dashboard exportável para Excel;
- [x] testes de persistência de atividades;
- [x] CLI atualizada.

## Estrutura de software

```text
src/eidon_os/
├── domain/
│   ├── memory.py
│   ├── knowledge.py
│   └── activity.py
├── application/
│   ├── ports.py
│   ├── use_cases.py
│   ├── knowledge_ports.py
│   ├── knowledge_use_cases.py
│   ├── activity_ports.py
│   ├── activity_use_cases.py
│   └── personal_intelligence.py
├── infrastructure/
│   ├── sqlite_repository.py
│   ├── sqlite_knowledge_repository.py
│   ├── sqlite_activity_repository.py
│   └── excel_dashboard.py
└── cli.py
```

O domínio não depende do SQLite, do Excel nem da interface de terminal. A aplicação define contratos, casos de uso e análises; a infraestrutura fornece persistência e exportação; a CLI é uma porta de entrada.

## Como executar

Requisito: Python 3.11 ou superior.

```bash
git clone https://github.com/JhonataFontoura/Eidon-OS.git
cd Eidon-OS
git checkout feat/personal-intelligence-v0.4.0
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -e .
```

## Comandos principais

### Registrar uma atividade

```bash
eidon activity-add --title "Estudo de SQL" --category "Estudos" --duration-minutes 60
```

Também é possível relacionar a atividade a um projeto ou outra entidade:

```bash
eidon activity-add --title "Sprint do Eidon" --category "Projetos" --duration-minutes 90 --source-type project --source-id "UUID_DO_PROJETO"
```

### Consultar atividades

```bash
eidon activity-list
```

### Dashboard no terminal

```bash
eidon dashboard
```

### Exportar dashboard para Excel

```bash
eidon dashboard-export
```

O arquivo será criado por padrão em:

```text
reports/eidon_dashboard.xlsx
```

Para escolher outro caminho:

```bash
eidon dashboard-export --output "meus-relatorios/desenvolvimento.xlsx"
```

## O que o dashboard apresenta

- quantidade de projetos;
- arquivos catalogados;
- pessoas e empresas;
- itens de conhecimento;
- relacionamentos;
- atividades registradas;
- tempo total investido;
- atividades por categoria;
- timeline detalhada.

## Testes

```bash
py -m unittest discover -s tests
```

## As Eras

1. **Fundação** — arquitetura, SQLite, CLI e memória.
2. **Conhecimento** — arquivos, projetos, pessoas, empresas e relações.
3. **Personal Intelligence** — atividades, analytics, timeline, relatórios e dashboard.
4. **Inteligência Semântica** — busca semântica, embeddings e RAG.
5. **Autonomia** — especialistas, automações e agentes.
6. **Ecossistema** — GitHub, Drive, Calendar, Gmail e outras integrações.

## Próximos passos

- registrar atividades automaticamente a partir de casos de uso;
- criar relatórios semanais e mensais em Markdown;
- ampliar o dashboard com metas e indicadores de carreira;
- adicionar filtros por período e categoria;
- preparar o Núcleo de Inteligência Semântica;
- implementar embeddings, busca semântica e RAG.

## Princípios

Código Limpo, Arquitetura Limpa, O Codificador Limpo, SOLID, KISS, DRY, YAGNI, documentação como código e evolução incremental.

## Frase de ativação

> **Está na hora do show.**

## Licença

MIT.
