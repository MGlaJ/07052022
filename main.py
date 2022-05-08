# notatki z zajęć z 07052022
# pandas 1.4.0
# openpyxl najnowsza wersja
# numpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# a=np.array([20,30,40,50])
# b=np.arange(4)
# c=a+b
# print(c)
# d=np.sqrt(b)
# print(d)
# e=d+c
# print(e) #numpy sam określa typ
# a=np.arange(12).reshape((3,4))
# print(a)
# print(a.sum())#suma wszystkich el
# print(a.sum(axis=0)) #dla kolumn
# print(a.sum(axis=1)) #dla wierszy
# print(a.cumsum(axis=1))
# a=np.arange(3)
# b=np.arange(3)
# print(np.dot(a,b))
# print(a.dot(b))
# c= np.arange(3)
# d =np.array([[0],[1],[2]])
# print(c.dot(d))
# e=np.array([[2,4,5],[5,1,7]])
# f=np.array([[2,3],[4,2],[6,1]])
# print(np.dot(e,f))
# a=np.arange(6).reshape((3,2))
# print(a)
# for b in a:
#     print(b)
#
# a = np.arange(6).reshape((3, 2))
# print(a)
# print(a.flat)
# for b in a:
#     print(b)
#     for c in b:
#         print(c)

# a=np.arange(12).reshape((3,4))
# print(a)
# b=a.reshape((4,3))
# print(a)
# c=b.ravel()
# print(c)
#
# c=np.arange(12).reshape((3,4))
# print(c)
# print(c.T)
# s=pd.Series([1,2,3,5,'a',5.5])
# print(s)
# s=pd.Series([10,12,14,8], index=['a','b','c', 'd'])
# print(s)
# data={'kraj': ['Belgia','Indie', 'Brazylia'],
#       'stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#       'populacja': [545454545,4646464646,646464]}
# df=pd.DataFrame
# print(df)
# daty=pd.date_range('20220507', periods=5)
# df2- pd.DataFrame(np.random.rand(5,4),index=daty, columns=list('ABCD'))
# print(df2)
#
# df3=pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df3)
#
# xlsx=pd.ExcelFile('imiona.xlsx')
# df=pd.read_excel(xlsx, header=0)
# print(df)
# print(df.head(10))
# print(df.tail(10))
#
# df3.to_csv('dane2.csv', index=False)
# df.to_exvel('imiona2', sheet_name='dane')
#
# print(s['a'])
# print(s.a)
# print(df[0:1])
# print(df['Kraj'])
# print(df.Kraj)
# print(df.iloc[[0],[0]])
# print(df.loc[[0],['Kraj']])
# print(df.at[0,'Kraj'])

# # notatki 08052022
# s=pd.Series([10,12,14,8], index=['a','b','c', 'd'])
# print(s)
# data={'kraj': ['Belgia','Indie', 'Brazylia'],
#       'stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#       'populacja': [545454545,4646464646,646464]}
# df=pd.DataFrame
# print(df)
# xlsx=pd.ExcelFile('imiona.xlsx')
# df4=pd.read_excel(xlsx, header=0)
# print(df4)
# # print (df4.head()) #pięć pierwszych wierszy
# # #analogicznie tail domyślnie 5
# # print(df4.sample()) #wyciąganie losowo jednego wiersza, nie możńa podać większej liczby niż liczba wierszy w danym
# # # #print(df.sample(10, replace=True))
# # print(s['a'])
# # print(s.a) #element w klasie
# # print(df['Kraj'])
# # print(df.Kraj)
# #
# # #cięcia
# # print(df[0:1])
# #
# # print(df.iloc[[0],[0]])
# # print(df.loc[[0], ['Kraj']])
# # print(df.at[0, 'Kraj'])
# # #wiersz, nazwa kolumny
# # print(s[s>9])
# # #wyświetla elementy serii spełniające warunek
# # print(s.where(s>10))
# # #w miejscach gdzie niespełniony warunek wyświetla się maska
# # print(s.where(s>10, 'warunek niespełniony'))
# # #where zwraca kopię
# # seria=s.copy()
# # seria.where(s>10, 'niespełniony', inplace=True)
# # print(seria)
# #
# # print(df[df['Populacja']>12000])
# # print(df[(df['Populacja']>100000)&(df.index.isin([0,2]))])
# #
# #DODAawanie elementu do serii
# s['e']=15
# print(s)
# df.loc[3]= 'nowy element'
# print(df)
# df.loc[4]= ['Polska','Warszawa', 35897899]
# print(df)
#
# new_df=df.drop([3])
# print(new_df)
# df.drop([3], inplace=True)
# #inplace zmienia na stałe
# df['Kontynent']=['Europa','Azja', 'Ameryka Południowa', 'Europa']
# print(df)
# df.sort_values('Kraj')
# #sortowanie po kraju
# print(df)
#
# #grupowania
# grupa=df.groupby('Kontynent')
# print(grupa.get_group('Europa'))
# print(df.groupby('Kontynent').agg({'Populacja': ['sum']}))
#
# #matplotlib 3.5.1
#
# grupa.plot(kind='bar')
# plt.show()
# grupa.plot(kind='bar', xlabel='kontynent', ylabel='Populacja w mld', rot=0, titla='Populacje na kontynentach', legend=True)
# #2.sposób
#
# wykres=grupa.plot.bar()
# print(wykres)
# wykres.set_xlabel('Kontynenty')
# wykres.set_ylabel('Populacja w mld')
# wykres.ticks_params(axis='x', labelrotation=0)
# wykres.set_title('Populacje na kontynentach')
#
# plt.show()
#
# #wykres kołowy
# df3=pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df3)
# grupa=df3.groupby('Imię i nazwisko').agg({'Wartość zamówienia':['sum']})
# print(grupa)
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',
#            fontsize=20, colors=['red','green'])
# plt.legend(loc='upper left')
# plt.show()
# plt.savefig('plot.png')

seria= pd.Series(np.random.randn(1000))
seria.cumsum()
print(seria)
seria.plot()
plt.show()