import os #Clase para limpiar pantalla
import time #Clase para pausar tiempo en la consola
import getpass #Clase para que la contraseña no aparezca en consola

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