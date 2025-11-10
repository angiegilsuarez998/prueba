#solitud del producto input()

Name = input("Ingrese nombre del producto: ")

#se coloca while para validar true o false, en este casa solo se ejecuto true.
#el false se genera con except valueError para arrojar error y solicitar nuevamente el dato.

while True:

    try:
        price = float(input("Ingrese el precio: "))
        break

    except ValueError:
        print("Error! ingresa un valor correcto")

while True:
    try:
        quality = int(input("Ingresa la cantidad: "))
        break
    
    except ValueError:
        print("Error! ingresa un valor correcto")


#funcion de multiplicar

total_cost = price*quality

print(f"El resulto de tu compra es: {total_cost}")

#la f es para poder colocar variable y un string al mismo tiempo. habilita utiliza {} para colocar las variables e imprimir

print(f"Producto {Name} | Precio Unitario {price} | Cantidad {quality} | Costo total {total_cost}")


#el programa ayuda a hacer una base de datos para inventrio solicitando datos precisos y



