from Produto import Produto

class Teclado(Produto):
    def __init__(
        self, 
        modelo: str, 
        preco: float, 
        cor: str, 
        tipo: 'mecânico' or 'membrana',
        milh_toques: int
        ):

        super().__init__(modelo, preco, cor)
        self.tipo = tipo
        self.milh_toques = milh_toques