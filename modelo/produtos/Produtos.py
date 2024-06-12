from utils.text import print_line
from modelo.produtos.lista_produtos import product_list, CATEGORIAS

class Produto:
    def __init__(
        self,
        id_num: int, #! talvez esse atributo não seja necessário
        modelo: str, 
        marca: str, 
        preco: float, 
        cor: str
        ):
        
        self.id_num = id_num
        self.modelo = modelo
        self.marca = marca
        self.preco = preco
        self.cor = cor


    def save(self):
        raise NotImplementedError()

    def show_info(self):
        print(f'{self.id_num}) {self.preco}: {self.modelo} | {self.marca}')
        print(f'Cor: {self.cor}')

    def show_formated_info(self):
        print_line(50)
        self.show_info()
        print_line(50)
    
    @staticmethod
    def get_all():
        return product_list

    @staticmethod
    def show_all():
        for produto in product_list:
            produto.show_info()
    
    @staticmethod
    def get_by_category(category: str):
        produtos = []
        for produto in product_list:
            if produto.categoria == category:
                produtos.append(produto)

        return produtos
    
    @staticmethod
    def show_by_category(category: str):
        produtos = Produto.get_by_category(category)
        for produto in produtos:
            produto.show_info()

class Mouse(Produto):
    def __init__(
        self, 
        id_num: int,
        modelo: str, 
        preco: float, 
        cor: str, 
        sensibilidade_dpi: int,
        tamanho_cm: float
        ):

        super().__init__(id_num, modelo, preco, cor)
        self.sensibilidade_dpi = sensibilidade_dpi
        self.tamanho_cm = tamanho_cm
        self.categoria = 'mouse'

    def save(self):
        pass

class Teclado(Produto):
    def __init__(
        self,
        id_num: int,
        modelo: str,
        preco: float,
        cor: str, 
        tipo: 'mecânico' or 'membrana',
        milh_toques: int
        ):

        super().__init__(id_num, modelo, preco, cor)
        self.tipo = tipo
        self.milh_toques = milh_toques
        self.categoria = 'teclado'

    def save(self):
        pass

class Monitor(Produto):
    def __init__(
        self, 
        id_num: int,
        modelo: str, 
        preco: float, 
        cor: str, 
        polegadas: float, 
        frequencia_hz: float
        ):

        super().__init__(id_num, modelo, preco, cor)
        self.polegadas = polegadas
        self.frequencia_hz = frequencia_hz
        self.categoria = 'monitor'

    def save(self):
        pass
