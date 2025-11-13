
option = ""
Inventary = []
while option != 4:
      print("")
      print("MENÚ PRINCIPAL")
      print("1.Agregar producto")
      print("2.Mostrar inventario")
      print("3.Calcular estadísticas")
      print("4.Salir")
      print("")

      option = input("Ingresa opcion (1-4): ")

      if option == '1':
            amaount = int(input("Cuantos productos vas a agregar: "))
            print("")
        #solicitar producto
            while amaount != 0 : 
                product = input("Ingrese el nombre del producto: ").strip().capitalize() #strip quita espacios #capitalize coloca primera letra en mayuscula
                price = float(input("enter the price of product: "))
                quantity = int(input("enter quantity: "))
                print("")
                print("")

                Compras = {  #se hace diccionario para la lista
                         "producto" : product,
                         "precio" : price,
                         "cantidad" : quantity,
          
                        }
                amaount -=1 #amaount se coloca para que vaya descontando de la cantidad que se ongresa a hasta llegar 0 
                Inventary.append(Compras) #agregar productos al final de la lista
                print(f"te faltan {amaount} productos por ingresar")
        
      elif option == '2':
              if Inventary: #se coloca para ingresar al inventrio y sacar los productos
                     for index, item in enumerate(Inventary,1 ): #para recorrer el inventario index para recorrer y item para sacar el inventario, enumerate es para convertir el diccionario en pequeñas listas.
                            print(f"--- Producto {index} ---")
                            print(f"nombre: {item['producto']}")
                            print(f"precio: {item['precio']}")
                            print("-" * 20)
                     
              else:
                     print("Inventario esta vacio.")       
                     print("")
      

      elif option == '3':
                print("")
                print("--- CÁLCULO DE ESTADÍSTICAS ---")            
                
                if Inventary:
                    # 1. Asegurarse de que el campo 'total' exista
                   # Si la Opción 2 ya lo calcula, este paso es para seguridad.
                   for item in Inventary:
                       # Se recalcula el total solo si no existe o si es necesario
                       if 'total' not in item:
                           item['total'] = item['cantidad'] * item['precio']
                   
                   
                   # 2. Extraer todos los valores 'total' usando
                   # Esto crea una lista como [15.0, 40.5, 20.0, ...]
                   totales_por_producto = [item['total'] for item in Inventary]
                   
                   
                   # 3. Sumar todos los totales para obtener el valor total del inventario
                   total_general_inventario = sum(totales_por_producto)
                   
                   
                   # 4. Mostrar el resultado
                   print(f"Número total de productos únicos en inventario: {len(Inventary)}")
                   print("-" * 40)
                   print(f"El VALOR TOTAL del inventario es: ${total_general_inventario:.2f}")#.2f quita decimales
                   print("-" * 40)
                   
                else:
                   print("No hay productos en el inventario para calcular estadísticas.")   


      elif option == '4':
               print("")
               print("Saliendo...")      

      else:
              print("Digite un valor que este en el menu o valido")

#El objetivo de la semana fue aprender a hacer listas, diccionario, a iterar y asi hacer una base de datos 