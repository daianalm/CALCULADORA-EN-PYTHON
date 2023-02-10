# Simple calculadora
#Crear las funciones que se encargan de dar formato a la lógica de la calculadora
def add(a,b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a,b):
    return a / b


print("Please, select your operation:")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Division")

while True:
    choice = input("Please, enter your choise(1| 2 | 3 | 4)")
    if choice in ('1', '2', '3', '4'):
        num1= float(input("Please, enter your FIRST number:"))
        num2= float(input("Please, enter your SECOND number: "))
        #Creamos la lógica de la calculadora
        if choice == '1':
            print(f"{num1} + {num2} = ", add(num1, num2))
        elif choice == '2':
            print(f"{num1} - {num2} = ", subtract(num1, num2))
        elif choice == '3':
            print(f"{num1} * {num2} = ", multiply(num1, num2))
        elif choice == '4':
            print(f"{num1} / {num2} = ", divide(num1, num2))
            #Sentencia break para detener la ejecución de un flujo dentro de nuestra aplicación. Utilizo para que una vez hecha la operación matemática, no siga preguntando por la siguiente operación  
            break


#En caso de que el usuario elija una operación matemática inválida entramos al 'else' e imprimimos un mensaje al usuario
    else:
        print("Your choice is not valid.")
        
keep_running = input("Would you like to continue? Yes or No?")
if keep_running in ('Yes', 'y', 'yes', 'Y', 'YES'):
    continue

else:
    break
