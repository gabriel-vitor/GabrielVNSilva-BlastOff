
import pandas as pd
import numpy as np

df = pd.read_csv('campeonato-brasileiro-full.csv')

print('5 primeiros: \n\n', df.head())          #mostra os 5 primeiros

print(df.info())                               #informações

#qual foi a média de gols do time mandante (clube1)

print(df['Mandante Placar'])       #dados da coluna mandante placar

print(df['Mandante Placar'].mean())  #média dos dados

print(df['Visitante Placar'].mean())

df['Total de Gols'] = df['Mandante Placar'] + df['Visitante Placar']

print(df)

media_totalgols = df['Total de Gols'].mean()

print('a média de gols é:', media_totalgols)

#qual foi o time que mais venceu?
vitorias = df['Vencedor'].value_counts()

print(' times que mais venceram:\n\n ',vitorias)
#alguns noems irão se repetir por causa de caracteres maiusculos e minusculos
#é necessário corrigir

df['Vencedor'] = df['Vencedor'].str.upper()
vitorias = df['Vencedor'].value_counts()
print(' times que mais venceram:\n\n ',vitorias)

print(vitorias.head())

#qual o estado com o maior número de vitórias

print(df['Estado Vencedor'].value_counts())

#sort_values

print(df.sort_values(by = 'Mandante Placar', ascending=False))

#unique
df['Mandante'] = df['Mandante'].str.upper()

print(df['Mandante'].unique())

#nunique

print(df['Visitante'].nunique())
df['Visitante'] = df['Visitante'].str.upper()
print(df['Visitante'].nunique())

#qual foi a maior goleada de todos os tempos

print(df[df['Mandante Placar'] == df['Mandante Placar'].max()])

#qual o time fez mais gols no campeaonato brasileiro?

by_mandante = df.groupby('Mandante')

print(by_mandante['Mandante Placar'].sum().sort_values(ascending=False))