print("¡Adivina el número secreto!")
nombre = input("Digite su primer nombre: ")
apellido = input("Digite su primer apellido: ")
edad=int(input("Digite su edad: "))
num1 = 8 #Número secreto
num2 = int(input("Digite un número del 1 al 10: "))

if int(num1 == num2):
    print("¡Felicitaciones!",nombre,apellido,"Has acertado el número secreto.")
else:
    print("No has ganado pero agradecemos tu participación.")