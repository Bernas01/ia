import streamlit as st
import pandas as pd
from io import StringIO

# Os dados fornecidos
data = """
NAME    BLOOD STATUS    Species    GENDER    HOUSE    HAIR COLOR    BOGGART    PATRONUS    Nationality    ALIVE?
Harry Potter    Half-blood    Human    Male    Gryffindor    Jet-black    Dementor    Stag    English    Yes
Minerva McGonagall    Half-blood    Human    Female    Gryffindor    Black    Lord Voldemort    Cat    Scottish    Yes
# ... (restante dos dados) ... 
Unknown Giant    Giant    Male    No"""

# Converter a string de dados em um objeto DataFrame do pandas
df = pd.read_csv(StringIO(data), delimiter='\t', engine='python')

# Usando Streamlit para mostrar a tabela
st.write(df)
