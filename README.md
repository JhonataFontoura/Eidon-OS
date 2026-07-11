# 🏛️ Eidon OS

**Eidon OS** é um sistema operacional pessoal baseado em inteligência artificial que combina características de **copiloto** e **agente** para organizar conhecimento, preservar contexto e apoiar decisões.

O projeto ocupa uma posição intermediária entre os dois modelos: mantém o usuário no controle, como um copiloto, mas evolui para executar fluxos especializados e coordenar diferentes papéis, como uma plataforma de agentes.

> **Missão:** construir e preservar.

## ✨ Visão

Transformar a interação com IA em uma experiência contínua, estruturada e orientada ao crescimento pessoal e profissional.

O Eidon OS organiza projetos, estudos, carreira, arquivos e decisões por meio de três elementos centrais:

- **Palácio da Memória:** estrutura lógica onde o conhecimento é organizado.
- **Bibliotecário Eidon:** responsável por inspecionar, catalogar e preservar informações.
- **Conselho do Palácio:** conjunto de especialistas virtuais para tecnologia, estudos, carreira, planejamento, qualidade e documentação.

## 🤖 Copiloto, agente ou os dois?

O Eidon OS é uma **plataforma de orquestração de IA pessoal**:

- atua como **copiloto** quando trabalha ao lado do usuário;
- adota comportamentos de **agente** ao executar fluxos definidos por regras;
- prepara a base para uma futura arquitetura **multiagente**.

```text
Usuário
   ↓
Eidon OS
   ↓
Conselho do Palácio
   ├── Eidon — organização e memória
   ├── Asterion — arquitetura
   ├── Aion — desenvolvimento
   ├── Argus — qualidade
   ├── Nareth — estratégia
   ├── Soren — documentação
   ├── Solon — estudos
   ├── Magnus — carreira
   └── Elarion — narrativa
```

## 🗄️ Banco de dados local

A versão `0.2.0` introduz persistência local com **SQLite**, usando apenas a biblioteca padrão do Python.

A primeira entidade persistida é uma **memória catalogada**, composta por:

- título;
- conteúdo;
- categoria;
- origem;
- data de criação;
- data de atualização.

O banco é criado automaticamente em `data/eidon.db` e não é versionado no Git.

## 🧱 Arquitetura

A implementação segue princípios de **Código Limpo**, **Arquitetura Limpa** e **O Codificador Limpo**.

```text
src/eidon_os/
├── domain/
│   └── memory.py
├── application/
│   ├── ports.py
│   └── use_cases.py
├── infrastructure/
│   └── sqlite_repository.py
└── cli.py
```

- **Domínio:** regras e entidades independentes de tecnologia.
- **Aplicação:** casos de uso e contratos de persistência.
- **Infraestrutura:** implementação do repositório SQLite.
- **Interface:** comandos de terminal para cadastrar e consultar memórias.

## 🚀 Como executar

Requisitos: Python 3.11 ou superior.

```bash
git clone https://github.com/JhonataFontoura/Eidon-OS.git
cd Eidon-OS
python -m venv .venv
```

Ative o ambiente virtual e instale o projeto:

```bash
pip install -e .
```

Cadastrar uma memória:

```bash
eidon add \
  --title "Decisão arquitetural" \
  --content "Usar SQLite na primeira versão." \
  --category "projetos" \
  --source "Eidon OS"
```

Listar memórias:

```bash
eidon list
```

Executar os testes:

```bash
python -m unittest discover -s tests
```

## 🏛️ Estrutura geral

```text
Eidon-OS/
├── README.md
├── SYSTEM.md
├── pyproject.toml
├── src/
├── tests/
├── docs/
├── config/
├── agents/
├── palace/
├── templates/
├── roadmap/
├── memory/
└── scripts/
```

## 🎬 Frase de ativação

> **Está na hora do show.**

Essa frase ativa o modo de desenvolvimento técnico orientado por boas práticas de engenharia de software.

## 🛣️ Roadmap

- [x] Definir o Palácio da Memória.
- [x] Criar os Guardiões e o Conselho do Palácio.
- [x] Documentar regras, comandos e memória estratégica.
- [x] Implementar banco de dados local com SQLite.
- [ ] Criar operações de atualização e remoção de memórias.
- [ ] Adicionar busca por categoria e palavras-chave.
- [ ] Criar API local.
- [ ] Desenvolver interface web para o Palácio.
- [ ] Integrar GitHub, Google Drive, Gmail e Google Calendar.
- [ ] Evoluir para uma plataforma multiagente.

## 📜 Licença

Este projeto é distribuído sob a licença MIT.
