# 02 — Dependências

## Objetivo

Explicar como as dependências são declaradas, instaladas e atualizadas sem comprometer a estabilidade do projeto.

## Fonte de verdade

As dependências do Eidon OS ficam em `pyproject.toml`. A instalação recomendada é editável:

```powershell
python -m pip install -e .
```

Isso permite alterar o código em `src/` e executar imediatamente a versão local.

## Dependências atuais

- Biblioteca padrão do Python para SQLite, CLI, datas e arquivos.
- `openpyxl` para exportação do dashboard em Excel.

## Regras para adicionar bibliotecas

Antes de incluir uma nova dependência, responda:

1. O problema pode ser resolvido com a biblioteca padrão?
2. A dependência é mantida e possui licença compatível?
3. O benefício supera o custo de instalação e manutenção?
4. Existe uma abstração na aplicação para evitar acoplamento direto?

## Atualização segura

```powershell
python -m pip install --upgrade pip
python -m pip install -e .
python -m unittest discover -s tests
```

Ao alterar `pyproject.toml`, atualize também o changelog e a documentação relacionada.

## Diagnóstico

```powershell
python -m pip list
python -m pip show openpyxl
python -m pip check
```

Nunca instale bibliotecas globalmente para trabalhar no projeto. Utilize sempre `.venv`.
