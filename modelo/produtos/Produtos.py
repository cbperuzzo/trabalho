from utils.text import print_line
import json

PRODUCT_DB_PATH = 'data_base/produtos.json'
CATEGORIAS = [
    'monitor',
    'mouse',
    'teclado'
]

class Produto:
    def __init__(
        self,
        id_num: int,
        categoria: str,
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
        print(f'{self.id_num} - {self.marca} | {self.modelo}')
        print(f'R${self.preco:.2f}')
        print(f'Cor: {self.cor}')
    

    @staticmethod
    def show_all():
        print_line(40)
        for produto in product_list:
            produto.show_info()
            print_line(40)
    
    @staticmethod
    def show_by_category(category: str):
        if category not in CATEGORIAS:
            raise ValueError('Categoria não encontrada')
        for produto in product_list:
            if produto.categoria == category:
                produto.show_info()
    
    @staticmethod
    def get_products_as_objects():
        all_products = []
        with open(PRODUCT_DB_PATH, 'r') as read_file:
            products_json = json.load(read_file)
            for product_dict in products_json:

                id_num = products_json.index(product_dict)
                categoria = product_dict['categoria']
                modelo = product_dict['modelo']
                marca = product_dict['marca']
                preco = float(product_dict['preco'])
                cor = product_dict['cor']
                
                product_obj = None

                if categoria == 'mouse':
                    product_obj = Mouse(
                        id_num, categoria, modelo, marca, preco, cor, 
                        product_dict['sensibilidade_dpi'], 
                        float(product_dict['tamanho_cm'])
                    )
                    
                elif categoria == 'teclado':
                    product_obj = Teclado(
                        id_num, categoria, modelo, marca,  preco, cor, 
                        product_dict['tipo'], 
                        int(product_dict['milh_toques'])
                    )

                elif categoria == 'monitor':
                    product_obj = Monitor(
                        id_num, categoria, modelo, marca, preco, cor, 
                        float(product_dict['polegadas']), 
                        float(product_dict['frequencia_hz'])
                    )
                
                all_products.append(product_obj)
        
        return all_products

class Mouse(Produto):
    def __init__(
        self, 
        id_num: int,
        categoria: str,
        modelo: str, 
        marca: str,
        preco: float, 
        cor: str, 
        sensibilidade_dpi: int,
        tamanho_cm: float
        ):

        super().__init__(id_num, categoria, modelo, marca, preco, cor)
        self.sensibilidade_dpi = sensibilidade_dpi
        self.tamanho_cm = tamanho_cm
        self.categoria = 'mouse'
    
    def show_info(self):
        print(f'{self.id_num} - Mouse {self.marca} | {self.modelo}')
        print(f'R${self.preco:.2f}')
        print(f'Cor: {self.cor}')
        print(f'DPI: {self.sensibilidade_dpi}')
        print(f'Tamanho: {self.tamanho_cm}cm')

    def save(self):
        raise NotImplementedError()

class Teclado(Produto):
    def __init__(
        self,
        id_num: int,
        categoria: str,
        modelo: str,
        marca: str,
        preco: float,
        cor: str, 
        tipo: 'mecânico' or 'membrana',
        milh_toques: int
        ):

        super().__init__(id_num, categoria, modelo, marca, preco, cor)
        self.tipo = tipo
        self.milh_toques = milh_toques
        self.categoria = 'teclado'

    def save(self):
        raise NotImplementedError()

class Monitor(Produto):
    def __init__(
        self, 
        id_num: int,
        categoria: str,
        modelo: str, 
        marca: str,
        preco: float, 
        cor: str, 
        polegadas: float, 
        frequencia_hz: float
        ):

        super().__init__(id_num, categoria, modelo, marca, preco, cor)
        self.polegadas = polegadas
        self.frequencia_hz = frequencia_hz
        self.categoria = 'monitor'

    def save(self):
        raise NotImplementedError()


product_list = Produto.get_products_as_objects()