# Runbook — Restaurar Banco

## Atenção

A restauração substitui o banco atual. Faça uma cópia dele antes de continuar.

## Procedimento

```powershell
$backup = "backups\eidon-AAAAMMDD-HHMMSS.db"
Copy-Item data\eidon.db data\eidon-before-restore.db
Copy-Item $backup data\eidon.db -Force
```

Depois valide:

```powershell
eidon list
eidon project-list
eidon activity-list
eidon dashboard
```

## Recuperação

Se o backup restaurado estiver incorreto:

```powershell
Copy-Item data\eidon-before-restore.db data\eidon.db -Force
```

## Checklist

```text
[ ] Aplicação fechada
[ ] Banco atual preservado
[ ] Backup selecionado corretamente
[ ] Comandos de consulta funcionando
```
