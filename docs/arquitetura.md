# Arquitetura do Eidon OS

O sistema é organizado em quatro núcleos evolutivos.

```text
Eidon OS
├── Núcleo do Conhecimento
├── Núcleo de Inteligência
├── Núcleo do Sistema
└── Núcleo dos Especialistas
```

## Núcleo do Conhecimento

Responsável por memórias, arquivos, projetos, pessoas, empresas, itens de conhecimento e relações.

## Núcleo de Inteligência

Responsável por busca semântica, classificação, embeddings, RAG e recomendações. Ainda não implementado.

## Núcleo do Sistema

Responsável por CLI, API, dashboard, configuração, persistência e integrações.

## Núcleo dos Especialistas

Responsável pelos papéis especializados do Conselho do Palácio e sua futura evolução para agentes.

## Camadas de software

```text
Interface -> Aplicação -> Domínio
                  ^
                  |
            Infraestrutura
```

O domínio não depende do SQLite, da CLI ou de futuras interfaces web. A infraestrutura implementa contratos definidos pela aplicação.
