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

#new_lists = sorted(lifestore_sales, key=itemgetter(2), reverse = True)
#print(len(new_lists))
print(type(lifestore_sales))

for w in range(len(lifestore_sales)):
  if lifestore_sales[w][4] == 0:
    print(lifestore_sales[w])
    ji.append(lifestore_sales[w])


#print(len(ji))
#print(ji)

i = 1 #columna que queremos obtener
columna = [fila[i] for fila in ji]

#for x in columna:
 # print(x)

for x in range(len(lifestore_products)+1):
  l = columna.count(x)
  top.append(l)
  print(str(x) + "  " + str(top[x]))

a = np.array(top)
print(a)

indices = np.sort(a)[::-1]
print(indices)

indices1 = np.argsort(a)[::-1]
print(indices1)

columna3 = indices1[0:5]

print("--")
for i in range(len(lifestore_products)):
  for x in range(len(columna3)):
    if lifestore_products[i][0] == columna3[x]: 
      print(lifestore_products[i][0:2]) 
       