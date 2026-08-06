# Runbook — Atualizar Ambiente

## Quando utilizar

Depois de baixar mudanças da branch, alterar dependências ou trocar de versão.

## Procedimento

```powershell
.\.venv\Scripts\Activate.ps1
git status
git fetch origin
git pull --ff-only
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip check
python -m unittest discover -s tests
```

## Cuidados

- Não use `git pull` com alterações locais não revisadas.
- Confira `git status` antes e depois.
- Não apague `.venv` sem necessidade.
- Faça backup do banco antes de mudanças estruturais.

## Resultado esperado

Código, dependências e testes ficam alinhados com a branch remota.
