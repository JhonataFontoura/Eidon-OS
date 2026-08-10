# Runbook — Criar Nova Branch

## Objetivo

Isolar cada evolução do Eidon OS e preservar o histórico de versões.

## Procedimento

```powershell
git status
git fetch origin
git checkout feat/personal-intelligence-v0.4.0
git pull --ff-only
git checkout -b feat/nome-da-evolucao-v0.5.0
```

Depois confirme:

```powershell
git branch --show-current
```

## Primeiro envio

```powershell
git push -u origin feat/nome-da-evolucao-v0.5.0
```

## Regras

- Não misture funcionalidades sem relação.
- Use nomes descritivos.
- Faça commits pequenos e coerentes.
- Abra Pull Request para a branch-base correta.
