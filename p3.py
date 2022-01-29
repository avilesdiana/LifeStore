"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

import numpy as np

from operator import itemgetter, attrgetter

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
#print(lifestore_searches[0])

#print(lifestore_products[0][0])

top = []
ji = []


i = 1 #columna que queremos obtener
columna = [fila[i] for fila in lifestore_searches]

for x in range(len(lifestore_products)+1):
  l = columna.count(x)
  top.append(l)
  print(str(x) + "  " + str(top[x]))

a = np.array(top)
print(a)
print("'l'")
print(len(a))

indices = np.sort(a)[::-1]
print(indices)
suma = np.sum(indices)
print(suma)

indices1 = np.argsort(a)[::-1]
print(indices1)
print(len(indices1))

columna3 = indices1[0:10]

print("--")
for i in range(len(lifestore_products)):
  for x in range(len(columna3)):
    if lifestore_products[i][0] == columna3[x]: 
      print(lifestore_products[i][0:2]) 
       