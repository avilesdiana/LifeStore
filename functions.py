
from datetime import date, time, datetime #para usar las fechas
import os #Clase para limpiar pantalla
import time #Clase para pausar tiempo en la consola
import getpass #Clase para que la contraseña no aparezca en consola
import numpy as np
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches



#Función para limpiar pantalla
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  #Si el programa corre en Windows, use cls
        command = 'cls'
    os.system(command)

#Función para mostrar mensaje: Presionar Enter y contniuar
def enter():
  input('\n[Presiona ENTER para continuar] ')

#Función para mostrar mensje Bienvenida
def welcome_System():
  print('\n-------------------------------\nBienvenido a LIFESTORE\n-------------------------------')
  print('Análisis de la rotación de productos por \nIng.Diana Aviles\n-------------------------------\n')
  print('\nIngresa tus credenciales de administrador para acceder a los reportes\n')

#Función para mostrar el menú principal 
def main_menu():
  print('\n-------------------------------\nMENU LIFESTORE\n-------------------------------')
  print('\nSeleccione una opción\n')
  print('\n1. Productos más vendidos y productos rezagados')
  print('\n2. Productos por reseña en el servicio')
  print('\n3. Total de ingresos anual,número de ventas\n  y top 3 de meses con más ventas en el año')
  print('\n4.Cerrar sesión\n')
  print('-------------------------------\n')
  choiceOfMainMenu = input('\nNúmero de elección: ')
  return choiceOfMainMenu #Regresa la elección para su validación en el programa principal

#Función para mostrar el cerrado de sesión
def log_Out():
  clearConsole()
  print('\n-------------------------------------\nCerrando sesión de LIFESTORE ....')
  print('-------------------------------------\n')
  time.sleep(1)
  clearConsole()
  print('\n-----------------------------------\nCerrando sesión de LIFESTORE ...')
  print('-----------------------------------\n')
  time.sleep(1)
  clearConsole()
  print('\n---------------------------------\nCerrando sesión de LIFESTORE ..')
  print('---------------------------------\n')
  time.sleep(1)
  clearConsole()
  print('\n-------------------------------\nCerrando sesión de LIFESTORE .')
  print('-------------------------------\n')
  time.sleep(1)
  clearConsole()

#Función para mostrar que ingreso un valor erróneo 
def wrong_Value(optionText):
  print('\n-------------------------------')
  print('\n    Opción INCORRECTA')
  print('\nIngrese un valor de '+ optionText+' válido')
  print('\n-------------------------------\n')

#Función para mostrar el inicio de sesión
def log_In():
  clearConsole()
  print('\n-------------------------------\nIniciando sesión de LIFESTORE .')
  print('-------------------------------\n')
  time.sleep(1)
  clearConsole()
  print('\n---------------------------------\nIniciando sesión de LIFESTORE ..')
  print('---------------------------------\n')
  time.sleep(1)
  clearConsole()
  print('\n-----------------------------------\nIniciando sesión de LIFESTORE ...')
  print('-----------------------------------\n')
  time.sleep(1)
  clearConsole()
  print('\n-------------------------------------\nIniciando sesión de LIFESTORE ....')
  print('-------------------------------------\n')
  time.sleep(1)
  clearConsole()

#Función para obtener el top de 5 productos más vendidos
def top5_mostSelledProducts():

  validation_refund = []
  count_products = []
  order_list5 = []
  
  #Agregamos en una nueva lista los productos de ventas que no tuvieron reembolso == 0 
  for sale0 in range(len(lifestore_sales)):
    if lifestore_sales[sale0][4] == 0:
      validation_refund.append(lifestore_sales[sale0])
      #Comprobamos que imprima los correctos
      #print(lifestore_sales[sale0]) 
  
  #Obtener la validation_refaund[1] para guadarla en una lista donde vienen todos los productos que se vendieron
  i = 1 #columna que queremos obtener
  column_products = [fila[i] for fila in validation_refund]  
  
  for products in range(len(lifestore_products)+1):
    element = column_products.count(products)
    count_products.append(element)
   #Comprobamos que imprima los correctos
   #print(str(products) + "  " + str(count_products[products]))
  
  #Convertir en un arreglo para ordenar la lista
  array_countProducts = np.array(count_products)
  #print(array_countProducts)
  
  #Comprobamos que se ordenen
  #commanded_frequency = np.sort(array_countProducts)[::-1]
  #print(commanded_frequency)
  
  #Ordenamos por id_producto
  idProduct_order = np.argsort(array_countProducts)[::-1]
  #print(idProduct_order)

  #Guardamos en un arreglo los primeros 5
  array_idProduct = idProduct_order[0:5]

  #Buscamos el id en el arreglo lifestore_products para imprimir el top 5
  for column in range(len(lifestore_products)):
   for row in range(len(array_idProduct)):
     if lifestore_products[column][0] == array_idProduct[row]: 
       order_list5.append(lifestore_products[column][0:2])
  
  return order_list5


#Función para obtener el top de 10 productos más buscados
def top10_mostWantedProducts():

  count_products = []
  order_list10 = []
  
  
  #Obtener la validation_refaund[1] para guadarla en una lista donde vienen todos los productos que se vendieron
  i = 1 #columna que queremos obtener
  column_products = [fila[i] for fila in lifestore_searches]  
  
  for products in range(len(lifestore_products)+1):
    element = column_products.count(products)
    count_products.append(element)
   #Comprobamos que imprima los correctos
   #print(str(products) + "  " + str(count_products[products]))
  
  #Convertir en un arreglo para ordenar la lista
  array_countProducts = np.array(count_products)
  #print(array_countProducts)
  
  #Comprobamos que se ordenen
  #commanded_frequency = np.sort(array_countProducts)[::-1]
  #print(commanded_frequency)
  
  #Ordenamos por id_producto
  idProduct_order = np.argsort(array_countProducts)[::-1]
  #print(idProduct_order)

  #Guardamos en un arreglo los primeros 5
  array_idProduct = idProduct_order[0:10]

  #Buscamos el id en el arreglo lifestore_products para imprimir el top 5
  for column in range(len(lifestore_products)):
   for row in range(len(array_idProduct)):
     if lifestore_products[column][0] == array_idProduct[row]: 
       order_list10.append(lifestore_products[column][0:2])
  
  return order_list10

#Función para obtener el top de 10 productos menos buscados
def top10_leastWantedProducts():

  count_products = []
  order_list10 = []
  
  
  #Obtener la validation_refaund[1] para guadarla en una lista donde vienen todos los productos que se vendieron
  i = 1 #columna que queremos obtener
  column_products = [fila[i] for fila in lifestore_searches]  
  
  for products in range(len(lifestore_products)+1):
    element = column_products.count(products)
    count_products.append(element)
   #Comprobamos que imprima los correctos
    #print(str(products) + "  " + str(count_products[products]))
  
  #Convertir en un arreglo para ordenar la lista
  array_countProducts = np.array(count_products)
  
  #print(array_countProducts)
  
  #Comprobamos que se ordenen
  #commanded_frequency = np.sort(array_countProducts)[::-1]
  #print(commanded_frequency)
  
  #Ordenamos por id_producto
  idProduct_order = np.argsort(array_countProducts)
  #print(idProduct_order)

  #Guardamos en un arreglo los primeros 10
  array_idProduct = idProduct_order[0:11]

  #Buscamos el id en el arreglo lifestore_products para imprimir el top 5
  for column in range(len(lifestore_products)):
   for row in range(len(array_idProduct)):
     if lifestore_products[column][0] == array_idProduct[row]: 
       order_list10.append(lifestore_products[column][0:2])
  
  return order_list10

#Función para unir listas
def merge(list1, list2): 
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
    return merged_list 

#Función para obtener el top de 5 productos más vendidos
def existingCategories():
  categories = []
  product_categories = []
  count_products = []
  validation_refund = []
  idProducto_SalesXProduct = []
  frecuency_categorie = []
  totalSalesByCategory = []

  #Guardamos en un arreglo las categorias existentes
  for product in range(len(lifestore_products)):
   if lifestore_products[product][3] not in categories:
     categories.append(lifestore_products[product][3])
  
  #Guardamos en una lista cada categoria de los productos en la lista de lifestore_productos
  for column in range(len(lifestore_products)):
   for row in range(len(categories)):
    if lifestore_products[column][3] == categories[row]: 
      product_categories.append(lifestore_products[column][3])
  
  #Creamos una lista que imprima del 1 hasta la longitud de número de productos que hay : 96
  for x in range(len(lifestore_products)+1):
   if x != 0:
     count_products.append(x)
  
  #Unión de listas de Id_producto y las categorías
  idProducto_category = merge(count_products, product_categories)

  #Agregamos en una nueva lista los productos de ventas que no tuvieron reembolso == 0 
  for sale0 in range(len(lifestore_sales)):
    if lifestore_sales[sale0][4] == 0:
       validation_refund.append(lifestore_sales[sale0])
  
  #Creamos una lista para unir los id productos de lifestore_sales con la nueva lista que contiene los id_producto y su categoria
  for x in range(len(validation_refund)):
    for j in range(len(idProducto_category)):
      if lifestore_sales[x][1] == idProducto_category[j][0]:
        idProducto_SalesXProduct.append(idProducto_category[j][1])

  #contamos las frecuencias de venta por cada categoria
  for product in idProducto_SalesXProduct:
    frecuency_categorie.append(idProducto_SalesXProduct.count(product))
  
  #Creamos una nueva lista para unir las frecuencias por categoría y su categoría
  salesByCategory = merge(frecuency_categorie,idProducto_SalesXProduct)

  #Ordenamos el número de ventas por categoria de menor a mayor
  leastSoldCategories = sorted(salesByCategory, key=lambda categorie : categorie[0])
  
  for element in leastSoldCategories:
    if element not in totalSalesByCategory:
      totalSalesByCategory.append(element)
  
  return categories, totalSalesByCategory



#Función para obtener el top de reviews
def top_Reviews(option):

  validation_refund = []
  resultantList = []
  product_top5 = []


  #Extraer la columna 0 y 1  de lifestore_products que corresponde al id_product y name para guardarlos en una lista y comparar después de filtrar 

  i = 0 #columna que queremos obtener
  column_idProduct = [fila[i] for fila in lifestore_products]
  
  i = 1 #columna que queremos obtener
  column_nameProduct = [fila[i] for fila in lifestore_products]
  
  productos_id_name = merge(column_idProduct ,column_nameProduct)
  
  #Agregamos en una nueva lista solamento los productos que tienen reseña, quitamos de la lista todos los productos vendidos que tengan scrore < 1

  for sale0 in range(len(lifestore_sales)):
   if lifestore_sales[sale0][2] >= 1:
    validation_refund.append(lifestore_sales[sale0])

  
  #Extraer la columna 1 y 2  de lifestore_sales que corresponde al id_product y score para guardarlos en una lista y comparar después de filtrar 

  i = 1 #columna que queremos obtener
  column_idProductSales = [fila[i] for fila in lifestore_sales]
  
  i = 2 #columna que queremos obtener
  column_scoreProduct = [fila[i] for fila in lifestore_sales]
  
  productos_id_score = merge(column_idProductSales, column_scoreProduct)

  #Ordenamos el Score
  ordenados = sorted(productos_id_score, key=lambda score : score[1], reverse = option)

  
 #Limpiamos los id_products y score repetidos.
  for element in ordenados:
    if element not in resultantList:
        resultantList.append(element)


  #Extraemos la columna con el Id_product de la nueva lista
  i = 0 #columna que queremos obtener
  column_idProductNew = [fila[i] for fila in resultantList] 
  #Guardar solamente los primeros 5
  top5 = column_idProductNew [0:5]
  

  #Buscamos el id producto de la nueva lista, con la creada al principio con el filtrado de Lifestore_sales
  for column in range(len(productos_id_name)):
    for row in range(len(top5)):
      if productos_id_name[column][0] == top5[row]: 
         product_top5.append(productos_id_name[column][0:2])

  return product_top5, resultantList
  

#Función para obtener el ventas totales, ventas totales sin reembolsos, total vendido, y el top 3 de meses con más ventas
def sales():

  validation_refund = []
  sales_total = []
  freq_month = []
  months_sales = []
  months_top3 = []
  column_dateSale = []
  column_month = []

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