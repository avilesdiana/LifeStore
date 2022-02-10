"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

import numpy as np

from operator import itemgetter, attrgetter

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#esta si 
from datetime import date, time, datetime

column_dateSale = []
column_month = []

#Función para unir listas
def merge(list1, list2): 
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
    return merged_list 



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

ordenados = sorted(idProduct_date, key=lambda mes : mes[1])


#Ordenar
  ordenados = sorted(count_freq, key=lambda mes : mes[0])

"""

def sales():

  validation_refund = []
  sales_total = []
  freq_month = []
  months_sales = []
  months_top3 = []

  #Agregamos en una nueva lista los productos de ventas que no tuvieron reembolso == 0 
  for sale0 in range(len(lifestore_sales)):
    if lifestore_sales[sale0][4] == 0:
       validation_refund.append(lifestore_sales[sale0])
  
  #Ventas totales registradas
  sales_Total_refund = len(validation_refund)


  #Convertimos la fecha a tipo datatime para extraerla
  for dateSale in range(len(validation_refund)):
    column_dateSale.append(datetime.strptime(validation_refund[dateSale][3], '%d/%m/%Y'))
    column_month.append(column_dateSale[dateSale].month)

  #Extraemos la el id producto de la nueva lista limpia
  i = 1 #columna que queremos obtener
  column_idProductSales = [fila[i] for fila in validation_refund]

  #Id_product Unión con el Mes de Venta
  idProduct_date = merge(column_idProductSales,column_month)

  #Extraemos la el id producto y el precio  de lifestore_products 
  i = 0 #columna que queremos obtener
  column_idProductP = [fila[i] for fila in lifestore_products]

  i = 2 #columna que queremos obtener
  column_priceP = [fila[i] for fila in lifestore_products]

  #Id_product Unión con el Precio del producto
  idProduct_Price = merge(column_idProductP,column_priceP)

  #Buscamos id_Product de sales con el Id_product de productos para hacer la suma de precios y calcular la venta
  for column in range(len(idProduct_Price)):
    for row in range(len(idProduct_date)):
      if idProduct_Price[column][0] == idProduct_date[row][0]: 
         sales_total.append(idProduct_Price[column][1])

  #Imprimir la suma total vendida con la unión 
  salesTotal = sum(sales_total)
  
  #Ordenar por Mes empezando por Enero
  ordenados = sorted(column_month, key=lambda mes : mes)
  
  #Eliminar los meses repetidos
  for product in range(len(column_month)):
   if column_month[product] not in months_sales:
     months_sales.append(column_month[product])


  #Ocurrencia de los meses donde más se compraron productos
  for products in ordenados:
    element = ordenados.count(products)
    freq_month.append(element)
  
  #Mes Unión con frecuencia de venta
  month_freq = merge(ordenados,freq_month)

  #Ordenar por ocurrencia - (mes, ocurrencia)
  ordenados_freq = sorted( month_freq, key=lambda freq : freq[1], reverse = True)
  
  #Eliminar las ocurrencias con su mes repetidas
  for product in range(len(ordenados_freq)):
   if ordenados_freq[product] not in months_top3:
     months_top3.append(ordenados_freq[product])

  
  return sales_Total_refund, salesTotal,  months_top3[0:3]
#####

sales_total, products_sale, freq_month = ventas()

print("\nVentas totales: ")
print(len(lifestore_sales))

print("\nVentas totales sin reembolsos: ")
print(sales_total)

print("\nTotal vendido en el 2020 sin reembolso:")
print("$" + str(products_sale))

print("\nTop 3 de meses con más ventas en el año: ")
print("\nMES - Artículos vendidos")
print(freq_month)