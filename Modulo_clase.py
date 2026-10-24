class Tratamiento:

    def __init__(self, id, dni, nombre, apellido, icd10, monto, monto_final, complejidad, id_alg):
        self.id = id
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.icd10 = icd10
        self.monto = float(monto)
        self.monto_final = float(monto_final) # se inicializa con 0
        self.complejidad = complejidad
        self.id_alg = id_alg




    def __str__(self):
        r = ""
        r += "\nid: " + str(self.id)
        r += "\ndni: "+ str(self.dni)
        r += "\nnombre: " + self.nombre
        r += "\napellido: " + self.apellido
        r += "\nicd10: " + self.icd10
        r += "\nmonto: "+ str(self.monto)
        r += "\nmonto final: " + str(self.monto_final)
        r += "\ncomplejidad: " + self.complejidad
        r += "\nid_alg: " + self.id_alg
        return r

    def conttratamacomplejidad(self):
        if self.complejidad == "A":
            return True
        else:
            return False