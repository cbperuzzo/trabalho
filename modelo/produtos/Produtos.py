from utils.text import print_line

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

    def show_info(self):
        print(f'{self.preco}: {self.modelo} | {self.marca}')
        print(f'Cor: {self.cor}')

    def show_formated_info(self):
        print_line(50)
        self.show_info()
        print_line(50)
    

    @staticmethod
    def getAll():
        pass
    
    @staticmethod
    def getWhereModelo(str):
        pass

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
    def save(self):
        pass

class Monitor(Produto):
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

    def save(self):
        pass
