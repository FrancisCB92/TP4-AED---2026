import ModuloClase


# función de la primera opción para cargar los tratamientos en el vector, tomando las filas del archivo CSV
def CargaTratamientos(v):
    #print("función de opción 1 carga de tratamientos")

    cantidad_tratamientos = 0

    m = open("tratamientos.csv")

    m.readline()

    for linea in m:
        cantidad_tratamientos += 1

        monto_final = 0
        dni, nombre, apellido, icd10, monto, complejidad, id_alg = linea.split(",")

        v.append(ModuloClase.Tratamiento(cantidad_tratamientos,
                                         dni,
                                         nombre,
                                         apellido,
                                         icd10,
                                         monto,
                                         monto_final,
                                         complejidad,
                                         id_alg))

    # dos ejemplos que muestran las dos primeras fijas ya como objetos dentro de vector que pide la consigna
    # llama al metodo especial __str__ para imprimir por  (de los modelos del Parcial3)
    # print(v[1])
    # print(v[2])

    # el primer resultado: cantidad de tratamientos cargados
    r1_1 = cantidad_tratamientos
    return r1_1, v







def principal():
    v = []
    op = -1

    # Bucle principal del menú: se repite hasta seleccionar la opción 3.
    while op != 0:
        print("\n\n1. Cargar Tratamientos")
        print("2. Mostrar Resultados")
        print("0. Salir")

        op = int(input("Ingrese opción: "))

        if op == 1:
            print("opcion 1 seleccionada")
            #v = CargaTratamientos(v)


        if op == 2:
            print("opción 2 seleccionada")


if __name__ == "__main__":
    principal()