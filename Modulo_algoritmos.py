def aplicaporcentaje(base, porcentaje):
    monto_porcenaje = (base * porcentaje) / 100
    return monto_porcenaje


def Algoritmo1(alta_complejidad, monto_base, ICD10):
    monto_base = float(monto_base)
    suma_fija = 0

    if monto_base > 60000:
        if "." in ICD10:
            porcentaje_extra = int(ICD10.split(".")[1])
        else:
            porcentaje_extra = int(ICD10[4:])

        if alta_complejidad and ICD10[0] != "U":
            suma_fija = monto_base / 2
    else:
        porcentaje_extra = 0

    monto_porcentaje = aplicaporcentaje(monto_base, porcentaje_extra)
    monto_final = monto_base + monto_porcentaje + suma_fija
    return monto_final


def Algoritmo2(alta_complejidad, monto_base, ICD10):
    monto_base = float(monto_base)
    porcentaje_extra = 0

    if "A" <= ICD10[0] <= "P":
        if "." in ICD10:
            porcentaje_extra = int(ICD10.split(".")[1])
        else:
            porcentaje_extra = int(ICD10[4:])
    else:
        if "." in ICD10:
            num_derecha = int(ICD10.split(".")[1])
        else:
            num_derecha = int(ICD10[4:])

        if alta_complejidad:
            porcentaje_extra = 2 * num_derecha
        else:
            porcentaje_extra = 15

    monto_porcentaje = aplicaporcentaje(monto_base, porcentaje_extra)
    monto_final = monto_base + monto_porcentaje
    return monto_final


def Algoritmo3(alta_complejidad, monto_base, ICD10):
    monto_base = float(monto_base)
    monto_extra = 0

    if alta_complejidad:
        monto_extra += aplicaporcentaje(monto_base, 30)

    if "A" <= ICD10[0] <= "L":
        monto_extra = monto_extra + 20000
    elif "M" <= ICD10[0] <= "P":
        monto_extra = monto_extra + 15000 + (5000 * int(ICD10[1:3]))
    else:
        monto_extra += aplicaporcentaje(monto_base, 10)

    if monto_extra > 60000:
        monto_extra = 60000

    monto_final = monto_base + monto_extra
    return monto_final