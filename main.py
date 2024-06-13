from controllers.userController import global_vars , indexUser
from controllers.menuController import init_menu

# Inicia a aplicação, fazendo o usuário se registrar ou logar
indexUser()

# print(f'{global_vars['user'].nome} é {'admin' if global_vars['user'].admin else 'um usuário normal'}')

# Inicia o menu da aplicação, onde o usuário escolhe o que fazer
init_menu(global_vars)

