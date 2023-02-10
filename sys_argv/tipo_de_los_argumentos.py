import sys

if __name__ == "__main__":
    anyo = sys.argv[1]
    print(f"El primer argumento recibido es: {anyo}. Ah! y su tipo es {type(anyo)}")

    anyo_int = int(sys.argv[1])
    print(f"El primer argumento recibido es: {anyo_int}. Ah! y su tipo es {type(anyo_int)} (gracias a que hicimos una operación de cast)")

    lista_elementos = sys.argv[2]
    print(f"La lista de elementos es: {lista_elementos}. Y su tipo es {type(lista_elementos)}")

    lista_elementos_int = sys.argv[2].split(",")
    print(f"La lista de elementos es: {lista_elementos_int}. Y su tipo es {type(lista_elementos_int)}")

    for element in lista_elementos_int:
        print(f"El tipo de cada elemento es: {type(element)}")

    lista_elementos_int_pero_de_verdad = [int(arg) for arg in sys.argv[2].split(",")]
    print(f"La lista de elementos es: {lista_elementos_int_pero_de_verdad}. Y su tipo es {type(lista_elementos_int_pero_de_verdad)}")

    for element in lista_elementos_int_pero_de_verdad:
        print(f"El tipo de cada elemento es: {type(element)}")
