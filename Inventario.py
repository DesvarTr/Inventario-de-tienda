#Realizado por Gonzalo Montezuma

inventario = []

def agregar_producto():

    while True:

        nombre = input("Ingres el nombre del producto: ").lower().capitalize()
        instancias = int(input(f"Ingrese la cantidad de existencias del producto {nombre}: "))
        precio = float(input(f"Ingrese el precio que tiene el producto {nombre}: "))

        if instancias < 0:
            print("Ingrese un valor positivo para las existencias")
            continue
        
        if precio < 0:
            print("Ingrese un valor positivo para el precio")
            continue

        else:
            inventario.append([nombre,instancias,precio])
            print(f"--El producto {nombre} fue añadido exitosamente--\n")
            break

def eliminar_producto():
    
    bul = False

    while True:

        nombre = input("Ingrese el nombre del producto: ").lower().capitalize()
        for x in inventario:

            if x[0] == nombre:

                productpamensaje = x[0]
                inventario.remove(x)
            
                print(f"El producto {productpamensaje} fue eliminado exitosamente\n")
                bul = True
                break

        if bul:
            break

        else:
            print("--El producto solicitado no fue encontrado, intente nuevamente--")
            continue       
    
def consultar_inv():

    print("El inventario completo es:")
    for x in inventario:
        print(x)
    
    print()

def actualizar():

    bul = False

    while True:

        nombre = input("Ingrese el nombre del producto: ").lower().capitalize()
        novo_existencias = input(f"Ingrese la nueva cantidad de existencias que posee del producto {nombre}: ")
        for x in inventario: 

            if x[0] == nombre:
                
                old_existencias = x[1]

                productpamensaje = x[0]

                x[1] = novo_existencias

                print(f"--El numero de existencias del producto {productpamensaje} se ha actualizado de {x[1]} existencias a {old_existencias} existencias--\n")
                bul = True
                break
            
        if bul:
            break

        else:
            print("--El producto solicitado no fue encontrado, intente nuevamente--")
            continue

def menu():

    while True:

        print("""1. Agregar un nuevo producto
2. Eliminar un producto existente
3. Actualizar las existencias de un producto existente
4. Consultar el inventario completo de los productos
5. Cerrar el programa""")
        opcion = int(input("Ingrese la opción deseada: "))
        print()

        if opcion == 1:
            agregar_producto()

        elif opcion == 2:
            eliminar_producto()

        elif opcion == 3:
            actualizar()
        
        elif opcion == 4:
            consultar_inv()

        elif opcion == 5:
            print("Programa cerrado")
            break

        else:
            print("Ingrese una opción válida")

menu()