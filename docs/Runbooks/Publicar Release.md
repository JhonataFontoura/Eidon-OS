# Runbook — Publicar Release

## Pré-requisitos

Pull Request revisado, testes aprovados e documentação atualizada.

## Checklist de versão

```text
[ ] pyproject.toml atualizado
[ ] README atualizado
[ ] CHANGELOG atualizado
[ ] Testes aprovados
[ ] Banco compatível ou migração documentada
[ ] Branch sincronizada
```

## Procedimento sugerido

```powershell
python -m unittest discover -s tests
git status
git add .
git commit -m "release: prepara versão X.Y.Z"
git push
```

Após a integração na branch escolhida:

```powershell
git tag -a vX.Y.Z -m "Eidon OS vX.Y.Z"
git push origin vX.Y.Z
```

Crie a release no GitHub usando o changelog como base e descreva impactos, instalação e possíveis migrações.
