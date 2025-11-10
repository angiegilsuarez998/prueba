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

#hacer un contador
iterador = 0
while iterador < 5:
    print("El iterador es: ", iterador)
    # iterador += 1 #metodo mas corto, le suma el 1 y lo asigna
    iterador = iterador + 1

# Python permite agregar un bloque else a un while.
# Este se ejecuta solo cuando el ciclo termina sin usar break.

intentosPermitidos = 3 #variable para intentos de ingreso de contraseña, realmente son 
intentos = 0

contraseñaCorrecta = "python123"
contraseñaUsuario = ""

while contraseñaUsuario != contraseñaCorrecta:
    contraseñaUsuario = input("Introduce la contraseña: ")
    intentos += 1 #suma de uno en uno y cuando llegue a 3 quema las posibilidades
    print(intentos)

    if contraseñaUsuario == contraseñaCorrecta: #se iguala con la contraseña correcta para que no solo salga la erronea
        print("contraseña correcta")
        print("Bienvenido al programa")
        break #se debe colocar para que no siga con el otro if.

    if intentosPermitidos == intentos: #cuando los intentos lo igualan por la suma
        print("intente en una hora")
        break #se cierra el bucle de la contraseña


else:
    print("¡Contraseña correcta!") #ejecuta otro codigo si el while tiene un error o deja de funcionar




