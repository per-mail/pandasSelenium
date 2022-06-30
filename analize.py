import pandas as pd
import seaborn as sns

df = pd.read_csv("C:\\Users\\dfg\\Desktop\\stoloto\\data\\draw.csv")


#r = sns.heatmap(df[['a','b']].corr())

#отбираем строки по условиям
#r = df.query('a == 26 &  b == 1 &  c == 22 &  d < 15')

draw = []
for i in range(1, 26):
#отбираем все строки у которых в столбце'a' число i    
    fil = df['a'] == i 
    r = df.loc[fil]#r строки у которых в столбце'a' число i
    print(i, r.shape)#r.shape-показывает кол-во строк и столбцов в одной r
    draw.append(r.shape[0])#shape[0]-берём кол-во строк
    
        
  
print(f'максимальное значение {max(draw)} ')
df2 = df.query('a == 9')


#повторяем это с df2-список у которого все а = 9, так-как чаще всего выпадают
draw2 = []
for i in range(1, 26):
#отбираем все строки у которых в столбце'b' число i    
    fil = df2['b'] == i 
    r = df2.loc[fil]
    print(i, r.shape)#r.shape-показывает кол-во строк и столбцов в одной r
    draw2.append(r.shape[0])#shape[0]-берём кол-во строк
    
print(f'максимальное значение {max(draw2)} ')
#Вывод с 9 чаще всего выпадает 6

df3 = df.query('a == 9 &  b == 6')


#повторяем это с dfc-список у которого все a == 9 &  b == 6', так-как чаще всего выпадают
draw3 = []
for i in range(1, 26):
#отбираем все строки у которых в столбце'c' число i    
    fil = df3['c'] == i 
    r = df3.loc[fil]
    if r.shape[0] != 0:
        print(r)
    #print(i, r.shape)#r.shape-показывает кол-во строк и столбцов в одной r
    draw3.append(r.shape[0])#shape[0]-берём кол-во строк
    
print(f'максимальное значение {max(draw3)} ')



