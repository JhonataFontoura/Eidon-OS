# Runbook — Recuperação de Ambiente

## Quando utilizar

Quando a virtualenv estiver corrompida, dependências não forem reconhecidas ou a instalação local deixar de funcionar.

## Procedimento

Preserve primeiro o banco:

```powershell
New-Item -ItemType Directory -Force backups | Out-Null
Copy-Item data\eidon.db backups\eidon-before-environment-recovery.db
```

Recrie apenas o ambiente Python:

```powershell
Deactivate 2>$null
Remove-Item -Recurse -Force .venv
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
python -m unittest discover -s tests
```

## Validação

```powershell
eidon --help
eidon dashboard
```

## Escalonamento

Se o erro continuar, registre a mensagem completa, versão do Python, saída de `python -m pip check` e `git status` antes de alterar outros arquivos.
