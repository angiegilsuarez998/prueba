
#https://github.com/daveshb/riwipython/blob/main/modulo1/semana1/Taller1.md
#https://github.com/Riwi-io-Medellin/Python_Fundamentals/blob/main/02_variable_types/variable_types.md

# la f es para poder colocar variable y un print al mismo tiempo. habilita utiliza {} para colocar las variables e imprimir
# if es un si condicional 
# el "entonces" es :
# el "int" es para convertir un numero en un entero para que funcionen las condicionales
#todo input debe ser texto



print("hola mundo")

name = input("ingrese su nombre:")
age = int(input("ingrese su edad:"))


name_age = f"su nombre es {name} y su edad es {age} años" #este es tipo variable en vez de print

print(name_age)
print(f"su nombre es {name} su edad es {age} años")


if age > 17 :
    print(f"{name} es mayor de edad")

else:
    print(f"{name} es menor de edad")


#