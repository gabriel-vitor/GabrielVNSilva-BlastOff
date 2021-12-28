import pandas as pd
import numpy as np
np.random.seed(100)

indices = ['janeiro','março','maio', 'junho', 'agosto', 'outubro', 'novembro']

colunas = np.arange(1, 32)

dados = np.random.randint(492, 2050, size=(7, 31))

print(colunas)

print(dados)

df = pd.DataFrame(data=dados, index = indices, columns = colunas)

print(df)

print(df[2])

print(df[[1, 2, 3]])

print(df[2][2])

print(df[:2])

print(df[2:])

print(df.loc['junho', 30])  

print(df.iloc[3, 30])

#print(df.loc[[1, 2, 3], [1, 2, 3]])  #não está funcionando

#quanto vendeu no dia 10 de todos os meses?

print(df[10])

#quanto vendeu nos dias 10, 20 e 30 de todos os meses?

print(df[[10, 20 ,30]])

#quanto vendeu no dia 15 de março?

print(df[15][1])

#quanto vendeu os meses de janeiro, março e maio?

print(df[:3])

#vendas de julho, agosto e outubro: [...]