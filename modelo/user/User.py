import json
from typing import List, Dict
from modelo.erros.Erros import ProductNotFoundError, InsufficientStockError

USERS_DB_PATH = 'data_base/usuarios.json'

class User:
    def __init__(self, nome: str, senha: str, admin: bool = False):
        if senha == '':
            raise ValueError('Senha vazia.')
        
        self.nome = nome
        self.senha = senha
        self.admin = admin
        self.carrinho = []
        

    def save(self) -> None:
        user_login = {
            'username': self.nome,
            'password': self.senha,
            'admin': False
        }

        all_users = User.get_all_users()

        if User.find_user_in_database(user_login['username']) != -1:
            raise ValueError('Nome de usuário já está sendo usado.')
        
        all_users.append(user_login)
        
        with open(USERS_DB_PATH, 'w') as write_file:
            json.dump(all_users, write_file)

    @staticmethod
    def find_user_in_database(username: str) -> int:
        all_users = User.get_all_users()
        
        for registered_user in all_users:
            if registered_user['username'] == username:
                return all_users.index(registered_user)
        
        return -1

    @staticmethod
    def verify_login(username: str, password: str) -> bool:
        all_users = User.get_all_users()

        user_index = User.find_user_in_database(username)
        
        if user_index == -1:
            raise ValueError('Nome de usuário não cadastrado.')
        if all_users[user_index]['password'] != password:
            raise ValueError('Senha incorreta.')
        
        return all_users[user_index]['admin']
        
    @staticmethod
    def get_all_users() -> List[Dict[str, str]]:
        with open(USERS_DB_PATH, 'r') as read_file:
            all_users = json.load(read_file)
        
        return all_users
    
    def add_product_to_cart(self, product_id: int, quantity: int):
        product_index = Product.find_product(product_id)

        if product_index == -1:
            raise ProductNotFoundError(product_id)

        stock = Product.get_stock(product_index)

        if stock < quantity:
            raise InsufficientStockError(stock)

        self.carrinho.append([product_id, quantity])

    def buy():
        raise NotImplementedError()
