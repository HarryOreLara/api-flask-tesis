class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    

    #esto es como se guardara en la base de datos, es decir es la collection
    def toDbConnection(self):
        return {
            'name':self.name,
            'price':self.quantity,
            'quantity':self.quantity
        }