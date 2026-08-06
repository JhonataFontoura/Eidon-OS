# 07 — Deploy e Distribuição

## Estado atual

O Eidon OS é executado localmente como pacote Python instalado em modo editável. Ainda não existe distribuição estável para usuário final.

## Execução de desenvolvimento

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
eidon --help
```

## Caminhos futuros

1. Pacote Python instalável.
2. Executável para Windows.
3. API local.
4. Interface web ou desktop.
5. Contêiner Docker para ambientes controlados.

## Requisitos de segurança

- O banco local não deve ser publicado no repositório.
- Segredos e tokens devem ficar em variáveis de ambiente.
- Integrações externas devem usar permissões mínimas.
- Backups devem ser criados antes de migrações.
- A autonomia dos agentes deve respeitar autorização explícita.

## Critérios para um deploy estável

- testes automatizados aprovados;
- instalação reproduzível;
- documentação de atualização;
- mecanismo de backup e restauração;
- logs de erro compreensíveis;
- versão e changelog consistentes.
