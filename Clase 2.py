#Condicionales
"""
 == Igualdad
 != Diferencia
 > mayor
 < menor
 >= mayor o igual
 <= menor o igual
 

 
nombre = input("Digite su nombre: ")

if ("gen"==nombre): # True o False
    print("El nombre es igual")
else:
    print("El nombre no es igual")
    

#Escribir un programa al usuario su edad y muestre si es mayor de edad o no

edad=int(input("Digite su edad: "))

if edad>=18:
    print("Sí es mayor de edad")
else:
    print("No es mayor de edad")
    


#Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario introduce un 0
#Debemos mostrar que existe un error, división 0 no es posible.

num1=float(input("Digite el primer número: "))
num2=float(input("Digite el segundo número: "))

if(num1 !=0 and num2 !=0):
    division = num1/num2
    print("El resultado de la división es:",division)
else:
    print("ERROR: división entre 0 no es posible")
    


num= int(input("Digite un número: "))
if num % 2==0:
    print("El número es par")
else:
    print("El número es impar")
    

#Para tributar un determinado impuesto se debe ser mayor de 18 años
#Además tener 500000 colones mensuales
#Escribir un programa qye pregunte su edad y sus ingresos mensuales y muestre en pantalla si este usuario tributa o no impuestos

edad=int(input("Digite su edad: "))
num=float(input("Digite sus ingresos mensuales: "))

if edad>=18 and num>=500000:
    print("Sí tributa impuestos")
else:
    print("No tributa impuestos")
    
"""
#Escribir un programa para una sala de video juegos, si los usuarios tienes 10 o menos de 10 años pagaran 3000 colones
#Si el usuario tiene menos de 15 años pagará 15000 colones y el usuario tiene menos de 19 años va a pagar 7500 colones
#Y si es mayor paga 10000

edad=int(input("Digite su edad: "))
if edad<=10:
    precio=3000
elif edad<=15 and edad>10:
    precio=5000
elif edad<=18 and edad>15:
    precio=7500
else: edad>18
precio=10000
print ("La cantidad a pagar es de: ", precio)

#arreglar

