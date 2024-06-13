from modelo.produtos.Produtos import Produto
from modelo.user.User import User
from  modelo.erros.Erros import *

def init_menu(global_vars):
    isAdmin = global_vars['user'].admin

    while True:
        print('Menu')
        print('1 - Ver todos os produtos')
        print('2 - Ver produtos por categoria')
        print('3 - Pesquisar produto pelo nome')
        print('4 - Visualizar carrinho')
        print('5 - Ver histórico de compras')
        if isAdmin:
            print('Painel de admin')
            print('6 - Cadastrar novo Produto')
            print('7 - Mostrar todo o histórico de compras')
            print('8 - Pesquisar histórico de compras de um cliente')
        
        print('F - Fechar o programa')

        option = input().strip()

        if option.upper() == 'F':
            break

        if menu_option_is_not_valid(option, isAdmin):
            print('Esta opção não existe, tente novamente.')
            continue

        option = int(option)

        APP_FUNCTIONS[option](global_vars['user'])

def menu_option_is_not_valid(option: str, admin: bool):
    without_permission = not admin and option > 5
    option_out_of_range = not option.isnumeric() or int(option) < 1 or int(option) > 8

    return option_out_of_range or without_permission

#* APP FUNCTIONS

def show_all_products(user):
    Produto.show_all()
    start_shopping(user)

def show_category_products(user):
    while True:
        print('Deseja ver os produtos de qual categoria? ')
        category = input()

        try:
            Produto.show_by_category(category)
        except CategoryNotFoundError as e:
            print('Erro:', e)
            print('Voltar - VOL')
            print('Tentar novamente - Any')
            option = input().strip().upper()

            if option == 'VOL':
                break
            else: 
                continue
        
        
        start_shopping(user)
        break

def search_product_by_name(user):
    raise NotImplementedError()

def show_cart(user):
    raise NotImplementedError()

def show_user_purchase_historic(user):
    raise NotImplementedError()

def register_product(user):
    raise NotImplementedError()

def show_purchase_historic(user):
    raise NotImplementedError()

def search_user_purchase_historic(user):
    raise NotImplementedError()

#* App auxilliary functions

def start_shopping(user):
    while True:
        [product, quantity] = ask_user_for_product_and_quantity()

        if product == None:
            break
        
        try:
            user.add_product_to_cart(product, quantity)
            
        except ProductNotFoundError as e:
            print('Erro:', e)
        except InsufficientStockError as e:
            print('Erro:', e)
        
def ask_user_for_product_and_quantity():
    print('Digite o número do produto e a quantidade desejada para adicionar ao carrinho')
    print('Voltar - VOL')
    entry = input().strip()

    entry = verify_entry(entry)
    
    return entry

def verify_entry(entry):
    if entry.upper() == 'VOL':
        return [None, 0]
    
    entrada = entry.split()
    while True:
        if len(entrada) != 2:
            print('Digite 2 números separados por espaços: o número do produto e a quantidade')
            entrada = input().strip().split()
        elif not entrada[0].isnumeric() or not entrada[1].isnumeric():
            print('As entradas precisam ser números')
            entrada = input().strip().split()
        else:
            break
    
    entrada = [ int(el) for el in entrada ]

    return entrada

APP_FUNCTIONS = {
    1: show_all_products,
    2: show_category_products,
    3: search_product_by_name,
    4: show_cart,
    5: show_user_purchase_historic,
    6: register_product,
    7: show_purchase_historic,
    8: search_user_purchase_historic
}