# 06 — Releases e Versionamento

## Padrão

O Eidon OS utiliza versionamento semântico:

```text
MAJOR.MINOR.PATCH
```

- `MAJOR`: mudanças incompatíveis.
- `MINOR`: novas funcionalidades compatíveis.
- `PATCH`: correções compatíveis.

## Linha evolutiva

- `0.1.0`: Fundação conceitual.
- `0.2.0`: estrutura inicial do sistema.
- `0.3.0`: Knowledge Core.
- `0.4.0`: Personal Intelligence.
- `0.5.0`: Semantic Intelligence, planejada.
- `0.6.0`: especialistas e autonomia, planejada.
- `1.0.0`: primeira versão estável.

## Regras

- Uma funcionalidade significativa deve nascer em branch própria.
- O número da versão precisa ser atualizado em `pyproject.toml`.
- Toda release deve atualizar `CHANGELOG.md` e README.
- Testes devem passar antes da tag.
- A versão publicada deve apontar para um commit revisado.

## Convenção de branches

```text
feat/nome-da-evolucao-v0.x.0
fix/descricao-curta
refactor/descricao-curta
docs/descricao-curta
```

Consulte o runbook `Publicar Release.md` para o procedimento completo.
