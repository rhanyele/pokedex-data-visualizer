import logging
import os
import pandas as pd
from api.imagem import baixar_imagem
from api.pokemon import dataframe_pokemon

logging.basicConfig(level=logging.INFO, filename=".log", filemode='w', format="%(asctime)s - %(levelname)s - %(message)s", encoding='utf-8')

def validar_arquivo_e_pasta():
    caminho_pasta = "data"
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
    
    caminho_arquivo = os.path.join(caminho_pasta, "pokedex.csv")
    if not os.path.exists(caminho_arquivo):
        df_vazio = pd.DataFrame(columns=["Id", "Nome", "Tipo1", "Tipo2", "urlImagem"]) 
        df_vazio.to_csv(caminho_arquivo, index=False)

    return caminho_arquivo

def carregar_pokedex():
    caminho_arquivo = validar_arquivo_e_pasta()

    try:
        df_existente = pd.read_csv(caminho_arquivo)
        
        for pokemon in range(1, 1026):
            logging.info(f"Extraindo dados do Pokémon {pokemon}...")
            
            if str(pokemon) not in df_existente["Id"].values:
                df_pokemon = dataframe_pokemon(pokemon)
                df_pokemon['urlImagem'] = baixar_imagem(pokemon)
                
                modo = 'w' if pokemon == 1 else 'a'
                header = pokemon == 1
                df_pokemon.to_csv(caminho_arquivo, mode=modo, header=header, index=False)
            else:
                logging.info(f"O Pokémon com ID {pokemon} já existe na Pokédex.")
    except Exception as e:
        logging.error(f"Erro ao carregar a Pokédex: {e}")

if __name__ == '__main__':
    logging.info('########## INICIO DA EXECUCAO ##########')
    carregar_pokedex()
    logging.info('########## FIM DA EXECUCAO ##########')
