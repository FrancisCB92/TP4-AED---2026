class Afiliado:

    def __init__(self, id, dni, codigo, nivel, tope):
        self.id = id
        self.dni = dni
        self.codigo = codigo
        self.nivel = nivel
        self.tope = tope




    def __str__(self):
        r = ""
        r += "\nid: " + str(self.id)
        r += "\ndni: "+ str(self.dni)
        r += "\ncodigo: " + str(self.codigo)
        r += "\nnivel: " + str(self.nivel)
        r += "\ntope: " + str(self.tope)
        return r