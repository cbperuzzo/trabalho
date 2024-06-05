class Produto:
    def __init__(
        self, 
        modelo: str, 
        marca: str, 
        preco: float, 
        cor: str
        ):
        
        self.modelo = modelo
        self.marca = marca
        self.preco = preco
        self.cor = cor

    def save(self):
        pass

    @staticmethod
    def getAll():
        pass
    @staticmethod
    def getWhereModelo(str):
        pass