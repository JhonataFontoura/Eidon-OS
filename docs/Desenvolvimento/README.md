# Guia de Desenvolvimento do Eidon OS

Este diretório reúne a documentação técnica necessária para instalar, executar, testar, manter e evoluir o Eidon OS.

## Índice

1. [Ambiente](01_Ambiente.md)
2. [Dependências](02_Dependencias.md)
3. [Banco SQLite](03_Banco_SQLite.md)
4. [Dashboard](04_Dashboard.md)
5. [Testes](05_Testes.md)
6. [Releases](06_Releases.md)
7. [Deploy](07_Deploy.md)
8. [Troubleshooting](08_Troubleshooting.md)

## Princípios

- Código Limpo e Arquitetura Limpa.
- Evolução incremental e versionada.
- Dependências explícitas e mínimas.
- Persistência local controlada pelo usuário.
- Documentação atualizada junto com o código.
- Automação somente com autorização.

## Fluxo recomendado

```text
Preparar ambiente
      ↓
Criar branch
      ↓
Implementar e testar
      ↓
Atualizar documentação
      ↓
Abrir Pull Request
      ↓
Publicar versão
```

Para tarefas operacionais, consulte também `docs/Runbooks/`.
