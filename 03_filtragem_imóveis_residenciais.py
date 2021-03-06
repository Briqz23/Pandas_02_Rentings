# -*- coding: utf-8 -*-
"""03_Filtragem_Imóveis_Residenciais

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qm1CmBjTpgje7pt55vyCevScr9D5k16z

#Importando dados
"""

import pandas as pd
dados = pd.read_csv("aluguel.csv", sep=";")

"""#Visão Geral"""

#dados.info()
dados.head(9)

tipos_de_dados = pd.DataFrame(dados.dtypes, columns = ['Tipos de Dados']) #atributo estava como "0"
tipos_de_dados.columns.name = "Variáveis" #Renomeando a coluna da extrema esquerda.
print(tipos_de_dados)

print(f'Tuplas (Registros de Imoveis) : {dados.shape[0]}\nAtributos (Variáveis): {dados.shape[1]}\n\nAssim, configura-se uma tabela de y = {dados.shape[0]} e x = {dados.shape[1]}')

"""# Relatório de Análise II
## Tipos de Imóveis (primeiro atributo)
"""

tipo_de_imovel = dados['Tipo'].drop_duplicates()

# ou tipo_de_imovel.drop_duplicates(inplace = True)

tipo_de_imovel = pd.DataFrame(tipo_de_imovel)

#arrumar o index (0,1,2,3... fim)
tipo_de_imovel.index = range(tipo_de_imovel.shape[0])

#arrumando coluna Index
tipo_de_imovel.columns.name = 'Id'
index = ['Linha ' + str(i) for i in range (tipo_de_imovel.shape[0])]
tipo_de_imovel.columns = ['Tipos de Imóveis']
print(pd.DataFrame(tipo_de_imovel))

#Filtragem para APENAS lugares RESINDENCIAIS
residencial = ['Quitinete', 
'Casa',
'Apartamento',
'Casa de Condomínio',
'Casa de Vila']

dados['Tipo'].isin(residencial).head(10)
selecao = dados['Tipo'].isin(residencial)
#agora só entrarão as variáveis classificadas como TRUE em SELEÇÃO e, portanto, em dados_residencial
dados_residencial = dados[selecao]

#Tratando da tabela com apenas lugares RESIDENCIAIS

dados_residencial.index = range(dados_residencial.shape[0])
print(dados_residencial.head(10))