import Modulo_clase
import Modulo_algoritmos
import Modulo_tp1

def CargaTratamientos(v):
    cantidad_tratamientos = 0

    # Apertura simple de archivo según el estándar de la materia
    m = open("tratamientos.csv")
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




def principal():
    v = []
    op = -1

    while op != 0:
        print("\n1. Cargar Tratamientos")
        print("2. Mostrar Resultados")
        print("0. Salir")

        op = int(input("Ingrese opción: "))

        if op == 1:
            v = CargaTratamientos(v)
            print("opción 1 seleccionada...")


        elif op == 2:
            print("opción 2 seleccionada...")


if __name__ == "__main__":
    principal()