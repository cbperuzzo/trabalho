from utils.text import print_line
from typing import List
import json
from modelo.erros.Erros import *

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
        estoque: int,
        categoria: str,
        modelo: str, 
        marca: str, 
        preco: float, 
        cor: str
        ):
        self.categoria = categoria
        self.id_num = id_num
        self.estoque = estoque
        self.modelo = modelo
        self.marca = marca
        self.preco = preco
        self.cor = cor

    #WIP
    def save(self):
        for produto in product_list:
            if produto.categoria == self.categoria and produto.modelo == self.modelo:
                raise ValueError('Este produto ja existe')
        product_list.append(self)
        Produto.update_products_db()

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
            raise CategoryNotFoundError(category)
        
        print(f'Categoria {category.upper()}')
        print_line(40)

    
    @staticmethod
    def show_by_model(model: str):
        not_found = True
        print_line(40)
        for produto in product_list:
            if model.upper() in produto.modelo.upper():
                produto.show_info()
                print_line(40)
                not_found = False
        
        if not_found:
            raise ModelNotFoundError(model)
    
    #! O método a seguir precisa ser atualizado ao adicionar novas categorias de produtos
    @staticmethod
    def get_products_as_objects() -> List:
        all_products = []
        with open(PRODUCT_DB_PATH, 'r') as read_file:
            products_json = json.load(read_file)
            for product_dict in products_json:

                id_num = products_json.index(product_dict)
                estoque = product_dict['estoque']
                categoria = product_dict['categoria']
                modelo = product_dict['modelo']
                marca = product_dict['marca']
                preco = float(product_dict['preco'])
                cor = product_dict['cor']
                
                product_obj = None

                if categoria == 'mouse':
                    product_obj = Mouse(
                        id_num, estoque, categoria, modelo, marca, preco, cor, 
                        product_dict['sensibilidade_dpi'], 
                        float(product_dict['tamanho_cm'])
                    )
                    
                elif categoria == 'teclado':
                    product_obj = Teclado(
                        id_num, estoque, categoria, modelo, marca, preco, cor, 
                        product_dict['tipo'], 
                        int(product_dict['milh_toques'])
                    )

                elif categoria == 'monitor':
                    product_obj = Monitor(
                        id_num, estoque, categoria, modelo, marca, preco, cor, 
                        float(product_dict['polegadas']), 
                        float(product_dict['frequencia_hz'])
                    )
                
                all_products.append(product_obj)
        
        return all_products

    @staticmethod
    def get_json_serializable_product_list():
        product_list_json = []
        for produto in product_list:
            product_json = produto.get_json_serializable()
            product_list_json.append(product_json)

        return product_list_json
        
    @staticmethod
    def get_product_by_id(product_id: int) -> int:
        for item in product_list:
            if item.id_num == product_id:
                return item
        
        return None
    
    @staticmethod
    def get_stock(product_index: int) -> int:
        return product_list[product_index].estoque
    
    @staticmethod
    def check_stock(product, quantity: int) -> None:

        if product == None:
            raise ProductNotFoundError(product.id_num)

        if product.estoque < quantity:
            raise InsufficientStockError(product.estoque)
    
    @staticmethod
    def decrease_products_stock(cart):
        for item in cart:
            product_list[product_list.index(item[0])].estoque -= item[1]
        
        Produto.update_products_db()
    @staticmethod
    def stock_operation(val:int):
        pass
        
    @staticmethod
    def update_products_db():
        product_list_json = Produto.get_json_serializable_product_list()
        with open(PRODUCT_DB_PATH, 'w') as write_file:
            json.dump(product_list_json, write_file)

class Mouse(Produto):
    def __init__(
        self, 
        id_num: int,
        estoque: int,
        categoria: str,
        modelo: str, 
        marca: str,
        preco: float, 
        cor: str, 
        sensibilidade_dpi: int,
        tamanho_cm: float
        ):

        super().__init__(id_num, estoque, categoria, modelo, marca, preco, cor)
        self.sensibilidade_dpi = sensibilidade_dpi
        self.tamanho_cm = tamanho_cm
        self.categoria = 'mouse'

    def show_info(self):
        print(f'{self.id_num} - Mouse {self.marca} | {self.modelo}')
        print(f'R${self.preco:.2f}')
        print(f'Cor: {self.cor}')
        print(f'DPI: {self.sensibilidade_dpi}')
        print(f'Tamanho: {self.tamanho_cm}cm')

    def get_json_serializable(self):
        product_json = {
                "estoque":self.estoque,
                "categoria": self.categoria,
                "modelo": self.modelo,
                "marca": self.marca,
                "preco": self.preco,
                "cor": self.cor,
                "sensibilidade_dpi": self.sensibilidade_dpi,
                "tamanho_cm": self.tamanho_cm
            }
        return product_json

class Teclado(Produto):
    def __init__(
        self,
        id_num: int,
        estoque: int,
        categoria: str,
        modelo: str,
        marca: str,
        preco: float,
        cor: str, 
        tipo: 'mecânico' or 'membrana',
        milh_toques: int
        ):

        super().__init__(id_num, estoque, categoria, modelo, marca, preco, cor)
        self.tipo = tipo
        self.milh_toques = milh_toques
        self.categoria = 'teclado'

    def show_info(self):
        print(f'{self.id_num} - Teclado {self.marca} | {self.modelo}')
        print(f'R${self.preco:.2f}')
        print(f'Cor: {self.cor}')
        print(f'Tipo: {self.tipo}')
        print(f'Milhares de toques: {self.milh_toques} mil')

    def get_json_serializable(self):
        product_json = {
                "estoque":self.estoque,
                "categoria": self.categoria,
                "modelo": self.modelo,
                "marca": self.marca,
                "preco": self.preco,
                "cor": self.cor,
                "tipo": self.tipo,
                "milh_toques": self.milh_toques
            }

        return product_json

class Monitor(Produto):
    def __init__(
        self, 
        id_num: int,
        estoque: int,
        categoria: str,
        modelo: str, 
        marca: str,
        preco: float, 
        cor: str, 
        polegadas: float, 
        frequencia_hz: float
        ):

        super().__init__(id_num, estoque, categoria, modelo, marca, preco, cor)
        self.polegadas = polegadas
        self.frequencia_hz = frequencia_hz
        self.categoria = 'monitor'

    def show_info(self):
        print(f'{self.id_num} - Monitor {self.marca} | {self.modelo}')
        print(f'R${self.preco:.2f}')
        print(f'Cor: {self.cor}')
        print(f'Tamanho: {self.polegadas} polegadas')
        print(f'Frequência: {self.frequencia_hz} Hz')

    def get_json_serializable(self):
        product_json = {
                "estoque":self.estoque,
                "categoria": self.categoria,
                "modelo": self.modelo,
                "marca": self.marca,
                "preco": self.preco,
                "cor": self.cor,
                "polegadas": self.polegadas,
                "frequencia_hz": self.frequencia_hz
            }

        return product_json


product_list = Produto.get_products_as_objects()