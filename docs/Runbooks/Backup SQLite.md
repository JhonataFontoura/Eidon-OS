# Runbook — Backup SQLite

## Objetivo

Criar uma cópia segura do banco local antes de atualizações, testes manuais ou migrações.

## Procedimento

1. Feche processos que estejam usando o Eidon.
2. Crie a pasta de backups.
3. Copie o banco com data e hora.

```powershell
New-Item -ItemType Directory -Force backups | Out-Null
$stamp = Get-Date -Format yyyyMMdd-HHmmss
Copy-Item data\eidon.db "backups\eidon-$stamp.db"
Get-Item "backups\eidon-$stamp.db"
```

## Validação

O arquivo deve existir e possuir tamanho maior que zero.

## Regra

Nunca publique backups no GitHub. Eles podem conter informações pessoais.
