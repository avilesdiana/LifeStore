import functions 


#Librería para mandar a llamar la información de Lifestore
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
#print(lifestore_searches[0])


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
  functions.clearConsole()
  functions.welcome_System() 
  user_Access = input('USUARIO: ')

  if user_Access == user_Login:
    #getpass es para que no aparezca la contraseña en la consola
    password_Access = functions.getpass.getpass('CONTRASEÑA: ')

    if password_Access == password_Login:
      functions.clearConsole() #Limpiar consola
      #Al ser diferente de 0 sale del ciclo while
      validation_Count += 1
      functions.log_In()
      functions.clearConsole()
      
      #validación del menú, mientras el contador == 0 lo seguirá repitiendo
      while validation_Menu == 0:
        choiceMainMenu = int(functions.main_menu())
      
        if choiceMainMenu == 1:
          functions.clearConsole()
          print('\nTop 5 más vendidos\n-------------------------------')
          top5 = functions.top5_mostSelledProducts()
          print('\nid - Component\n')
          for list in top5:
            print(list)
            print(" ")
          
          print('\nTop 10 más buscado\n-------------------------------')
          top10_more = functions.top10_mostWantedProducts()
          print('\nid - Component\n')
          for list in top10_more:
            print(list)
            print(" ")

          print('\nTop 10 menos buscado\n-------------------------------')
          top10_less = functions.top10_leastWantedProducts()
          print('\nid - Component\n')
          for list in top10_less:
            print(list)
            print(" ")
          
          print('\nCategorías menos vendidas\n-------------------------------')
          print('\nCategorías existentes: \n')
          categories,count_products= functions.existingCategories()
          print(categories)
          print('\n_____________')
          print('\nVendidos - Categoria\n')
          for list in count_products:
            print(list)
            print(" ")


          functions.enter()
          functions.clearConsole()
          continue
          validation_Menu += 1

        elif choiceMainMenu == 2:
          functions.clearConsole()
          print('Elección 2')
          functions.enter()
          functions.clearConsole()
          continue
          validation_Menu += 1
      
        elif choiceMainMenu == 3:
          functions.clearConsole()
          print('Elección 3')
          functions.enter()
          functions.clearConsole()
          continue
          validation_Menu += 1
        
        elif choiceMainMenu == 4:
          #función para cerrar sesión
          functions.log_Out()
          validation_Menu += 1
        
        else:
         #Ingreso una valor erróneo en el menú
         functions.clearConsole()
         functions.wrong_Value('menú')
         functions.enter()
         functions.clearConsole() 

    #else contraseña
    else:
      #Ingreso una contraseña errónea
      functions.clearConsole()
      functions.wrong_Value('contraseña')
      functions.enter()
      functions.clearConsole()
      session_error -=1
      print("PASASTE LAS 3 VECES,\nContacta a tu gerente para revisar tus credenciales\n")
      

  #else usuario   
  else:
    #Ingreso un Usuario erróneo
    functions.clearConsole()
    functions.wrong_Value('usuario')
    functions.enter()
    functions.clearConsole()
    session_error -=1
    print("PASASTE LAS 3 VECES,\nContacta a tu gerente para revisar tus credenciales\n")
    

    