
# #si es menor de 10, el color es azul
# # si es mayor que 10, el color es gris
# # si es mayor de 40, el color es negro

# value = 41

# if value < 10:
#     print(f"el color es azul")
    
# elif value >= 10 and value < 40:
#     print("el color es gris")
    
# else:
#     print("el color es negro")

# #se usa para rango que es star, stop y step (que hace salto en el conteo)
# for i in range(1,100,2): 
#     print("hola")


# entrada = ""

# while entrada != "x": #pide la x para salir del ciclo
#     print("sigue adentro")
#     entrada = input("ingrese x para salir: ")

# #hacer un contador
# iterador = 0
# while iterador < 5:
#     print("El iterador es: ", iterador)
#     # iterador += 1 #metodo mas corto, le suma el 1 y lo asigna
#     iterador = iterador + 1

# # Python permite agregar un bloque else a un while.
# # Este se ejecuta solo cuando el ciclo termina sin usar break.

# intentosPermitidos = 3 #variable para intentos de ingreso de contraseña, realmente son 
# intentos = 0

# contraseñaCorrecta = "python123"
# contraseñaUsuario = ""

# while contraseñaUsuario != contraseñaCorrecta:
#     contraseñaUsuario = input("Introduce la contraseña: ")
#     intentos += 1 #suma de uno en uno y cuando llegue a 3 quema las posibilidades
#     print(intentos)

#     if contraseñaUsuario == contraseñaCorrecta: #se iguala con la contraseña correcta para que no solo salga la erronea
#         print("contraseña correcta")
#         print("Bienvenido al programa")
#         break #se debe colocar para que no siga con el otro if.

#     if intentosPermitidos == intentos: #cuando los intentos lo igualan por la suma
#         print("intente en una hora")
#         break #se cierra el bucle de la contraseña


# else:
#     print("¡Contraseña correcta!") #ejecuta otro codigo si el while tiene un error o deja de funcionar

#FUNCION
#una funcion es un bloque de codigo reutilizable, se busca que las funciones cumplan un objetivo.
# def saludar(aqui van lo parametros que quiero en la funcion o a la variablae (lista)) #def siempre se coloca, en parentesis se puede colocar las variables
# print(f"saludar")

# x = 10
# def showmain():
#     x = 20
#     print(x)

# showmain()
# print(x)
    #se imprimen las 2 varibles de x ya que una esta dentro de la funcion y la otra esta fuera

# nums = [23, 22, 10, 100]
# animals = ["cat", "dog", "horse", "elephant"]

# def showFirstAndLast(cosas):
#     first = cosas[0] #variable que define que va a imprimir de las listas anteriores
#     last = cosas[3]
#     return first , last #lo que hace retornar las informacion que estan en la varible

# num1, num2 = showFirstAndLast(nums)
# animal1, animal2 = showFirstAndLast(animals)

# print(num1, num2) 
# print(animal1, animal2)


#funcion lambda, son funciones abreviadas, ya que no necesita una declaración return y puede aceptar múltiples argumentos, pero solo contiene una única expresión. 
# # Función que suma dos números
# suma = lambda x, y: x + y
# print(suma(5, 3))  # Salida: 8

# # Función para invertir una cadena de texto
# invertir = lambda s: s[::-1]
# print(invertir("hola"))  # Salida: aloh


# # Usar lambda con la función sorted()
# lista = [(1, 'uno'), (3, 'tres'), (2, 'dos')]
# lista_ordenada = sorted(lista, key=lambda item: item[0])
# print(lista_ordenada)  # Salida: [(1, 'uno'), (2, 'dos'), (3, 'tres')]


#LISTAS
#se define por [] y se separan por ,
# Crear una lista
# frutas = ["manzana", "plátano", "cereza"]

# # Acceder a elementos por índice
# print(frutas[0])  # Salida: manzana

# # Añadir un elemento
# frutas.append("naranja")
# print(frutas)  # Salida: ['manzana', 'plátano', 'cereza', 'naranja']

# # Eliminar un elemento
# frutas.remove("plátano")
# print(frutas)  # Salida: ['manzana', 'cereza', 'naranja']


#METODO = funciones


# frutas = ["manzana", "plátano", "cereza"]
# frutas.append("mandarina") #se coloca el nombre de la lista y cada que se agrega un metodo es con "."
# #se hace para agregar nuevos elemenos en la lista
# print(frutas)


Numbers = ["1", "4", "2", "3", "5", "7", "6", "8"]
Numbers.sort() #metodo para organizar numeros
print(Numbers)





