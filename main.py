from controllers.userController import global_vars , indexUser
from controllers.menuController import init_menu
mm = True
while mm:
    indexUser()
    mm = init_menu(global_vars)