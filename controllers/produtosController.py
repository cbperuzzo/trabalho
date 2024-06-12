from modelo.produtos.lista_produtos import PRODUCT_LIST, CATEGORIAS

MENU_OPTIONS = {
    1: show_products,
    2: show_category_products,
    3: search_product_by_name,
    4: show_cart,
    5: show_purchase_historic
}

def init_menu(global_vars: Dict[str,str or bool]):
    while True:
        print('Menu')
        print('1 - Ver todos os produtos')
        print('2 - Ver produtos por categoria')
        print('3 - Pesquisar produto pelo nome')
        print('4 - Visualizar carrinho')
        print('5 - Ver histórico de compras')
        if global_vars['user'].admin:
            print('Painel de admin')
            print('6 - Cadastrar novo Produto')
            print('7 - Mostrar todo o histórico de compras')
            print('8 - Pesquisar histórico de compras de um cliente')

        menu_selector = input().strip()

        if not menu_selector.isnumeric() or menu_selector < 1 or menu_selector > 5:
            print('Esta opção não existe, tente novamente.')
            continue

def show_products(category: str = 'all'):
    for produto in PRODUCT_LIST:
        produto.show_info()
    print('Digite o número do produto e a quantidade desejada para adicionar ao carrinho')



def show_category_products():
    while True:
        print('Deseja ver os produtos de qual categoria? ')
        categoria = input()
        if categoria not in CATEGORIAS:
            print('Categoria não encontrada.')
            print('Voltar - VOL')
            print('Tentar novamente - Any')

            opcao = input().strip().upper()

            if opcao == 'VOL':
                break
            else: 
                continue

