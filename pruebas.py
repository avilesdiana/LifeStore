"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""


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

new_lists = sorted(lifestore_sales, key=itemgetter(1), reverse = True)
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

for k in range(len(lifestore_products)+1):
  top1.append(k)

print(top1)
print(type(top1))


array3 = np.array(top1)
array4 = np.array(top)
print(array3)
print(array4)


arrayto = np.append(array3,array4,axis=1)

print(arrayto)
""""
new_list2 = sorted(top, reverse = True)
print(new_list2)
print(type(new_list2))
"""
#lista_ordenada = sorted(l, key=itemgetter(2))


"""
new_lists = sorted(lifestore_sales, key=itemgetter(2), reverse = True)

print(len(new_lists))

for lists in new_lists[0:50]:
  print(lists)

for x in range(len(lifestore_products[i])):

for i in range(len(lifestore_products)):
  if lifestore_products[i][0] == 2:
    print(lifestore_products[i][0:2]) 
  

---
i = 1 #columna que queremos obtener
columna = [fila[i] for fila in new_lists]
print(columna)
print(len(columna))

columna1 = set(columna)
columna2 = list(columna1)
columna3 = columna2[:5]

print(columna3)
---



  

more_sales = int(lifestore_sales)
top_sales = more_sales.sort()

for top in top_sales:
 print(top)

#for sale in lifestore_sales[0:50]:
 # print(sale)



l1 = [[1, 2, 3, 4, 5,4],  [7,7,7,7,7,7],  [8, 8, 8, 8, 8,8]]
l2 = [[9, 2, 7, 6, 5,4], [9, 9, 9, 9, 9,9], [6, 6, 6, 6, 6,6]]
    
#if l1[1] == l2[1]:
 # print(str(l1[1]) + " " + str(l2[1]))

for l in l1[[1]:
  print(l)
  
"""

'''
new_lists = sorted(lifestore_sales, key=itemgetter(2), reverse = True)

print(len(new_lists))

for i in range(0,50):
  print(new_lists[i])

nl= []

i = 1 #columna que queremos obtener
columna = [fila[i] for fila in new_lists[0:50]]
print(columna)
print(len(columna))
print(len(lifestore_products))

print(set(columna))

#
'''



''''
for i in range(len(lifestore_products)):
  for x in range(len(columna3)):
    if lifestore_products[i][0] == columna3[x]: 
      print(lifestore_products[i][0:2]) 
  

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
top_diez = []

for x in range(10):  # Número de veces que ejecutamos este bucle
    maximo = max(lista)  # Buscamos el máximo valor
    top_diez.append(maximo)  # Lo añadimos a una nueva lista
    top = lista.remove(maximo)  # Lo eliminamos de la lista antigua, para que el próximo "máximo valor" no incluya este valor

top_diez.sort()  # Ordenamos la lista
print(lista)
print(top_diez)

for h in columna:
  print(h)
#print(columna)
#print(len(columna))




top.sort(reverse=True)  # Ordenarla de forma inversa
top5 = top[:5]  # Y capturar los 10 primeros elementos
print(top)
print(top5)
'''


"""

for x in range(len(lifestore_products)):
  l = columna.count(x)
  top.append(l)
  print(str(x) + "  " + str(top[x]))

"""