import Modulo_clase
import Modulo_algoritmos
import Modulo_tp1


def CargaTratamientos(v):
    cantidad_tratamientos = 0

    # Apertura simple de archivo según el estándar de la materia
    m = open("tratamientosPRUEBAS.csv")
    m.readline()  # Salta el encabezado

    for linea in m:
        linea_limpia = linea[:-1]  # Quita el salto de línea (\n)
        if not linea_limpia:
            continue

        dni, nombre, apellido, icd10, monto, complejidad, id_alg = linea_limpia.split(",")
        cantidad_tratamientos += 1
        monto_final = 0

        v.append(Modulo_clase.Tratamiento(
            cantidad_tratamientos,
            dni,
            nombre,
            apellido,
            icd10,
            monto,
            monto_final,
            complejidad,
            id_alg
        ))

    m.close()
    r1_1 = cantidad_tratamientos
    return r1_1, v


def mayor_monto_final_dni(v):
    t_mont_mayor = None
    for t in v:
        if t.conttratamacomplejidad():
            t_mont_mayor = t
            break

    if t_mont_mayor is None:
        return "No hay tratamientos de alta complejidad"

    for t in v:
        if t.conttratamacomplejidad():
            if t.monto_final > t_mont_mayor.monto_final:
                t_mont_mayor = t

    return t_mont_mayor.dni


def calculomontofinalr21(v):
    cont_tratamiento = 0
    acumulador_dif = 0

    for t in v:
        cont_tratamiento += 1
        monto_base = float(t.monto)
        id_alg = int(t.id_alg)

        if id_alg == 1:
            monto_final = Modulo_algoritmos.Algoritmo1(t.conttratamacomplejidad(), monto_base, t.icd10)
        elif id_alg == 2:
            monto_final = Modulo_algoritmos.Algoritmo2(t.conttratamacomplejidad(), monto_base, t.icd10)
        elif id_alg == 3:
            monto_final = Modulo_algoritmos.Algoritmo3(t.conttratamacomplejidad(), monto_base, t.icd10)
        else:
            monto_final = Modulo_tp1.calcular_monto_tratamiento(t.icd10, monto_base)

        t.monto_final = monto_final
        diferencia = monto_final - monto_base
        acumulador_dif += diferencia

    if cont_tratamiento > 0:
        promedio_r21 = acumulador_dif / cont_tratamiento
    else:
        promedio_r21 = 0

    return promedio_r21


def letracodmastratamiento_r22(v):
    lista = []
    letras = []
    cantidades = []

    for t in v:
        lista.append(t.icd10[0])

    for x in lista:
        if x in letras:
            pos = letras.index(x)
            cantidades[pos] += 1
        else:
            letras.append(x)
            cantidades.append(1)

    pos_mayor = 0
    for i in range(len(cantidades)):
        if cantidades[i] > cantidades[pos_mayor]:
            pos_mayor = i

    return letras[pos_mayor], cantidades[pos_mayor]


def r1_2(v):
    contador_r1_2 = 0
    for t in v:
        if t.conttratamacomplejidad():
            contador_r1_2 += 1
            if contador_r1_2 == 5:
                return t.apellido
    return False


def principal():
    v = []
    op = -1

    while op != 0:
        print("\n1. Cargar Tratamientos")
        print("2. Mostrar Resultados")
        print("0. Salir")

        op = int(input("Ingrese opción: "))

        if op == 1:
            r11, v = CargaTratamientos(v)
            print("r1.1:", r11)

            r12 = r1_2(v)
            if r12 == False:
                print("r1.2: No hay suficientes tratamientos de alta complejidad")
            else:
                print("r1.2:", r12)

        elif op == 2:
            if v:
                r21 = calculomontofinalr21(v)
                print("r2.1:", r21)
                r22, r23 = letracodmastratamiento_r22(v)
                print("r2.2:", r22)
                print("r2.3:", r23)
                r24 = mayor_monto_final_dni(v)
                print("r2.4:", r24)
            else:
                print("************\nNo hay tratamientos cargados\n************")


if __name__ == "__main__":
    principal()