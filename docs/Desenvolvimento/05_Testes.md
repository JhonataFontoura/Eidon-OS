# 05 — Testes

## Objetivo

Garantir que novas funcionalidades preservem as regras de domínio e a persistência existente.

## Execução completa

```powershell
python -m unittest discover -s tests
```

## Estratégia

- Testes de domínio: validações e criação de entidades.
- Testes de casos de uso: comportamento sem depender da interface.
- Testes de repositório: gravação e leitura em banco temporário.
- Testes de exportação: estrutura e conteúdo mínimo do arquivo Excel.

## Boas práticas

- Cada teste deve verificar um comportamento claro.
- Bancos de teste devem ser temporários e isolados.
- O resultado não pode depender da ordem de execução.
- Bugs corrigidos devem receber um teste de regressão.
- Evite testar detalhes internos que não fazem parte do contrato.

## Checklist antes do commit

```text
[ ] Ambiente virtual ativo
[ ] Dependências instaladas
[ ] Testes executados
[ ] Sem banco real usado nos testes
[ ] Documentação atualizada
[ ] Alterações revisadas com git diff
```

Cobertura e integração contínua poderão ser incorporadas em versões futuras.
