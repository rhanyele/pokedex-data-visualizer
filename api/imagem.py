import requests
import logging
import os
import shutil

def formatar_numero_pokemon(numeroPokemon):
    if numeroPokemon < 999:
        return str(numeroPokemon).zfill(3)
    else:
        return str(numeroPokemon)

def verificar_ou_criar_pasta(pasta):
    if not os.path.exists(pasta):
        os.makedirs(pasta)

def imagem_existe(pastaArquivo, nome_arquivo):
    return os.path.exists(os.path.join(pastaArquivo, nome_arquivo))

def baixar_imagem(pokemon):
    numeroPokemon = formatar_numero_pokemon(pokemon)
    nomeArquivo = f"{numeroPokemon}.png"
    pastaArquivo = 'img'

    if not imagem_existe(pastaArquivo, nomeArquivo):
        url_imagem = f'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/{numeroPokemon}.png'

        try:
            resposta = requests.get(url_imagem, stream=True)
            resposta.raise_for_status()  # Lança exceção se a solicitação falhar

            verificar_ou_criar_pasta(pastaArquivo)

            with open(os.path.join(pastaArquivo, nomeArquivo), 'wb') as arquivo:
                resposta.raw.decode_content = True
                shutil.copyfileobj(resposta.raw, arquivo)

            logging.info(f"Imagem {numeroPokemon} baixada com sucesso!")
        except requests.exceptions.RequestException as e:
            logging.error(f"Falha ao baixar a imagem {numeroPokemon}: {e}")
    else:
        logging.info(f"A imagem {numeroPokemon} já existe. Não é necessário baixar novamente.")

    return f'{pastaArquivo}/{nomeArquivo}'