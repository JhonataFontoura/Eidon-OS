# 03 — Banco de Dados SQLite

## Objetivo

Documentar a persistência local do Eidon OS e os cuidados necessários para preservar os dados do usuário.

## Local padrão

```text
data/eidon.db
```

O arquivo é criado automaticamente pelos repositórios SQLite quando necessário.

## Principais tabelas

- `memories`: memórias textuais.
- `projects`: projetos.
- `files`: metadados de arquivos.
- `people`: pessoas.
- `companies`: empresas.
- `knowledge_items`: itens de conhecimento.
- `relationships`: relações entre entidades.
- `activities`: histórico de atividades e evolução pessoal.

## Arquitetura

O domínio não conhece SQLite. Os contratos ficam na camada de aplicação e as implementações em `infrastructure/`.

```text
Domínio ← Aplicação ← Infraestrutura SQLite
```

## Convenções

- Identificadores em UUID armazenados como texto.
- Datas em ISO 8601.
- Chaves e índices criados de forma idempotente.
- Consultas parametrizadas para evitar injeção SQL.
- Migrações futuras devem preservar dados existentes.

## Inspeção manual

É possível abrir `data/eidon.db` com uma extensão SQLite no VS Code. Não altere dados manualmente sem backup.

## Backup

Com o Eidon fechado:

```powershell
Copy-Item data\eidon.db backups\eidon-$(Get-Date -Format yyyyMMdd-HHmmss).db
```

Consulte os runbooks de backup e restauração antes de qualquer operação destrutiva.
