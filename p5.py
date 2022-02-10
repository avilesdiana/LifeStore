"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

import numpy as np

from operator import itemgetter, attrgetter

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches


from datetime import date, time, datetime

f = []

"""
f = datetime.strptime('15/4/2020', '%d/%m/%Y')
print(f.month)
"""

"""
print(lifestore_sales[0][3])
print(lifestore_sales[1][3])


for l in range(len(lifestore_sales)):
  f.append(datetime.strptime(lifestore_sales[l][3], '%d/%m/%Y'))


for h in range(len(f)):
  print(f[h].month)

"""

def ventas():

  validation_refund = []

  #Agregamos en una nueva lista los productos de ventas que no tuvieron reembolso == 0 
  for sale0 in range(len(lifestore_sales)):
    if lifestore_sales[sale0][4] == 0:
       validation_refund.append(lifestore_sales[sale0])
  
  #Ventas totales registradas
  sales_Total_refund = len(validation_refund)



  return sales_Total_refund

#####

sales_total = ventas()

print("\nVentas totales: ")
print(len(lifestore_sales))

print("\nVentas totales sin reembolsos: ")
print(sales_total)