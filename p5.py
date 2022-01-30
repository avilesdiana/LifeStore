"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

import numpy as np

from operator import itemgetter, attrgetter

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches


validation_refund = []

 #Agregamos en una nueva lista los productos de ventas que no tuvieron reembolso == 0 
for sale0 in range(len(lifestore_sales)):
 if lifestore_sales[sale0][4] == 0:
   validation_refund.append(lifestore_sales[sale0])
   #print(lifestore_sales[sale0]) 

for x in validation_refund:
  print(x)

