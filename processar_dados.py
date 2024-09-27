#%%Importando os pacotes
import pandas as pd
import numpy as np
import fastparquet as ft
import os


#%% Importando o data frame
df_vendas = pd.read_csv("vendas.csv", sep=",", decimal=".")
df_vendas.info()

#%%Covertendo a data em datetime
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])

#%% Identificar e tratar dados inválidos (nulos, duplicados ou inconsistentes)

print(df_vendas.isnull().sum()) #Identificar Dados Nulos
print(df_vendas[df_vendas.duplicated()]) # Identificar Dados Duplicados
print(df_vendas.dtypes) #Verificar tipos incorretos:

#Não identifiquei dados inválidos, nulos, duplicados ou inconsistentes

#%%Salvar o DataFrame em Parquet
df_vendas.to_parquet("C:/Users/affon/test-infra/data/vendas.parquet", index=False, engine='fastparquet')