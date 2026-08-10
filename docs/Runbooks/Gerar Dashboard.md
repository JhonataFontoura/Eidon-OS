# Runbook — Gerar Dashboard

## Objetivo

Gerar o relatório Excel da Personal Intelligence.

## Pré-requisitos

Ambiente ativo, projeto instalado e pelo menos uma atividade registrada.

## Procedimento

```powershell
.\.venv\Scripts\Activate.ps1
eidon activity-list
eidon dashboard
eidon dashboard-export
```

Saída padrão:

```text
reports/eidon_dashboard.xlsx
```

Saída personalizada:

```powershell
eidon dashboard-export --output reports\academia_de_codigo.xlsx
```

## Validação

Abra o arquivo e confirme as abas `Dashboard`, `Categories` e `Timeline`.

## Problemas comuns

- `eidon` não reconhecido: reinstale com `python -m pip install -e .`.
- `openpyxl` ausente: reinstale as dependências.
- arquivo vazio: registre atividades antes da exportação.
