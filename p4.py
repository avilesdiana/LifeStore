"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

import numpy as np

from operator import itemgetter, attrgetter

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

result = []
list10 = []
list1 = []
count_products = []
#print(lifestore_searches[0])

#Imprimir todas las catergorías existentes
for item in range(len(lifestore_products)):
  if lifestore_products[item][3] not in result:
    result.append(lifestore_products[item][3])

print(result)

for column in range(len(lifestore_products)):
  for row in range(len(result)):
    if lifestore_products[column][3] == result[row]: 
      list10.append(lifestore_products[column][0:4])
     


for c in list10:
  print(c)


print(len(list10))
print(type(list10))
print(list10[0][3])


