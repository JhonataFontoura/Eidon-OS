# 01 — Ambiente de Desenvolvimento

## Objetivo

Preparar uma máquina Windows para executar e desenvolver o Eidon OS com isolamento e reprodutibilidade.

## Pré-requisitos

- Git.
- Python 3.11 ou superior.
- Visual Studio Code.
- Acesso ao repositório.

## Instalação do Python

Durante a instalação, marque **Add Python to PATH**. Depois, abra um novo PowerShell e valide:

```powershell
python --version
python -m pip --version
```

Se `python` não for reconhecido, tente:

```powershell
py --version
```

## Clonar e selecionar a branch

```powershell
git clone https://github.com/JhonataFontoura/Eidon-OS.git
cd Eidon-OS
git fetch origin
git checkout feat/personal-intelligence-v0.4.0
```

## Ambiente virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear o script:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Instalação local

```powershell
python -m pip install --upgrade pip
python -m pip install -e .
```

## Extensões recomendadas do VS Code

- Python.
- Pylance.
- GitLens.
- SQLite Viewer.
- Markdown All in One.

## Verificação final

```powershell
eidon --help
python -m unittest discover -s tests
```

O ambiente está pronto quando a virtualenv aparece no terminal, o comando `eidon` é reconhecido e os testes terminam sem falhas.
