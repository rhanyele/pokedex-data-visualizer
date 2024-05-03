import streamlit as st
import pandas as pd
import os
from pokedex import carregar_pokedex

# Função para carregar os dados da Pokédex
@st.cache_data
def carregar_dados():
    caminho_arquivo = "data/pokedex.csv"
    if not os.path.exists(caminho_arquivo):
        carregar_pokedex()
    # Carregar os dados da Pokédex e forçar o ID como string
    return pd.read_csv(caminho_arquivo, dtype={"Id": str}).sort_index()

# Função para criar um botão personalizado para cada tipo de Pokémon
def criar_botao_tipo(tipo, align="left"):
    cor = cores_tipo_pokemon.get(tipo, "black")
    return f'<button style="background-color:{cor}; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer; margin: 5px; float: {align};">{tipo}</button>'

# Configurações da página
st.set_page_config(page_title="Pokédex", page_icon="img/pokedex.png", layout='wide')

# Mapeamento de cores para cada tipo de Pokémon
cores_tipo_pokemon = {
    "Normal": "#A8A878",
    "Fire": "#F08030",
    "Water": "#6890F0",
    "Electric": "#F8D030",
    "Grass": "#78C850",
    "Ice": "#98D8D8",
    "Fighting": "#C03028",
    "Poison": "#A040A0",
    "Ground": "#8B4513",
    "Flying": "#808080",
    "Psychic": "#F85888",
    "Bug": "#2E8B57",
    "Rock": "#B8A038",
    "Ghost": "#705898",
    "Dragon": "#7038F8",
    "Dark": "#705848",
    "Steel": "#B8B8D0",
    "Fairy": "#EE99AC"
}

# Carregar os dados da Pokédex
pokedex_original = carregar_dados()
nomes_pokemon = pokedex_original["Nome"].unique().tolist()

# Interface do usuário
st.title("Pokédex")

col1, col2 = st.columns(2)
with col1:
    filtro_id = st.text_input("Filtrar por Id:", "")
with col2:
    filtro_nome = st.multiselect("Filtrar por Nome:", nomes_pokemon)

pokedex = pokedex_original.copy()

if filtro_id:
    pokedex = pokedex[pokedex["Id"].astype(str).str.contains(filtro_id)].reset_index()
if filtro_nome:
    filtro_nome_str = "|".join(filtro_nome)
    pokedex = pokedex[pokedex["Nome"].str.contains(filtro_nome_str)].reset_index()

st.divider()

MAX_COLUNAS_POR_LINHA = 3
linha = st.columns(MAX_COLUNAS_POR_LINHA)
for index, pokemon in pokedex.iterrows():
    if index > 0 and index % MAX_COLUNAS_POR_LINHA == 0:
        st.write('\n')
    with linha[index % MAX_COLUNAS_POR_LINHA]:
        st.subheader(f'{pokemon.Nome} - #{pokemon.Id}')
        st.image(pokemon.urlImagem)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                criar_botao_tipo(pokemon.Tipo1, "right"),
                unsafe_allow_html=True
            )
        with col2:
            if pd.notna(pokemon.Tipo2):
                st.markdown(
                    criar_botao_tipo(pokemon.Tipo2, "left"),
                    unsafe_allow_html=True
                )
        st.divider()
