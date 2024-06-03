from Produto import Produto

class Tela(Produto):
    def __init__(
        self, 
        modelo: str, 
        preco: float, 
        cor: str, 
        polegadas: float, 
        frequencia_hz: float
        ):

        super().__init__(modelo, preco, cor)
        self.polegadas = polegadas
        self.frequencia_hz = frequencia_hz

