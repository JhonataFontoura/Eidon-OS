# Banco de dados local

## Objetivo

Persistir memórias do Palácio sem depender de serviços externos.

## Escolha técnica

Foi adotado SQLite por ser leve, local, transacional e disponível na biblioteca padrão do Python.

## Limites da primeira versão

A versão inicial permite:

- criar memórias;
- listar memórias;
- recuperar memória por identificador;
- persistir título, conteúdo, categoria, origem e datas.

## Próximas evoluções

- atualizar e remover memórias;
- busca textual;
- filtros por categoria;
- migrações de esquema;
- criptografia de dados sensíveis;
- API local;
- interface web.
