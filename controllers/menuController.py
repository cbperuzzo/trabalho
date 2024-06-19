from modelo.produtos.Produtos import Produto,Mouse,Monitor,Teclado
from modelo.produtos.Produtos import CATEGORIAS,product_list
from modelo.user.User import User
from  modelo.erros.Erros import *
from utils.text import print_line, isFloatable


def init_menu(global_vars):
    isAdmin = global_vars['user'].admin

    while True:
        print('Menu')
        print('0 - logout') #novo
        print('1 - Ver todos os produtos')
        print('2 - Ver produtos por categoria')
        print('3 - Pesquisar produto pelo modelo')
        print('4 - Visualizar carrinho')
        print('5 - Ver histórico de compras')
        if isAdmin:
            print('Painel de admin')
            print('6 - Cadastrar novo Produto')
            print('7 - Mostrar todo o histórico de compras')
            print('8 - ver clientes') #antes era pesquisar histórico de um cliente
        
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
    without_permission = not admin and int(option) > 5
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

def search_product_by_model(user):
    while True:
        print('Digite o nome de algum produto para pesquisá-lo')
        search = input().strip()

        try:
            Produto.show_by_model(search)
        except ModelNotFoundError as e:
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

def show_cart(user):
    while True:
        user.show_cart()
        print('Voltar - VOL')
        print('Finalizar compra - COM')
        print('Remover item do carrinho - REM')
        opcao = input().strip().upper()

        if opcao == 'VOL':
            break
        elif opcao == 'COM':
            Produto.decrease_products_stock(user.carrinho)
            user.buy()
            break
        elif opcao == 'REM':
            [product_id, quantity] = ask_user_for_product_and_quantity('rem')

            if product_id == None:
                break

            user.remove_from_cart(product_id, quantity)

def show_user_purchase_historic(user):
    user.show_own_purchase_historic()
    print('Digite qualquer coisa para voltar')
    input()

def logout(user):
    pass

#* Admin only app functions

def register_product(user): #model save
    if not user.admin:
        print('Não autorizado!')
        return
    cat = input("qual categoria ?")
    if cat not in CATEGORIAS:
        raise CategoryNotFoundError(cat)

    print(f'Categoria {cat.upper()}')
    marca = input("marca:").strip()
    modelo = input("modelo").strip()
    estoque = input("estoque inicial:").strip()
    preco = input("preço:").strip()
    cor = input("cor:").strip()
    if not (isFloatable(preco) and estoque.isnumeric()):
        raise InvalidInput
    preco = float(preco)
    estoque = int(estoque)

    nnum = len(product_list)

    if cat == 'monitor':
        hz = input("frequência em hz:").strip()
        polegadas = input("polegadas:").strip()
        if not (isFloatable(hz) and isFloatable(polegadas)):
            raise InvalidInput
        hz = float(hz)
        polegadas = float(polegadas)

        nmoni = Monitor(nnum,estoque,cat,modelo,marca,preco,cor,polegadas,hz)
        nmoni.save()

    elif cat =='mouse':
        dpi = input("DPI:").strip()
        tamanho = input("tamanho CM:").strip()
        if not (dpi.isnumeric() and isFloatable(tamanho)):
            raise InvalidInput
        dpi = int(dpi)
        tamanho = float(tamanho)

        nmouse = Mouse(nnum,estoque,cat,modelo,marca,preco,cor,dpi,tamanho)
        nmouse.save()

    else:  # cat == teclado
        tipo = input("tipo: 0 - membrana 1 - mecânico").strip()
        mil_toques = input("durabilidade (milhões de toques) :").strip()
        if not(mil_toques.isnumeric() and tipo in ['0', '1']):
            raise InvalidInput
        tipos = ['membrana','mecânico']
        tipo = tipos[int(tipo)]
        mil_toques = int(mil_toques)

        ntecl = Teclado(nnum,estoque,cat,modelo,marca,preco,cor,tipo,mil_toques)
        ntecl.save()

def show_purchase_historic(user):
    if not user.admin:
        print('Não autorizado!')
        return
    
    User.show_purchase_historic()
    print('Digite qualquer coisa para voltar')
    input()

def search_user_purchase_historic(user):
    if not user.admin:
        print('Não autorizado!')
        return
    
    raise NotImplementedError()

#* App auxilliary functions

def start_shopping(user):
    while True:
        [product_id, quantity] = ask_user_for_product_and_quantity()

        if product_id == None:
            break
        
        try:
            product = Produto.get_product_by_id(product_id)
            user.add_product_to_cart(product, quantity)
            
        except ProductNotFoundError as e:
            print('Erro:', e)
        except InsufficientStockError as e:
            print('Erro:', e)
        
def ask_user_for_product_and_quantity(mode='add'):
    if mode == 'add':
        print('Digite o número do produto e a quantidade desejada para adicionar ao carrinho')
    elif mode == 'rem':
        print('Digite o número do produto e a quantidade desejada para remover do carrinho')
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
    0: logout,
    1: show_all_products,
    2: show_category_products,
    3: search_product_by_model,
    4: show_cart,
    5: show_user_purchase_historic,
    6: register_product,
    7: show_purchase_historic,
    8: search_user_purchase_historic
}