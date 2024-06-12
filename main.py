from controllers.userController import global_vars , indexUser

# Inicia a aplicação, fazendo o usuário se registrar ou logar
indexUser()

print(f'{global_vars['user'].nome} é {'admin' if global_vars['user'].admin else 'um usuário normal'}')