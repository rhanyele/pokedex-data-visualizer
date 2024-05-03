# Projeto Pokédex Data Visualizer

O projeto é uma aplicação Python desenvolvida com o framework Streamlit, criada para construir uma Pokédex ao extrair dados e imagens dos Pokémon. Os dados são processados e armazenados em um arquivo CSV, permitindo a criação de uma página web interativa.

A Pokédex é uma enciclopédia virtual presente no universo Pokémon que contém informações sobre várias espécies de Pokémon, incluindo seus nomes, números de identificação, tipos, habilidades e imagens.

As [imagens](https://www.pokemon.com/br/pokedex) são obtidas da Pokédex oficial do site Pokémon.

![pokemon](https://github.com/rhanyele/pokedex-data-visualizer/assets/10997593/c685458f-ca15-4639-b0da-28faa1ac0322)

### Documentação da API
- [Pokémon API](https://pokeapi.co/)

## Estrutura do projeto
```bash
- api
  - imagem.py
  - pokemon.py
- data
  - pokedex.csv
- img
  - 0001.png
  - 0002.png
  - 0003.png
  - ...
- model
  - Model.py
- app.py
- pokedex.py
```
## Funcionalidades
- **Extrair imagem do Pokémon:** Busca as imagem do Pokémon da Pokédex oficial.
- **Extrair dados do Pokémon:** Busca dados de Pokémon na API do PokeAPI.
- **Model:** Faz a validação dos dados para garantir que estão no formato e tipo esperado.
- **Carregar Pokédex:** Carrega os dados transformados em um arquivo de dados CSV.
- **App:** Visualização da Pokédex com os dados e as imagens.

## Requisitos
- Python
- Poetry
- Pandas
- Pydantic
- Logging
- Streamlit


## Instalação
1. Clone este repositório:

   ```bash
   git clone https://github.com/rhanyele/pokedex-data-visualizer.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd pokedex-data-visualizer
   ```

3. Instale as dependências usando Poetry:

   ```bash
   poetry install
   ```

## Uso
Faça a carga dos dados e baixe as imagens:

```bash
poetry run python pokedex.py
```

Execute o app:

```bash
poetry run streamlit run app.py
```
## Demonstração 
![Gravando 2024-05-03 140827](https://github.com/rhanyele/pokedex-data-visualizer/assets/10997593/60e7a5ec-5f40-466e-adcb-978d3c55920c)

## Contribuição
Sinta-se à vontade para contribuir com novos recursos, correções de bugs ou melhorias de desempenho. Basta abrir uma issue ou enviar um pull request!

## Autor
[Rhanyele Teixeira Nunes Marinho](https://github.com/rhanyele)

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).
