# 08 — Troubleshooting

## Python não reconhecido

```powershell
python --version
py --version
```

Se ambos falharem, instale o Python e marque **Add Python to PATH**. Abra um novo terminal.

## `.venv` não existe

```powershell
python -m venv .venv
```

## PowerShell bloqueia `Activate.ps1`

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Comando `eidon` não reconhecido

Com a virtualenv ativa:

```powershell
python -m pip install -e .
```

Alternativa:

```powershell
python -m eidon_os.cli --help
```

## `openpyxl` ausente

```powershell
python -m pip install -e .
python -m pip show openpyxl
```

## Dashboard vazio

Registre atividades antes de exportar:

```powershell
eidon activity-add --title "Estudo de Python" --category "Estudos" --duration-minutes 60
eidon dashboard-export
```

## Problemas com SQLite

- feche programas que estejam usando o banco;
- confirme a existência de `data/`;
- faça backup antes de remover ou substituir o arquivo;
- nunca use o banco real em testes automatizados.

## Branch desatualizada

```powershell
git fetch origin
git status
git pull --ff-only
```
