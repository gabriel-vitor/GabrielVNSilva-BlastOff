import pandas as pd
import numpy as np
np.random.seed(100)

indices = ['janeiro','março','maio', 'junho', 'agosto', 'outubro', 'novembro']

colunas = np.arange(1, 32)

dados = np.random.randint(492, 2050, size=(7, 31))

print(colunas)

print(dados)

df = pd.DataFrame(data=dados, index = indices, columns = colunas)

#quanto vendeu no dia 10 de todos os meses?

print(df[10])

#quanto vendeu nos dias 10, 20 e 30 de todos os meses?

print(df[[10, 20 ,30]])

#quanto vendeu no dia 15 de março?

print(df[15][1])

#quanto vendeu os meses de janeiro, março e maio?

print(df[:3])

#vendas de junho, agosto e outubro nos dias 25 a 31:

print(df.loc[['junho', 'agosto', 'outubro'],[25, 26, 27, 28, 29 ,30, 31]])
print('-'*50)
print(df.iloc[[3, 4 ,5],[24, 25, 26, 27 ,28 ,29 ,30]]) #não pode ir até 31, senão dá erro.

df.rename({'novembro':'dezembro'}, inplace=True)
print('-'*100)
print(df)

print(df[df > 1000])
print('-'*100)
print(df[df > 1000].fillna('-'))

print(df[df > 1000][2])          #apenas um valor = colunas

print('-'*100)

print(df[df > 1000][0:3])     #linhas

#print(df[df > 1000][:][1, 2, 3, 4, 5])   #não funciona

print(df[df > 1000][:][[1, 2, 3, 4, 5]].fillna('-'))    #agora funciona

print(df[(df[10] > 1000) & (df[15] > 1500)])  #usando duas condições 'e'

print(df[(df[10] > 1000) | (df[15] > 1500)])  # 'ou'   