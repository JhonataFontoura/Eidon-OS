# 04 — Dashboard

## Objetivo

Transformar dados do Eidon OS em indicadores compreensíveis sobre projetos, estudos, carreira e atividades.

## Camadas planejadas

```text
SQLite → Casos de uso → Analytics → Exportador → Excel/Web
```

A versão 0.4.0 oferece dashboard no terminal e exportação para Excel.

## Comandos

```powershell
eidon dashboard
eidon dashboard-export
```

Saída padrão:

```text
reports/eidon_dashboard.xlsx
```

Caminho personalizado:

```powershell
eidon dashboard-export --output reports\academia_de_codigo.xlsx
```

## Abas esperadas

- `Dashboard`: indicadores gerais.
- `Categories`: distribuição por categoria.
- `Timeline`: atividades ao longo do tempo.

## Academia de Código

Meta mensal inicial:

- 40 desafios concluídos.
- 25 horas de estudo.
- 4 plataformas utilizadas.
- 3 tecnologias praticadas.

Métricas futuras:

- dificuldade dos desafios;
- linguagem utilizada;
- plataforma;
- tempo gasto;
- resolução com ou sem ajuda;
- temas praticados;
- sequência de dias de estudo.

## Regra de projeto

O dashboard não deve acessar diretamente detalhes do SQLite. Ele deve consumir resultados da camada de aplicação, mantendo o exportador substituível por uma futura interface web.
