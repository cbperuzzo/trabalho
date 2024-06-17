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
        
        self.id_num = id_num
        self.estoque = estoque
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
            raise CategoryNotFoundError(category)
        
        print(f'Categoria {category.upper()}')
        print_line(40)
        for produto in product_list:
            if produto.categoria == category:
                produto.show_info()
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
    
    #! Os 2 métodos a seguir precisam ser atualizados ao adicionar novas categorias de produtos
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
        for product in product_list:
            product_json = {
                "estoque":product.estoque,
                "categoria": product.categoria,
                "modelo": product.modelo,
                "marca": product.marca,
                "preco": product.preco,
                "cor": product.cor
            }

            #! Atualizar ao adicionar mais categorias de produtos
            if product.categoria == 'mouse':
                product_json['sensibilidade_dpi'] = product.sensibilidade_dpi
                product_json['tamanho_cm'] = product.tamanho_cm
            elif product.categoria == 'teclado':
                product_json['tipo'] = product.tipo
                product_json['milh_toques'] = product.milh_toques
            elif product.categoria == 'monitor':
                product_json['polegadas'] = product.polegadas
                product_json['frequencia_hz'] = product.frequencia_hz
            
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
            raise ProductNotFoundError(product_id)

        if product.estoque < quantity:
            raise InsufficientStockError(stock)
    
    @staticmethod
    def decrease_products_stock(cart):
        for item in cart:
            product_list[product_list.index(item[0])].estoque -= item[1]
        
        Produto.update_products_db()
        
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

    def save(self):
        raise NotImplementedError()

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

    def save(self):
        raise NotImplementedError()

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

    def save(self):
        raise NotImplementedError()


product_list = Produto.get_products_as_objects()