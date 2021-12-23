import pandas as pd
import numpy as np
np.random.seed(100)



df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                   'C': ['C0', 'C1', 'C2', 'C3'],
                   'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                       'B': ['B4', 'B5', 'B6', 'B7'],
                       'C': ['C4', 'C5', 'C6', 'C7'],
                       'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7])
   
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                     'C': ['C8', 'C9', 'C10', 'C11'],
                      'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])

dicionario = {'ID':[10,11,12,13,14,],'NOME':['Mario','Joana','Claudia','Lucas','Gabriel'],
              'CIDADE':['SÃO PAULO','RIO DE JANEIRO','SÃO PAULO','CAMPINAS','PORTO ALEGRE']}
dicionario2 = {'ID':[16,11,12,13,18,],'Experiência':['Junior','Senior','Pleno','Estagiário','Analista']}

df4 = pd.DataFrame(data=dicionario)
df5 = pd.DataFrame(data=dicionario2)

dicionario = {'NOME':['Mario','Joana','Claudia','Lucas','Gabriel'],
              'CIDADE':['SÃO PAULO','RIO DE JANEIRO','SÃO PAULO','CAMPINAS','PORTO ALEGRE']}

dicionario2 = {'Experiência':['Junior','Senior','Pleno','Estagiário','Analista']}

df7 = pd.DataFrame(data=dicionario)
df8 = pd.DataFrame(data=dicionario2)

print(df1)
print(df2)
print(df3)


df_concat = pd.concat([df1,df2])   #lembrar dos colchetes

print(df_concat)

df_concat2 = pd.concat([df1,df2,df3])

print(df_concat2)

df_concat3 = pd.concat([df1, df2], axis = 1)    #vai juntar todas as colunas

print(df_concat3)

#merge inner
print('merge inner:')
merge_inner = pd.merge(df4,df5)

print(merge_inner)         #junta só o que tem de igual nos dois

#merge outer
print('merge outer:')
merge_outer = pd.merge(df4, df5, how ='outer')

print(merge_outer)

#merge left
print('merge left:')
merge_left = pd.merge(df4, df5, how = 'left')

print(merge_left)

#join

join_esq = df4.join(df5, lsuffix='_X', rsuffix='_Y')

print(join_esq)

join_esq2 = df7.join(df8)

print(join_esq2)


