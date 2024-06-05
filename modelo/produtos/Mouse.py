from Produto import Produto

class Mouse(Produto):
    def __init__(
        self, 
        modelo: str, 
        preco: float, 
        cor: str, 
        sensibilidade_dpi: int,
        tamanho_cm: float
        ):

        super().__init__(modelo, preco, cor)
        self.sensibilidade_dpi = sensibilidade_dpi
        self.tamanho_cm = tamanho_cm

    def save(self):
        pass

    @staticmethod
    def getAll():
        pass
    @staticmethod
    def getWhereModelo(str):
        pass