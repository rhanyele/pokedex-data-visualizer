import requests
import logging
import pandas as pd
from model.Model import validarDadosPokemon

def extrair_pokemon_api(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/'
    logging.info(url)

    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta exceção se a solicitação falhar
        dadosJson = response.json()
        return dadosJson
    except requests.exceptions.RequestException as e:
        logging.critical(f"Erro ao extrair dados do Pokémon {pokemon}: {e}")

def dataframe_pokemon(pokemon):
    dados = extrair_pokemon_api(pokemon)

    if dados:
        pokemon_id = str(dados["id"]).zfill(4)
        pokemon_nome = dados["name"].capitalize()
        pokemon_tipos = [tipo["type"]["name"].capitalize() for tipo in dados["types"]]
        pokemon_tipo1 = pokemon_tipos[0]
        pokemon_tipo2 = pokemon_tipos[1] if len(pokemon_tipos) > 1 else None

        dados_pokemon = {
            "Id": pokemon_id,
            "Nome": pokemon_nome,
            "Tipo1": pokemon_tipo1,
            "Tipo2": pokemon_tipo2
        }
        
        logging.info("Validando os dados.")
        if validarDadosPokemon(dados_pokemon):
            df = pd.DataFrame([dados_pokemon])
            return df
        else:
            logging.critical(f"Dados inválidos para o Pokémon {pokemon}.")
    else:
        logging.critical(f"Não foi possível obter dados para o Pokémon {pokemon}.")
