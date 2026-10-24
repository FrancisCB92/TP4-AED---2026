def ExtraerDatosCodigo(codigo):
    letra = codigo[0]
    numcapitulo = int(codigo[1:3])
    if "." in codigo:
        porcentaje = int(codigo.split(".")[1])
    else:
        porcentaje = int(codigo[4:])
    return letra, porcentaje, porcentaje, numcapitulo


def sumafijapuntoa(monto):
    return monto + 25000


def sumafijapuntob(letra, monto):
    if "A" <= letra <= "L":
        monto += 25000
    elif "M" <= letra <= "Z" and letra != "U":
        monto += 40000
    elif letra == "U":
        monto += 100000
    return monto


def aplicarporcentaje(monto, porcentaje):
    monto_final = monto + (monto * porcentaje / 100)
    return monto_final


def calcular_monto_tratamiento(Cod_ICD10, monto_base):
    base = float(monto_base)
    letra, parte_decimal, porcentaje, numcapitulo = ExtraerDatosCodigo(Cod_ICD10)

    monto = sumafijapuntoa(base)
    monto = sumafijapuntob(letra, monto)
    monto_final = aplicarporcentaje(monto, porcentaje)

    return monto_final

def principal(Cod_ICD10, monto_base):
    codigo = Cod_ICD10
    base = monto_base

    letra, parte_decimal, porcentaje, numcapitulo = ExtraerDatosCodigo(codigo)


    monto = sumafijapuntoa(base)

    monto = sumafijapuntob(letra, monto)

    monto_final = aplicarporcentaje(monto, porcentaje)

    # prints para testeo

    print("Codigo:", codigo)
    print("Capitulo:", numcapitulo)
    print("Monto a pagar:", monto_final)

    return monto_final

if __name__ == "__main__":

    principal("H70.1", "5200")

