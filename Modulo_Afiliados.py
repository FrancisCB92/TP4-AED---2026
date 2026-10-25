import Modulo_algoritmos



def porcentajecubierto(nivel, complejidad):
    # así es escalable?
    # f = nivel, c = complejidad
    cobertura = [
        [50, 40],
        [70, 60],
        [90, 80],
    ]
    porcentaje_cubierto = cobertura[nivel][complejidad]
    return porcentaje_cubierto



def esafiliado(tratamiento_dni, vectorafiliados):
    izq, der = 0, len(vectorafiliados) - 1
    while izq <= der:
        c = (izq + der) // 2
        if tratamiento_dni == vectorafiliados[c].dni:
            #print("se encontró afiliado!: ", dni)
            return vectorafiliados[c]
        if tratamiento_dni < vectorafiliados[c].dni:
            der = c - 1
        else:
            izq = c + 1
    return False


# TESTEAER CON LOS VALORES DE EJEMPLO DE LA CONSIGNA!!!!!!
# [] se llama al afiliado concreto y al vector de afiliados ¿hay forma de simplificar esto?
def calculomontosobrasocial(afiliado, tratamiento):
    monto_cubierto = aplicatopes = 0
    monto_no_cubierto = 0

    if afiliado:
        porcentaje = porcentajecubierto(afiliado.nivel, tratamiento.conttratamacomplejidad())
        monto_cubierto = Modulo_algoritmos.aplicaporcentaje(tratamiento.monto_final, porcentaje)
        if monto_cubierto >= afiliado.tope:
            monto_cubierto = afiliado.tope
            aplicatopes = True


    monto_no_cubierto =  tratamiento.monto_final - monto_cubierto

    return monto_cubierto, monto_no_cubierto, aplicatopes


#if __name__ == "__main__":
    #calculomontosobrasocial(afiliado, tratamiento, vectorafiliados)
