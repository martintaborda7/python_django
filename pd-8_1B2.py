# IMPORTANTE: NO borrar los comentarios

# Alumno:
# Hemos creado distintas listas de compras
# con los datos de compra de varios clientes.

# IMPORTANTE:
# No todas las compras/diccionarios
# tienen exactamente los mismos campos y datos.
# Por ejemplo, en una de las listas de compras el cliente
# no hay comprado ningún producto.
# Deberá hacer uso del método "get" de diccinoarios
# o el operador "in" para evitar que su programa
# explote intentando accede a los datos del diccionario
# en cada caso

# Su misión es completar la función "procesar_monto"
# que hemos dejado vacia para que las desarrolle.
# La función recibe por parámetro una lista de compras
# y lo importante es que su función deberá funcionar bien
# sin importar que lista de compras que reciba,
# Para eso deberá hacer uso de bucles, condicionales
# y el operador "get" o "in" para acceder a los datos
# indistintamente del comprador SIN que explote su programa

def lista_compras_1():
    return [
        {
            "cliente": {
                "nombre": "Juan",
                "apellido": "Pérez",
                "email": "juanperez@mail.com"
            },
            "fecha": "2022-03-23",
            "productos": [
                {
                "nombre": "Camiseta deportiva",
                "precio": 20,
                },
                {
                "nombre": "Zapatillas de running",
                "precio": 80,
                },
                {
                "nombre": "Mallas deportivas",
                }
            ]
        },
        {
            "cliente": {
                "nombre": "Laura",
                "apellido": "Thompson",
                "email": "laura@mail.com"
            },
            "fecha": "2022-03-28",
        },
        {
            "cliente": {
                "nombre": "Daniela",
                "apellido": "Martinez",
                "email": "daniela@mail.com"
            },
            "fecha": "2022-03-31",
            "productos": [
                {
                "nombre": "Camiseta deportiva",
                "precio": 30,
                },
            ]
        },
    ]

def lista_compras_2():
    return [
        {
            "cliente": {
                "nombre": "Juan",
                "apellido": "Pérez",
                "email": "juanperez@mail.com"
            },
            "fecha": "2022-03-23",
            "productos": [
                {
                "nombre": "Camiseta deportiva",
                "precio": 20,
                },
                {
                "nombre": "Mallas deportivas",
                "precio": 18,
                }
            ]
        },
        {
            "cliente": {
                "nombre": "Laura",
                "apellido": "Thompson",
                "email": "laura@mail.com"
            },
            "fecha": "2022-03-28",
            "productos": [
                {
                "nombre": "Camiseta deportiva",
                "precio": 50,
                },
            ]
        },
        {
            "cliente": {
                "nombre": "Daniela",
                "apellido": "Martinez",
                "email": "daniela@mail.com"
            },
            "fecha": "2022-03-31",
            "productos": [
                {
                "nombre": "Mallas deportivas",
                "precio": 12,
                }
            ]
        },
    ]


def procesar_monto(lista_compras):
    print("Funcion procesar monto")
    monto = 0
    # ------------------------
    # Alumno:
    # Deberá sumar todos los precios de todos los clientes
    # dentro de la lista de compras para
    # obtener el monto total de la compra
    
    # Ej: Para la lista 1 es el resultado esperado
    # en "monto" es 130
    
    # Ej: Para la lista 2 es el resultado esperado
    # en "monto" es 100
    
    # Comienza aquí su código
    monto = 0
    for compra in lista_compras:
        if "productos" in compra:
            productos = compra.get("productos", [])
            for producto in productos:
                precio = producto.get("precio", 0)
                monto += precio
    return monto
    
    # ------------------------
    


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    lista_compras = lista_compras_1()
    monto = procesar_monto(lista_compras)
    
    print("El monto total de la lista 1 es:", monto)
    
    lista_compras = lista_compras_2()
    monto = procesar_monto(lista_compras)
    
    print("El monto total de la lista 1 es:", monto)

    print("terminamos")