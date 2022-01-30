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
  input('\n[Presiona Enter para continuar] ')

#Función para mostrar mensje Bienvenida
def welcome_System():
  print('\nBienvenido a LIFESTORE')
  print('\nIngresa tus credenciales de administrador para acceder a los reportes\n')

#Función para mostrar el menú principal 
def main_menu():
  print('\nMENU LIFESTORE\n-------------------------------')
  print('\nSeleccione una opción\n')
  print('\n1.Productos más vendidos y productos rezagados')
  print('\n2.Productos por reseña en el servicio')
  print('\n3.Total de ingresos y ventas promedio mensuales,\ntotal anual y meses con meses con más ventas en el año')
  print('\n4.Cerrar sesión\n')
  choiceOfMainMenu = input('\nNúmero de elección: ')
  return choiceOfMainMenu #Regresa la elección para su validación en el programa principal

#Función para mostrar el cerrado de sesión
def log_Out():
  clearConsole()
  print('Cerrando sesión de LIFESTORE .')
  time.sleep(1)
  clearConsole()
  print('Cerrando sesión de LIFESTORE ..')
  time.sleep(1)
  clearConsole()
  print('Cerrando sesión de LIFESTORE ...')
  time.sleep(1)
  clearConsole()
  print('Cerrando sesión de LIFESTORE ....')
  time.sleep(1)
  clearConsole()

#Función para mostrar que ingreso un valor erróneo 
def wrong_Value(optionText):
  print('\n    Opción INCORRECTA')
  print('\nIngrese un valor de '+ optionText+' válido')

#Función para mostrar el inicio de sesión
def log_In():
  clearConsole()
  print('Iniciando sesión de LIFESTORE .')
  time.sleep(1)
  clearConsole()
  print('Iniciando sesión de LIFESTORE ..')
  time.sleep(1)
  clearConsole()
  print('Iniciando sesión de LIFESTORE ...')
  time.sleep(1)
  clearConsole()
  print('Iniciando sesión de LIFESTORE ....')
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

  #Guardamos en un arreglo los primeros 5
  array_idProduct = idProduct_order[0:10]

  #Buscamos el id en el arreglo lifestore_products para imprimir el top 5
  for column in range(len(lifestore_products)):
   for row in range(len(array_idProduct)):
     if lifestore_products[column][0] == array_idProduct[row]: 
       order_list10.append(lifestore_products[column][0:2])
  
  return order_list10
  