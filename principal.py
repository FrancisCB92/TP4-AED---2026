# PENDIENTES
# [] Faltan pruebas y determinar las salidas de r3.__ TODAS!
# [] falló el punto r2.1 del TP anterior: de los comentarios entrega del TP3, pero no tenemos los valores de entreda para probar, algun algoritmo de calculo de monto final
# no funciona bien, puede ser del TP3: módulo algoritmos o el módulo del TP1 (este último no está testeado) o es la lógica del último paso del punto r2.1 del TP3
# en este último caso no interesa para este TP4.
# r2.1: 31471.151477599982 --> Incorrecto (esperado: (30245.9809074 <= resultado <= 30246.0809074) o (29540.880907400002 <= resultado <= 29540.9809074))
from operator import contains

import Modulo_Afiliados
import Modulo_clase
import Modulo_algoritmos
import Modulo_tp1



# Funciones tomadas de los simulacros de parcial: algoritmo de búsqueda binaria para order el vector

def aniadir_en_orden(v, afiliado):
    n = len(v)
    izq, der = 0, n - 1
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
    vectorafiliados = []  # este reinicia el vector en cada llamada

    m = open("coberturasPRUEBAS.csv")
    m.readline()
    id_afiliado = 0


    for linea in m:
        linea_limpia = linea[:-1]  # Quita el salto de línea (\n)
        if not linea_limpia:
            continue

        dni, codigo, nivel, tope = linea_limpia.split(",")
        id_afiliado += 1

        afiliado = Modulo_clase.Afiliado(
                                          id_afiliado,
                                          dni,
                                          codigo,
                                          nivel,
                                          tope
                                          )


        aniadir_en_orden(vectorafiliados, afiliado)


    m.close()

    #for afiliado in vectorafiliados:
    #    print(afiliado)


    return vectorafiliados




def CargaTratamientos():
    vectortratamientos = []
    id_tratamientos = 0

    # Apertura simple de archivo según el estándar de la materia
    m = open("tratamientosPRUEBAS.csv")
    m.readline()  # Salta el encabezado

    for linea in m:
        linea_limpia = linea[:-1]  # Quita el salto de línea (\n)
        if not linea_limpia:
            continue

        #print("línea limpia: ", linea_limpia)
        dni, nombre, apellido, icd10, monto, complejidad, id_alg = linea_limpia.split(",")
        id_tratamientos += 1
        monto_final = 0

        vectortratamientos.append(Modulo_clase.Tratamiento(
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

    return vectortratamientos




def calculomontofinal(vectorafiliados, vectortratamientos):
    #cont_tratamiento = 0
    #acumulador_dif = 0
    obras_sociales = [0] * 20
    r34contnoafiliados = 0
    aplicatopes = False
    r35codigo = r33conttope = 0
    r31monto_cubierto_total = r32monto_no_cubierto_total = monto_cubierto =  monto_no_cubierto = 0
    r36mayor_monto_nocubierto = 0

    for t in vectortratamientos:
        #cont_tratamiento += 1
        monto_base = float(t.monto)
        #print(t)
        id_alg = int(t.id_alg)

        # acá se verifica si es afiliado para luego usar los algoritmos que van a
        # modificar el monto final


        if id_alg == 1:
            monto_final = Modulo_algoritmos.Algoritmo1(t.conttratamacomplejidad(), monto_base, t.icd10)
        elif id_alg == 2:
            monto_final = Modulo_algoritmos.Algoritmo2(t.conttratamacomplejidad(), monto_base, t.icd10)
        elif id_alg == 3:
            monto_final = Modulo_algoritmos.Algoritmo3(t.conttratamacomplejidad(), monto_base, t.icd10)
        else:
            monto_final = Modulo_tp1.calcular_monto_tratamiento(t.icd10, monto_base)

        t.monto_final = monto_final

        # verificar si tiene cobertura y extraer datos del afiliado para hacer cuentas
        afiliado = Modulo_Afiliados.esafiliado(t.dni, vectorafiliados)

        #  acumuladores en una lista de obras sociales: el código de la obra es la [posición + 1]
        obras_sociales[afiliado.codigo - 1] += monto_cubierto


        #=====================
        # R3.1 y R3.2 (y R3.4)
        #=====================
        # determinar si es afiliado
        if afiliado:
            monto_cubierto, monto_no_cubierto, aplicatopes = Modulo_Afiliados.calculomontosobrasocial(afiliado, t)
        else:
            # contador de NO afiliados: para el punto 4
            r34contnoafiliados += 1

        if monto_no_cubierto > r36mayor_monto_nocubierto:
            r36mayor_monto_nocubierto = monto_no_cubierto




        r31monto_cubierto_total += monto_cubierto
        r32monto_no_cubierto_total += monto_no_cubierto


        #=============
        # R3.3
        #=============
        if aplicatopes:
            r33conttope += 1









    #=============
    # R3.5
    #=============
    # acumuladores en una lista de obras sociales para el punto r35
    # [] falta que en caso de empate el de menor código
    mayor = obras_sociales[0]
    pos = 0
    for i in range(len(obras_sociales)):
        if obras_sociales[i] > mayor:
            mayor = obras_sociales[i]
            pos = i
    r35codigo = obras_sociales[pos + 1]

    # =============
    # SALIDAS
    # =============
    print("r3.6: ", r36mayor_monto_nocubierto)


    print(r35codigo)

    return vectortratamientos




def principal():
    vectorafiliados = []
    vectortratamientos = []
    op = -1

    while op != 0:
        print("\n1. Cargar afiliados")
        print("2. Cargar tratamientos")
        print("3. Mostrar resultados")
        print("0. Salir")

        op = int(input("Ingrese opción: "))

        if op == 1:
            vectorafiliados = cargarafiliados()
            #print("opción 1 seleccionada...")


        elif op == 2:
            vectortratamientos = CargaTratamientos()
            #print("opción 2 seleccionada...")

        elif op == 3:
            if vectorafiliados and vectortratamientos:

                calculomontofinal(vectorafiliados, vectortratamientos)
                print("opción 3 seleccionada...")
            else:
                print("el/los vector/es no fueran cargados")


if __name__ == "__main__":
    principal()