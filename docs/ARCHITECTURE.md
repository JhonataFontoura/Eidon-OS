# Arquitetura do Eidon OS

O núcleo funcional segue uma separação inspirada em Arquitetura Limpa:

- `domain`: entidades e regras de negócio sem dependências externas;
- `application`: casos de uso e contratos de persistência;
- `infrastructure`: detalhes técnicos, como SQLite;
- `cli`: interface de entrada para o usuário.

A regra de dependência aponta para dentro: infraestrutura conhece a aplicação e o domínio, mas o domínio não conhece SQLite, terminal ou frameworks.
