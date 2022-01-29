"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

import numpy as np
import copy 
from operator import itemgetter, attrgetter

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
#print(lifestore_searches[0])

"""
new_lists = sorted(lifestore_sales, key=itemgetter(2), reverse = True)

print(len(new_lists))

for lists in new_lists[0:50]:
  print(lists)




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

new_lists = sorted(lifestore_sales, key=itemgetter(2), reverse = True)

print(len(new_lists))

nl= []

i = 1 #columna que queremos obtener
columna = [fila[i] for fila in new_lists[0:50]]
print(columna)
print(len(columna))

productos = np.array(columna)
result = np.where(productos == 5)

print(result)


