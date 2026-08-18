# 🏛️ Eidon OS

**Eidon OS** é uma plataforma pessoal de conhecimento e evolução. O núcleo pertence ao próprio Eidon: memória, projetos, atividades, metas, analytics e dados permanecem independentes do provedor de inteligência artificial.

> **Missão:** construir, preservar e transformar contexto em decisões.

## Estado atual — v0.5.0 Eidon Web + AI Integration Foundation

A v0.5.0 mantém o Personal Intelligence Core e adiciona uma interface web própria. Nesta atualização, o Eidon passa a ter também uma camada de inteligência integrada ao núcleo local.

### Entregas atuais

- [x] FastAPI + comando `eidon-web`;
- [x] dashboard web com projetos, conhecimento, atividades e metas;
- [x] AI Gateway desacoplado do domínio;
- [x] primeiro provedor: OpenAI / ChatGPT via OpenAI API;
- [x] configuração visual de provedor, modelo e chave de API;
- [x] chat visual dentro do Eidon Web;
- [x] ferramentas de leitura para dashboard, atividades, metas, projetos e conhecimento;
- [x] ferramentas de escrita para atividades, metas, projetos e conhecimento;
- [x] remoção controlada de registros com autorização visual por mensagem;
- [x] chave de API nunca retornada pela API do Eidon e mantida somente em memória quando inserida pela interface;
- [x] testes locais da camada de ferramentas da IA.

## Arquitetura

```text
Usuário
  ↓
Eidon Web
  ├── Dashboard
  └── Eidon IA
        ↓
     AI Gateway
        ↓
 OpenAI / futuros provedores
        ↓
   Eidon Tools
        ↓
 Application / Repositories
        ↓
      SQLite
```

A IA não recebe acesso SQL bruto. Ela opera por ferramentas controladas que respeitam o núcleo do Eidon.

> **A IA acessa o Eidon; o Eidon não pertence à IA.**

## Configurar OpenAI / ChatGPT

Instale a versão atual da branch:

```powershell
git switch v0.5.0
git pull
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
eidon-web
```

Acesse:

```text
http://127.0.0.1:8000
```

Na seção **Eidon IA**, escolha `OpenAI / ChatGPT`, informe o modelo e a chave da API. A chave digitada na interface existe somente durante o processo atual.

Para configuração persistente e segura, prefira uma variável de ambiente:

```powershell
$env:OPENAI_API_KEY="sua-chave"
$env:EIDON_AI_MODEL="gpt-5"
eidon-web
```

Nunca envie a chave da API para o GitHub.

## Endpoints

```text
GET  /health
GET  /api/dashboard
GET  /api/activities
GET  /api/goals
GET  /api/ai/status
POST /api/ai/config
POST /api/ai/chat
```

## Segurança operacional

A IA pode ler e registrar informações no Eidon. Exclusões são bloqueadas por padrão e somente ficam disponíveis quando a opção **Autorizar exclusões nesta mensagem** é marcada na interface.

## Próximas versões

1. **v0.5.1 — Eidon Web Experience** — identidade visual profissional, arquitetura da informação, navegação, dashboard refinado, estados de interface e visualizações úteis.
2. **v0.6.0 — Intelligence Expansion** — novos provedores, permissões mais granulares, histórico/auditoria e evolução do AI Gateway.
3. **v0.7.0 — Semantic Memory / RAG** — embeddings, busca semântica e recuperação de contexto.
4. **v0.8.0 — Agents & Automation** — especialistas e automações controladas.
5. **v1.0.0 — Eidon OS** — plataforma pessoal estável e integrada.

## Testes

```powershell
python -m unittest discover -s tests -v
```

## Frase de ativação

> **Está na hora do show.**

## Licença

MIT.
