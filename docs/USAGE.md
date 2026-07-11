# Uso local

## Instalação

```bash
python -m venv .venv
pip install -e .
```

## Adicionar memória

```bash
eidon add --title "Título" --content "Conteúdo" --category "projetos"
```

## Listar memórias

```bash
eidon list
```

## Testes

```bash
python -m unittest discover -s tests
```
