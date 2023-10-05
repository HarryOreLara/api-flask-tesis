class Analisis:
    def __init__(self, idPersona, nombre, frase, fecha, estado_animo):
        self.idPersona = idPersona
        self.nombre = nombre
        self.frase = frase
        self.fecha = fecha
        self.estado_animo = estado_animo

    def toDBCollection(self):
        return{
            'idPersona':self.idPersona,
            'nombre':self.nombre,
            'frase':self.frase,
            'fecha':self.fecha,
            'estado_animo':self.estado_animo
        }