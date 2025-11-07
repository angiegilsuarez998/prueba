
# #Nivel 1 - Fundamentos y Variable



# #1.

# name = input("Ingrese su nombre: ") #variable que ingresa el usuario
# age = int(input("Ingrese su edad: ")) #variable que ingresa el usuario

# print(f"Hola {name}, tienes {age} años") #impresion en la terminal de la información. Se pone f para colocar variable y un print al mismo tiempo.

# print()
# print()

# #2.
# print("*" * 10, "|| Suma ||","*"*10)
# print()

# number1 = float(input("Ingrese el primer número: ")) #variable ingresada por el usuario

# number2 = float(input("Ingrese el segundo número: ")) #variable ingresada por el usuario

# suma = number1 + number2 #suma de las variables

# print("La suma de los dos números es: " , suma) #impresion resultado de la suma 

# print()
# print("*" * 10, "|| Área de un rectagulo con los datos anteriores ||","*"*10)
# print()

# #3. Área triangulo

# Base = abs(number1) #se coloca variable del usuario input number1, con funcion integrada abs() para devolver valor adsoluto en caso de ser negativa la variable.

# height = abs(number2) #se coloca variable del usuario input number2, con funcion integrada abs() para devolver valor adsoluto en caso de ser negativa la variable.

# Area = (Base * height) / 2 #formula para sacar el área

# print("El área del triangulo es: ", Area)

# #4 
# print()
# print("*" * 10, "|| Conversión de temperatura ||","*"*10)
# print()

# Temperature = int(input("Ingrese la temperatura en grados celsius: ")) #variable ingresada por el usuario

# change = (Temperature * 9/5) + 32 #formula de conversion

# print(f"Conversión de temperatura: , {change} °F")

# #5

# print()
# print("*" * 10, "|| Tipos de datos ||","*"*10)
# print()

# print(f"Tu nombre es de tipo: {type(name)}. Los números son de tipo: {type(number1)}. Tu edad es de tipo: {type(age)}" )

# #6
# print()
# print("*" * 10, "|| Edad futura ||","*"*10)
# print()

# print(f"{name}, en 10 años tendras {age+10} años.") #reciclo los datos iniciales haciendo una suma y imprimo.

# #7

# print()
# print("*" * 10, "|| Edad autorizada ||","*"*10)
# print()

# name_age = f"su nombre es {name} y su edad es {age} años" #variable que recicla datos anteriores

# print(name_age)

# if age > 17 :
#     print(f"{name} es mayor de edad") #se usa si condicional

# else:
#     print(f"{name} es menor de edad") 

# #8
# print()
# print("*" * 10, "|| Programa para saber si un número es positivo, negativo o cero ||","*"*10)
# print()


# # Pedimos el número al usuario

# num = float(input("Ingresa un número: "))

# # Estructura condicional

# if num > 0:
#     print("El número es positivo.")

# elif num < 0:
#     print("El número es negativo.")

# else:
#     print("El número es cero.")

# #9

# print()
# print("*" * 10, "|| par o impar ||","*"*10)
# print()


# num1 = int(input("Ingresa un número: ")) # Pedir al usuario un número


# if num1 % 2 == 0:
#     print(f"El número {num1} es par.") # Verificar si es par o impar

# else:
#     print(f"El número {num1} es impar.")

# #10 

# print()
# print("*" * 10, "|| Calculadora Básica ||","*"*10)
# print()

# num2 = float(input("Ingrea un número: ")) #solo se solicita un numero ya que el otro de recicla

# operator = input("Ingresa el signo de la operacion que deseas realizar (+, -, *, /): ") #se hace variable con input 

# if operator == "+": 
#     print(f"La suma de {num1} y {num2} es igual a: {num1+num2} ")
# elif operator == "-": 
#     print(f"La resta de {num1} y {num2} es igual a: {num1-num2} ")
# elif operator == "/": 
#     print(f"La division de {num1} y {num2} es igual a: {num1/num2} ")
# elif operator == "*": 
#     print(f"La multiplicación de {num1} y {num2} es igual a: {num1*num2} ")

# else:
#     print("Operación no válida.") #si el usuario no ingrea el signo correcto

# #11
# print()
# print("*" * 10, "|| Clasificador de notas (Excelente, Aprobado, Reprobado) ||","*"*10)
# print()

# nota = float(input("Ingresa la nota: "))

# if nota == 100: 
#     print(f"Excelente")
# elif nota >=70:
#     print(f"Aprobado")
# elif nota <= 69:
#     print(f"Reprobado")

# #12
# print()
# print("*" * 10, "|| Comparador de tres números: mayor y menor. ||","*"*10)
# print()

# num3 = float(input("Ingrese el tercer número: "))

# if num1 > num2 and num1 > num3:
#     mayor = num1

# elif num2 > num1 and num2 > num3:
#     mayor = num2
# else:
#     mayor = num3

# # Determinar el número menor

# if num1 < num2 and num1 < num3:
#     menor = num1

# elif num2 < num1 and num2 < num3:
#     menor = num2

# else:
#     menor = num3

# # Mostrar resultados
# print(f"El número mayor es: {mayor}")
# print(f"El número menor es: {menor}")

# #13
# print()
# print("*" * 10, "|| Contar del 1 al 10 ||","*"*10)
# print()

# for i in range(1, 11):
#     print(i)

#14
print()
print("*" * 10, "|| Sumatoria del 1 al n ||","*"*10)
print()

n = int(input("Ingresa un número: "))
for i in range (n): 
    digit = i #el i es igual a 1, lo que hace es que el numero que el usuario ingrese el mismo se sume las veces del numero.
    result = digit + (digit+1)
    print(result)
    i += 1


#15
print()
print("*" * 10, "|| Tabla de multiplicar ||","*"*10)
print()


