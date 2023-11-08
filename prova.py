import pandas as pd

# Os dados fornecidos
data = """NAME    BLOOD STATUS    Species    GENDER    HOUSE    HAIR COLOR    BOGGART    PATRONUS    Nationality    ALIVE?
Harry Potter    Half-blood    Human    Male    Gryffindor    Jet-black    Dementor    Stag    English    Yes
Minerva McGonagall    Half-blood    Human    Female    Gryffindor    Black    Lord Voldemort    Cat    Scottish    Yes
# ... (restante dos dados) ... 
Unknown Giant    Giant    Male    No"""

# Converter a string de dados em um objeto DataFrame do pandas
# Aqui estou simulando a leitura dos dados fornecidos, que podem ser obtidos de um arquivo CSV ou de uma fonte de dados
# Devido ao limite de caracteres, apenas um pequeno trecho foi inserido
# Certifique-se de que a string contém todos os dados no formato de tabela e não tenha sido truncada

# Supondo que a string é um arquivo CSV ou uma tabela, use o método StringIO para simulá-lo
from io import StringIO
df = pd.read_csv(StringIO(data), delimiter='\t', engine='python')

# Exibindo as primeiras linhas para verificar se os dados foram lidos corretamente
print(df.head())
