import pandas as pd
from extractor import extract_data

# função para puxar os dados extraídos e apresentar o json puro, 
# usar o pandas para organizar e filtrar dados
def transform_data():
    pure_data = extract_data("https://servicodados.ibge.gov.br/api/v1/localidades/municipios")
    #json_normalize para organização dos dados
    response = pd.json_normalize(pure_data)
    response = response[['id', 'nome', 'microrregiao.mesorregiao.UF.sigla', 'microrregiao.mesorregiao.UF.nome']]
    print(response.head())
    print(response.columns)


data = transform_data()