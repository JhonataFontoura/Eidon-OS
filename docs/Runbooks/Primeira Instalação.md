# Runbook — Primeira Instalação

## Objetivo

Preparar uma máquina nova para executar o Eidon OS.

## Pré-requisitos

Git, Python 3.11+ e VS Code instalados.

## Procedimento

```powershell
git clone https://github.com/JhonataFontoura/Eidon-OS.git
cd Eidon-OS
git fetch origin
git checkout feat/personal-intelligence-v0.4.0
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
python -m unittest discover -s tests
eidon --help
```

## Resultado esperado

A virtualenv aparece no terminal, os testes passam e a CLI exibe os comandos disponíveis.

## Checklist

```text
[ ] Python reconhecido
[ ] Branch correta
[ ] .venv criada
[ ] Projeto instalado
[ ] Testes aprovados
[ ] CLI funcionando
```
