# PENDIENTES
# [] falla este punto r2.1: de los comentarios entrega del TP3, pero no tenemos los valores de entreda para probar, algun algoritmo de calculo de monto final
# no funciona bien, puede ser del TP3: módulo algoritmos o el módulo del TP1 (este último no está testeado) o es la lógica del último paso del punto r2.1 del TP3
# en este último caso no interesa para este TP4.
# r2.1: 31471.151477599982 --> Incorrecto (esperado: (30245.9809074 <= resultado <= 30246.0809074) o (29540.880907400002 <= resultado <= 29540.9809074))





import Modulo_clase
import Modulo_clase_Afiliado
import Modulo_algoritmos
import Modulo_tp1



# Funciones tomadas de los simulacros de parcial: algoritmo de búsqueda binaria para order el vector

def aniadir_en_orden(v, afiliado):
    n = len(v)
    izq, der = 0, n - 1 # ****
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if v[c].dni == afiliado.dni:
            pos = c
            break
        elif v[c].dni > afiliado.dni:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [afiliado]


def cargarafiliados():
    v1 = []  # este reinicia el vector en cada llamada

    m = open("coberturas.csv")
    m.readline()
    id_afiliado = 0

    for linea in m:
        linea_limpia = linea[:-1]  # Quita el salto de línea (\n)
        if not linea_limpia:
            continue

        dni, codigo, nivel, tope = linea_limpia.split(",")
        id_afiliado += 1

        afiliado = Modulo_clase_Afiliado.Afiliado(
                                                  id_afiliado,
                                                  dni,
                                                  codigo,
                                                  nivel,
                                                  tope
                                                  )


        aniadir_en_orden(v1, afiliado)

    m.close()

    return v1




def CargaTratamientos(v2):
    id_tratamientos = 0

    # Apertura simple de archivo según el estándar de la materia
    m = open("tratamientos.csv")
    m.readline()  # Salta el encabezado

    for linea in m:
        linea_limpia = linea[:-1]  # Quita el salto de línea (\n)
        if not linea_limpia:
            continue

        dni, nombre, apellido, icd10, monto, complejidad, id_alg = linea_limpia.split(",")
        id_tratamientos += 1
        monto_final = 0

        v2.append(Modulo_clase.Tratamiento(
            id_tratamientos,
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

    return v2



def calculomontofinal(v):
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
    v1 = []
    v2 = []
    op = -1

    while op != 0:
        print("\n1. Cargar afiliados")
        print("2. Cargar tratamientos")
        print("3. Mostrar resultados")
        print("0. Salir")

        op = int(input("Ingrese opción: "))

        if op == 1:
            v1 = cargarafiliados()
            print("opción 1 seleccionada...")


        elif op == 2:
            v2 = CargaTratamientos()
            print("opción 2 seleccionada...")

        elif op == 3:

            print("opción 3 seleccionada...")


if __name__ == "__main__":
    principal()