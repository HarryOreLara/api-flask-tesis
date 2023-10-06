class Analisis:
    def __init__(self, idPersona, frase, fecha, estado_animo):
        self.idPersona = idPersona
        self.frase = frase
        self.fecha = fecha
        self.estado_animo = estado_animo

    def toDBCollection(self):
        return{
            'idPersona':self.idPersona,
            'frase':self.frase,
            'fecha':self.fecha,
            'estado_animo':self.estado_animo
        }