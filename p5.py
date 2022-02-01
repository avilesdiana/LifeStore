"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

import numpy as np

from operator import itemgetter, attrgetter

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches


def merge(list1, list2): 
      
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
    return merged_list 
      

validation_refund = []

 ### lista productos

i = 1 #columna que queremos obtener
column_products1 = [fila[i] for fila in lifestore_products] 

for x in column_products1:
  print(x)

i = 0 #columna que queremos obtener
column_products0 = [fila[i] for fila in lifestore_products] 

for x in column_products0:
  print(x)

productos_id_name = merge(column_products0 ,column_products1)

for x in productos_id_name :
  print(x)

  ########

  #Agregamos en una nueva lista solamento los productos que tienen reseña
for sale0 in range(len(lifestore_sales)):
 if lifestore_sales[sale0][2] >= 1:
   validation_refund.append(lifestore_sales[sale0])

for x in validation_refund:
  print(x)

print(len(validation_refund))
print(len(lifestore_sales))

i = 1 #columna que queremos obtener
column_sales0 = [fila[i] for fila in lifestore_sales] 

for x in column_sales0:
  print(x)

i = 2 #columna que queremos obtener
column_sales1 = [fila[i] for fila in lifestore_sales] 

for x in column_sales1:
  print(x)


sales_id_name = merge(column_sales0 ,column_sales1)

for x in sales_id_name :
  print(x)


ordenados = sorted(sales_id_name, key=lambda score : score[1], reverse = True)

print("ordenados")
for x in ordenados:
  print(x)

resultantList = []
 
for element in ordenados:
    if element not in resultantList:
        resultantList.append(element)


print("PRODUCTOS FINALES")
for x in resultantList:
  print(x)




print("prubeas")
print(resultantList[0][0])
print(productos_id_name[0][0])

product_categories20 = []

i = 0 #columna que queremos obtener
column_sales11 = [fila[i] for fila in resultantList] 
column_sale12 = column_sales11[0:5]
print("column_sales11")
for x in column_sale12:
  print(x)

print("fin")


for column in range(len(productos_id_name)):
  for row in range(len(column_sale12 )):
   if productos_id_name[column][0] == column_sale12[row]: 
    product_categories20.append(productos_id_name[column][0:2])

print("idProducto_SalesXProduct")
for x in product_categories20:
  print(x)


  