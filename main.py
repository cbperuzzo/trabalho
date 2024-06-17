from controllers.userController import global_vars , indexUser
from controllers.menuController import init_menu

# Inicia a aplicação, fazendo o usuário se registrar ou logar
indexUser()

# Inicia o menu da aplicação, onde o usuário escolhe o que fazer
init_menu(global_vars)
