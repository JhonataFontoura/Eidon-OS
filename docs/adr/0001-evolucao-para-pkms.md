# ADR-0001 — Evolução para uma plataforma de gestão do conhecimento pessoal

- **Status:** Aceita
- **Data:** 2026-07-11

## Contexto

A primeira versão persistia apenas memórias textuais. Essa estrutura validou o armazenamento local, mas não representa a visão de conectar arquivos, projetos, pessoas, empresas, conhecimento e decisões.

## Decisão

O Eidon OS evoluirá para uma Plataforma de Gestão do Conhecimento Pessoal (PKMS), organizada em quatro núcleos: Conhecimento, Inteligência, Sistema e Especialistas.

A Era II começa com entidades separadas para memórias, arquivos, projetos, pessoas, empresas e itens de conhecimento, além de relações genéricas entre registros.

## Consequências

- O banco SQLite passa a possuir múltiplas tabelas.
- O domínio permanece independente da tecnologia de persistência.
- Novos tipos podem ser adicionados sem transformar a entidade `Memory` em um objeto genérico e excessivo.
- Relações permitem construir o grafo lógico do Palácio da Memória.
- Importação de arquivos, embeddings e RAG ficam adiados para eras posteriores.
