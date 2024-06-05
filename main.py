from controllers.userController import global_vars , indexUser

# Inicia a aplicação, fazendo o usuário se registrar ou logar
indexUser()

print(f'{global_vars['curuser']} é {'admin' if global_vars['admin'] else 'um usuário normal'}')