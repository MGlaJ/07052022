# notatki z zajęć z 07052022
# pandas 1.4.0
# openpyxl najnowsza wersja
# numpy
import numpy as np
import pandas as pd
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

xlsx=pd.ExcelFile('imiona.xlsx')
df=pd.read_excel(xlsx, header=0)
# print(df)
print(df.head(10))
print(df.tail(10))