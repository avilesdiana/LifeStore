import os #Clase para limpiar pantalla
import getpass #Clase para que la contraseña no aparezca en consola
import time #Clase para pausar tiempo en la consola

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

#Inicializando el contador para la evaluación
validation_Count = 0
validation_Menu = 0
session_error = 3

#Login
user_Login = 'admin'
password_Login = '1234'

#Estructura del programa
#Mientras el contador == 0, repetira la acción hasta que ingrese el valor correcto
while validation_Count == 0 and session_error != 0:
  #Mensaje de bienvenida
  clearConsole()
  welcome_System() 
  user_Access = input('USUARIO: ')

  if user_Access == user_Login:
    #getpass es para que no aparezca la contraseña en la consola
    password_Access = getpass.getpass('CONTRASEÑA: ')

    if password_Access == password_Login:
      clearConsole() #Limpiar consola
      #Al ser diferente de 0 sale del ciclo while
      validation_Count += 1
      log_In()
      clearConsole()
      
      #validación del menú, mientras el contador == 0 lo seguirá repitiendo
      while validation_Menu == 0:
        choiceMainMenu = int(main_menu())
      
        if choiceMainMenu == 1:
          clearConsole()
          print('Elección 1')
          enter()
          validation_Menu += 1

        elif choiceMainMenu == 2:
          clearConsole()
          print('Elección 2')
          enter()
          validation_Menu += 1
      
        elif choiceMainMenu == 3:
          clearConsole()
          print('Elección 3')
          enter()
          continue
          validation_Menu += 1
        
        elif choiceMainMenu == 4:
          #función para cerrar sesión
          log_Out()
          validation_Menu += 1
        
        else:
         #Ingreso una valor erróneo en el menú
         clearConsole()
         wrong_Value('menú')
         enter()
         clearConsole() 

    #else contraseña
    else:
      #Ingreso una contraseña errónea
      clearConsole()
      wrong_Value('contraseña')
      enter()
      clearConsole()
      session_error -=1
      print("PASASTE LAS 3 VECES,\nContacta a tu gerente para revisar tus credenciales\n")
      

  #else usuario   
  else:
    #Ingreso un Usuario erróneo
    clearConsole()
    wrong_Value('usuario')
    enter()
    clearConsole()
    session_error -=1
    print("PASASTE LAS 3 VECES,\nContacta a tu gerente para revisar tus credenciales\n")
    

    