from modelo.produtos.Produtos import Produto,Mouse,Monitor,Teclado
from modelo.produtos.Produtos import CATEGORIAS,product_list
from modelo.stock.StockOps import *
from modelo.user.User import User
from  modelo.erros.Erros import *
from utils.text import isFloatable


def init_menu(global_vars):
    isAdmin = global_vars['user'].admin

    back = False

    while True:
        print('Menu')
        print('0 - logout')
        print('1 - Ver todos os produtos')
        print('2 - Ver produtos por categoria')
        print('3 - Pesquisar produto pelo modelo')
        print('4 - Visualizar carrinho')
        print('5 - Ver histórico de compras')
        if isAdmin:
            print('Painel de admin')
            print('6 - Cadastrar novo Produto')
            print('7 - Mostrar todo o histórico de compras')
            print('8 - ver clientes/histórico do cliente')
            print('9 - adicionar/ver estoque')
            print('10 - editar produtos')
            print('11 - elevar usuário a admin')
            print('12 - histórico de adição ao estoque')
        
        print('F - Fechar o programa')

        option = input().strip()

        if option.upper() == 'F':
            break
        if option == '0':
            back = True
            break
        if menu_option_is_not_valid(option, isAdmin):
            print('Esta opção não existe, tente novamente.')
            continue

        option = int(option)

        APP_FUNCTIONS[option](global_vars['user'])

    return back

def menu_option_is_not_valid(option: str, admin: bool):
    without_permission = not admin and int(option) > 5
    option_out_of_range = not option.isnumeric() or int(option) < 1 or int(option) > 12

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

#* Admin only app functions

def view_users(user):
    if not user.admin:
        print('Não autorizado!')
        return
    allUsrs = User.get_all_users()
    while True:
        for usr in allUsrs:
            print("nome:",usr['username'])
            print("status de admin:",usr['admin'])
            print("----------------------------------")
        print("[nome do cliente] -> ver histórico do cliente")
        print("[enter] (vazio) -> voltar")

        res = input("")
        if res =='':
            break
        index = User.find_user_in_database(res)
        usrinfo = allUsrs[index]
        tusr = User(usrinfo['username'],usrinfo["password"],usrinfo["admin"])
        print("-----------------")
        print(tusr.nome,":")
        print("-")
        tusr.show_own_purchase_historic()
        input("qualquer coisa para continuar")
        print("-")
def register_product(user): #model save
    if not user.admin:
        print('Não autorizado!')
        return
    while True:
        cat = input("qual categoria ?")
        if cat not in CATEGORIAS:
            print("categoria inválida")
            continue

        print(f'Categoria {cat.upper()}')
        marca = input("marca:").strip()
        modelo = input("modelo").strip()
        estoque = input("estoque inicial:").strip()
        preco = input("preço:").strip()
        cor = input("cor:").strip()
        if not (isFloatable(preco) and estoque.isnumeric()):
            print("preço e estoque devem ser números")
            continue

        preco = float(preco)
        estoque = int(estoque)

        nnum = len(product_list)

        if cat == 'monitor':
            hz = input("frequência em hz:").strip()
            polegadas = input("polegadas:").strip()
            if not (isFloatable(hz) and isFloatable(polegadas)):
                print("frquẽncia e polegadas devem ser números")
                continue
            hz = float(hz)
            polegadas = float(polegadas)

            nmoni = Monitor(nnum,estoque,cat,modelo,marca,preco,cor,polegadas,hz)
            nmoni.save()
            break

        elif cat =='mouse':
            dpi = input("DPI:").strip()
            tamanho = input("tamanho CM:").strip()
            if not (dpi.isnumeric() and isFloatable(tamanho)):
                print("dpi e tamanho devem ser números")
                continue
            dpi = int(dpi)
            tamanho = float(tamanho)

            nmouse = Mouse(nnum,estoque,cat,modelo,marca,preco,cor,dpi,tamanho)
            nmouse.save()
            break

        else:  # cat == teclado
            tipo = input("tipo: 0 - membrana 1 - mecânico").strip()
            mil_toques = input("durabilidade (milhões de toques) :").strip()
            if not(mil_toques.isnumeric() and tipo in ['0', '1']):
                continue
            tipos = ['membrana','mecânico']
            tipo = tipos[int(tipo)]
            mil_toques = int(mil_toques)

            ntecl = Teclado(nnum,estoque,cat,modelo,marca,preco,cor,tipo,mil_toques)
            ntecl.save()
            break

def show_purchase_historic(user):
    if not user.admin:
        print('Não autorizado!')
        return
    
    User.show_purchase_historic()
    print('Digite qualquer coisa para voltar')
    input()

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

# * new admin only functions
def stock_ops(user):
    if not user.admin:
        print('Não autorizado!')
        return
    while True:
        Produto.show_all_with_stock()

        print("[id oo produto] -> seleciona produto")
        print("[enter] (vazio) -> voltar")

        res = input("")
        if res == '':
            break
        try:
            res = int(res.strip())
        except:
            print("valor inválido")
            continue
        if not (res>=0 and res<len(product_list)):
            continue

        val = input("quantos produtos devem ser adicionados:")
        try:
            val = int(val.strip())
        except:
            print("valor inválido")
            continue

        cst = input("custo da operação:")
        try:
            cst = float(cst.strip())
        except:
            print("valor inválido")
            continue

        product_list[res].estoque += val
        Produto.update_products_db()

        new_operaion(res,val,cst)
        print("operação realizada com sucesso")
        print("- \n digite qualquer coisa para continuar")


def update_product(user):
    if not user.admin:
        print('Não autorizado!')
        return
    while True:
        Produto.show_all()

        print("[id oo produto] -> seleciona produto")
        print("[enter] (vazio) -> voltar")

        res = input(":")
        if res == '':
            break
        try:
            res = int(res.strip())
        except:
            print("valor inválido")
            continue
        if not (res >= 0 and res < len(product_list)):
            continue
        pro = product_list[res]
        pro.show_info()
        print("---------------------")
        print("!!! oque for digitado substituirá a iformação antiga !!!")
        while True:
            nmodelo = input("modelo:").strip()
            nmarca = input("marca:").strip()
            preco = input("preço:").strip()
            cor = input("cor:").strip()
            if not (isFloatable(preco)):
                print("preço tem que ser um float")
                continue
            preco = float(preco)

            if pro.categoria == "mouse":
                ndpi = input("dpi:").strip()
                ntam = input("tamanho:").strip()
                if not (isFloatable(ntam) and ndpi.isnumeric()):
                    print("tamanho e dpi devem ser valores numéricos")
                    continue
                ndpi = int(ndpi)
                ntam = float(ntam)

                nmous= Mouse(pro.id_num, pro.estoque, pro.categoria, nmodelo, nmarca, preco, cor,ndpi,ntam)
                product_list[res] = nmous
                Produto.update_products_db()

            if pro.categoria == "teclado":
                tipo = input("tipo: 0 - membrana 1 - mecânico:").strip()
                milt = input("durabilidade (milhões de toque)").strip()
                if not (tipo in ['1','0'] and milt.isnumeric()):
                    print("tipo inválido ou durabilidade não é um valor inteiro")
                    continue
                tipos = ['membrana', 'mecânico']
                tipo = tipos[int(tipo)]
                milt = int(milt)

                ntec = Teclado(pro.id_num, pro.estoque, pro.categoria, nmodelo, nmarca, preco, cor, tipo, milt)
                product_list[res] = ntec
                Produto.update_products_db()

            if pro.categoria == "monitor":
                hz = input("frequência(hz)").strip()
                pol = input("polegadas").strip()
                if not(isFloatable(hz) and isFloatable(pol)):
                    print("freqência e ou polegadas não são valores númericos")
                    continue
                hz = float(hz)
                pol = float(pol)

                nmon = Monitor(pro.id_num,pro.estoque,pro.categoria,nmodelo,nmarca,preco,cor,pol,hz)
                product_list[res] = nmon
                Produto.update_products_db()
            break


def new_admin(user):
    if not user.admin:
        print('Não autorizado!')
        return
    while True:
        print("usuários não admins:")
        allUser = User.get_all_users()
        for item  in allUser:
            if not item['admin']:
                print("nome:",item['username'])
                print("status de admin: False")
            print("--------------------------")

        print("[nome do usuário] -> promove o usuário a admin")
        print("[enter] (vazio) -> voltar")
        r = input("").strip().upper()
        index = User.find_user_in_database(r)
        if r == "":
            break
        if index == -1:
            print("usuário não encontrado")
            continue
        usinf = allUser[index]
        print("---------------")
        print("o usuário",usinf["username"],"será elevado a admin")
        r = input("para confirmar digite: CONFIRMAR")
        if r != "CONFIRMAR":
            print("operação cancelada")
            input("- \nqualquer coisa para continuar")
        else:
            el = User(usinf["username"],usinf["password"],usinf["admin"])
            el.ascend()
            print("usuário elevado ")
            input("- \nqualquer coisa para continuar")
def view_stock_ops(user):
    if not user.admin:
        print('Não autorizado!')
        return
    lis = get_ops_list()
    for item in lis:
        print(product_list[item["prod_id"]].marca,"|",product_list[item["prod_id"]].modelo)
        print("quantidade comprada:",item["amount"])
        print("valor total pago:",item["cost"])
        print(item["datetime"])
        print("----------------------------------------------------")
    print("total gasto em todas as operações:",get_total_cost())
    print("- - - ")
    input("- \nqualquer coisa para voltar")

APP_FUNCTIONS = {
    1: show_all_products,
    2: show_category_products,
    3: search_product_by_model,
    4: show_cart,
    5: show_user_purchase_historic,
    6: register_product,
    7: show_purchase_historic,
    8: view_users,
    9: stock_ops,
    10: update_product,
    11: new_admin,
    12: view_stock_ops
}