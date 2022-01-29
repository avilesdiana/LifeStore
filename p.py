import numpy as np
import collections
import copy 
from operator import itemgetter, attrgetter

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
#print(lifestore_searches[0])

#print(lifestore_products[0][0])

top = []
top1 = []
arrayto= []

new_lists = sorted(lifestore_sales, key=itemgetter(2), reverse = True)
print(len(new_lists))


i = 1 #columna que queremos obtener
columna = [fila[i] for fila in new_lists]
print(columna)
print(len(columna))
#columna1 = columna.sort()

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

print(indices1[0:5])

columna3 = indices1[0:5]

for i in range(len(lifestore_products)):
  for x in range(len(columna3)):
    if lifestore_products[i][0] == columna3[x]: 
      print(lifestore_products[i][0:2]) 
  