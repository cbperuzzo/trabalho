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

        all_users = User.get_all_users()

        if User.find_user_in_database(user_login['username']) != -1:
            raise ValueError('Nome de usuário já está sendo usado.')
        
        all_users.append(user_login)
        
        with open('data_base/usuarios.json', 'w') as write_file:
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
        with open('data_base/usuarios.json', 'r') as read_file:
            all_users = json.load(read_file)
        
        return all_users