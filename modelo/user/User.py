import json
from typing import List, Dict
from modelo.produtos.Produtos import Produto
from utils.text import print_line, get_current_formated_date_time

VENDAS_DB_PATH = 'data_base/vendas.json'
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
            if registered_user['username'].strip().upper() == username.strip().upper():
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
    
    def add_product_to_cart(self, product, quantity: int):
        product_already_in_cart = False
        
        for item in self.carrinho:
            if item[0] == product:
                product_already_in_cart = True
                product_cart_index = self.carrinho.index(item)
                # quantity += item[1]

        Produto.check_stock(product, quantity)

        if product_already_in_cart:
            self.carrinho[product_cart_index][1] += quantity
        else:
            self.carrinho.append([product, quantity])
        
        print(f'{quantity} {product.categoria}(s) {product.modelo} adicionados ao carrinho!')
    
    def buy(self):
        if len(self.carrinho) == 0:
            return
        
        with open(VENDAS_DB_PATH, 'r') as read_file:
            vendas_dict = json.load(read_file)
        
        items = []
        for item in self.carrinho:
            items.append([item[0].modelo, item[1]])
        
        nova_venda = {
            "data": get_current_formated_date_time(),
            "usuario": self.nome,
            "valor_total": round(self.get_cart_total(), 2),
            "produtos_comprados": items
        }

        vendas_dict["receita"] += nova_venda['valor_total']
        vendas_dict["historico"].append(nova_venda)

        with open(VENDAS_DB_PATH, 'w') as write_file:
            json.dump(vendas_dict, write_file)
        
        self.carrinho = []
        print("Compra finalizada com sucesso!")
    
    def get_cart_total(self):
        total = 0

        for item in self.carrinho:
            total += item[1] * item[0].preco
        
        return total
    
    def show_cart(self):
        total = self.get_cart_total()
        if total == 0:
            print('Nenhum produto no carrinho...')
            return

        print(f'Carrinho de {self.nome}')

        cabecalho = f'| {"Num, Marca e modelo":<35}|{"Preço":^10}|{"Qtd.":^6}| Preço total'
        print(cabecalho)

        print_line(len(cabecalho))

        for item in self.carrinho:
            formated_string = f'| {str(item[0].id_num) + " - " + item[0].categoria.title() + " " + item[0].modelo:<35}|{item[0].preco:^10.2f}|{item[1]:^6}| R${item[0].preco * item[1]:.2f}'
            print(formated_string)

        print_line(len(cabecalho))
        
        print(f'Total: R${total:.2f}')

    def remove_from_cart(self, product_id: int, quantity: int) -> None:
        for item in self.carrinho:
            product = item[0]
            if product.id_num == product_id:
                if quantity >= item[1]:
                    self.carrinho.remove(item)
                elif quantity >= 0:
                    item[1] -= quantity
    
    def show_own_purchase_historic(self) -> None:
        own_purchase_historic = self.get_own_purchase_historic()

        if len(own_purchase_historic) == 0:
            print('Nenhuma compra relizada.')
            return
        
        print_line(40)
        for purchase in own_purchase_historic:
            print(f'Data e hora: {purchase["data"]}')
            print(f'Valor total: R${purchase["valor_total"]:.2f}')
            print(f'Produtos comprados:')
            for produto in purchase['produtos_comprados']:
                print(f'\t{produto[1]} {produto[0]}(s)')
            print_line(40)
    
    def get_own_purchase_historic(self) -> Dict['str', Dict]:
        purchase_historic = User.get_purchase_historic()

        own_purchase_historic = []
        for purchase in purchase_historic['historico']:
            if purchase['usuario'] == self.nome:
                own_purchase_historic.append(purchase)
        
        return own_purchase_historic

    @staticmethod
    def get_purchase_historic():
        with open(VENDAS_DB_PATH, 'r') as read_file:
            purchase_historic = json.load(read_file)
        
        return purchase_historic

    @staticmethod
    def show_purchase_historic():
        purchase_historic = User.get_purchase_historic()
        for purchase in purchase_historic['historico']:
            print(f'Usuário: {purchase["usuario"]}')
            print(f'Data e hora: {purchase["data"]}')
            print(f'Valor total: R${purchase["valor_total"]:.2f}')
            print(f'Produtos comprados:')
            for produto in purchase['produtos_comprados']:
                print(f'\t{produto[1]} {produto[0]}(s)')
            print_line(40)
        print(f'Receita total: R${purchase_historic["receita"]}')
