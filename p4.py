"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

import numpy as np

from operator import itemgetter, attrgetter

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

result = []
list10 = []
list1 = []
f= []
count_products = []
l = []
validation_refund = []
count_products2 = []
new = []
new2 = []


#Imprimir todas las catergorías existentes
for item in range(len(lifestore_products)):
  if lifestore_products[item][3] not in result:
    result.append(lifestore_products[item][3])

print(result)

for column in range(len(lifestore_products)):
  for row in range(len(result)):
    if lifestore_products[column][3] == result[row]: 
      list10.append(lifestore_products[column][3])
     

print("list10")
print(len(list10))
for c in list10:
  print(c)


"""
print(len(list10))
print(type(list10))
print(list10[3])
"""

for x in range(len(lifestore_products)+1):
  if x != 0:
   count_products.append(x)

print("conunt_priductos")
for c in count_products:
  print(c)

#print(len(list10))
#print(len(count_products))

a = np.array(count_products)
#print(len(a))
b = np.array(list10)
#print(len(b))

""""
for i in range(len(a)):
  for x in range(len(b)):
    list1 = np.append(a[i],b[x])

"""

def merge(list1, list2): 
      
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
    return merged_list 
      

def merge2(list1, list2,list3): 
      
    merged_list = [(list1[i], list2[i], list3[i]) for i in range(0, len(list1))] 
    return merged_list 


f = merge(count_products, list10)
g = np.array(f)
#print(f) 
#print(len(f))

""""
print(f[0][0])
print(f[1][0]) 
print(lifestore_sales[0][1])

print(g) 
"""

#print(len(g))

 #Agregamos en una nueva lista los productos de ventas que no tuvieron reembolso == 0 
for sale0 in range(len(lifestore_sales)):
 if lifestore_sales[sale0][4] == 0:
   validation_refund.append(lifestore_sales[sale0])
      #Comprobamos que imprima los correctos

#print("aqui")
#for o in validation_refund:
#print(o)      #print(lifestore_sales[sale0]) 


for c in range(len(validation_refund)):
  for j in range(len(f)):
    if lifestore_sales[c][1] == f[j][0]:
     l.append(f[j][1])
      

#print(len(l))
#print(type(l))

###print("aqui 2")
#for o in l:
 #print(o)

frecuenciaPalab = []

for w in l:
    frecuenciaPalab.append(l.count(w))

print(frecuenciaPalab)



new = merge(frecuenciaPalab,l)

print("aqui 0000")

for j in new:
 print(j)




ordenados = sorted(new, key=lambda coche : coche[0])

print("conteo vendidos ! categoria !")
for s in ordenados:
 print(s)

print(type(ordenados))




resultantList = []
 
for element in ordenados:
    if element not in resultantList:
        resultantList.append(element)
        
print('aqui 3')

for s in resultantList:
 print(s)

#p = merge(resultantList,)

""""
array_countProducts = np.array(resultantList)
print('o')
print(array_countProducts)
"""

""""
resultantList1 = []
for element in frecuenciaPalab:
    if element not in resultantList1:
        resultantList1.append(element)

print(resultantList1)"""
