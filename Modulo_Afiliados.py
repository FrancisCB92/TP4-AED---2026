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



def esafiliado(dni, vector):
    izq, der = 0, len(vector) - 1
    while izq <= der:
        c = (izq + der) // 2
        if dni == vector[c].dni:
            #print("se encontró afiliado!: ", dni)
            return True
        if dni < vector[c].dni:
            der = c - 1
        else:
            izq = c + 1
    return False


# TESTEAER CON LOS VALORES DE EJEMPLO DE LA CONSIGNA!!!!!!
# [] se llama al afiliado concreto y al vector de afiliados ¿hay forma de simplificar esto?
def calculomontosobrasocial(afiliado, tratamiento, vectorafiliados):
    monto_cubierto = 0
    monto_no_cubierto = 0

    if esafiliado(tratamiento.dni, vectorafiliados):
        porcentaje = porcentajecubierto(afiliado.nivel, tratamiento.conttratamacomplejidad())
        monto_cubierto = Modulo_algoritmos.aplicaporcentaje(tratamiento.monto_final, porcentaje)
        if monto_cubierto >= afiliado.tope:
            monto_cubierto = afiliado.tope


    monto_no_cubierto =  tratamiento.monto_final - monto_cubierto

    return monto_cubierto, monto_no_cubierto


#if __name__ == "__main__":
    #calculomontosobrasocial(afiliado, tratamiento, vectorafiliados)
