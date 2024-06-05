import json
from typing import List, Dict

class User:
    def __init__(self, nome: str, senha: str, admin: bool = False):
        if senha == '':
            raise ValueError('Senha vazia.')
        
        self.nome = nome
        self.senha = senha
        self.admin = admin
        

    def save(self) -> None:
        user_login = {
            'username': self.nome,
            'password': self.senha,
            'admin': False
        }

        with open('data_base/usuarios.json', 'r') as read_file:
            all_users = json.load(read_file)
        
        if self.user_in_list(all_users, user_login):
            raise ValueError('Nome de usuário já está sendo usado.')
        
        all_users.append(user_login)
        
        with open('data_base/usuarios.json', 'w') as write_file:
            json.dump(all_users, write_file)

    def user_in_list(self, user_list: List[Dict[str, str]], user_login) -> bool:
        for registered_user in user_list:
            if registered_user['username'] == user_login['username']:
                return True
        
        return False

    @staticmethod
    def getAllUsers():
        pass

    @staticmethod
    def getWhereUserName(str):
        pass