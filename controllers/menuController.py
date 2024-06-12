from modelo.produtos.Produtos import Produto

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

        option = input().strip()

        if menu_option_is_not_valid(option, isAdmin):
            print('Esta opção não existe, tente novamente.')
            continue

        APP_FUNCTIONS[option]()

def menu_option_is_not_valid(option: str, admin: bool):
    without_permission = not admin and option > 5
    option_out_of_range = not option.isnumeric() or option < 1 or option > 8

    return option_out_of_range or without_permission

def show_all_products(category: str = 'all'):
    Produto.show_all()
    print('Digite o número do produto e a quantidade desejada para adicionar ao carrinho')


def show_category_products():
    while True:
        print('Deseja ver os produtos de qual categoria? ')
        category = input()

        if category not in CATEGORIAS:
            print('Categoria não encontrada.')
            print('Voltar - VOL')
            print('Tentar novamente - Any')

            option = input().strip().upper()

            if option == 'VOL':
                break
            else: 
                continue
        
        Produto.show_by_category(category)

