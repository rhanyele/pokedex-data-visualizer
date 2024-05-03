from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional
import logging

# Define um modelo Pydantic para representar um Pokémon individual
class Pokemon(BaseModel):
    Id: str = Field(..., min_length=4, max_length=4)  # ID do Pokémon com exatamente 4 caracteres
    Nome: str          # Nome do Pokémon 
    Tipo1: str         # Tipo primário do Pokémon
    Tipo2: Optional[str]  # Tipo secundário do Pokémon (opcional)

# Define um modelo Pydantic para representar uma lista de Pokémon
class PokemonList(BaseModel):
    pokemons: List[Pokemon]  # Lista de objetos Pokemon

def validarDadosPokemon(pokemon_data):
    try:
        pokemon = Pokemon(**pokemon_data)
        # Cria um log com os dados validados
        logging.info(f"Dados válidos: {pokemon.model_dump()}")  
        return True
    except ValidationError as e:
        # Cria um log com os erros de validação
        logging.error(f"Erro de validação no registro{pokemon_data}: {e.errors()}")
        return False
