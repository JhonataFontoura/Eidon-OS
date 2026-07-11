# ADR-001 — SQLite como banco local

## Status

Aceita.

## Contexto

O Eidon OS precisa preservar memórias localmente antes de depender de integrações externas.

## Decisão

Usar SQLite na primeira implementação do banco local.

## Motivos

- não exige servidor;
- está disponível na biblioteca padrão do Python;
- oferece transações e persistência em arquivo;
- facilita instalação e uso offline;
- mantém a infraestrutura substituível por meio do contrato `MemoryRepository`.

## Consequências

A solução é adequada para uso pessoal e desenvolvimento inicial. Escalabilidade distribuída, sincronização e acesso concorrente avançado ficarão para versões futuras.
