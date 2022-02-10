#Importa las funciones que desarrolle en mi archivo functions.py
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
          print('\n-------------------------------\nTop 5 más vendidos\n-------------------------------')
          top5 = functions.top5_mostSelledProducts()
          print('\nid - Component\n')
          for list in top5:
            print(list)
            print(" ")
          
          print('\n-------------------------------\nTop 10 más buscado\n-------------------------------')
          top10_more = functions.top10_mostWantedProducts()
          print('\nid - Componente\n')
          for list in top10_more:
            print(list)
            print(" ")

          print('\n-------------------------------\nTop 10 menos buscado\n-------------------------------')
          top10_less = functions.top10_leastWantedProducts()
          print('\nid - Componente\n')
          for list in top10_less:
            print(list)
            print(" ")
          
          print('\n-------------------------------\nCategorías menos vendidas\n-------------------------------')
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
          print('\n-------------------------------\nProductos con mejores reseñas (5-3) \n-------------------------------')
          option = True
          top_reviews, listT = functions.top_Reviews(option)
          print('\nid - Componente\n')
          for list in top_reviews:
            print(list)
            print(" ")
          
          print('\n-------------------------------\nProductos con peores reseñas (1-3)\n-------------------------------')
          option = False
          top_Badreviews, listF= functions.top_Reviews(option)
          print('\nid - Componente\n')
          for list in top_Badreviews:
            print(list)
            print(" ")
          
          print('\n-------------------------------\nListado detallado de las mejores reseñas\n-------------------------------')
          print('\nid_producto - Score\n')
          for list in listT:
            print(list)
            print(" ")

          print('\n-------------------------------\nListado detallado de las peores reseñas\n-------------------------------')
          print('\nid_producto - Score\n')
          for list in listF:
            print(list)
            print(" ") 
          functions.enter()
          functions.clearConsole()
          continue
          validation_Menu += 1
      
        elif choiceMainMenu == 3:
          functions.clearConsole()
          sales_total, products_sale, freq_month = functions.sales()
          print('\n-------------------------------\nNúmero de Ventas Totales\n-------------------------------')
          print(str(len(lifestore_sales)) + " Productos")
          print('\n-------------------------------\nNúmero de Ventas Totales sin reembolsos\n-------------------------------')
          print(str(sales_total) + " Productos")
          print('\n-------------------------------\nTotal de ingresos en el 2020 sin reembolso\n-------------------------------')
          print("$" + str(products_sale) + " Pesos")
          print('\n-------------------------------\nTop 3 de meses con más ventas en el año\n-------------------------------')
          print('\nMes - Número de ventas\n')
          for list in freq_month:
            print(list)
            print(" ") 
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
      print("\n-------------------------------\nPASASTE LAS 3 VECES,\nContacta a tu gerente para revisar tus credenciales\n-------------------------------\n")
      

  #else usuario   
  else:
    #Ingreso un Usuario erróneo
    functions.clearConsole()
    functions.wrong_Value('usuario')
    functions.enter()
    functions.clearConsole()
    session_error -=1
    print("\n-------------------------------\nPASASTE LAS 3 VECES,\nContacta a tu gerente para revisar tus credenciales\n-------------------------------\n")
    

    
