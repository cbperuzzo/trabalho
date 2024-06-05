from modelo.user.User import User

global_vars = {
    'curuser' : "",  #não poder usuário com nome vazio, não podem usuários com o mesmo nome
    'admin' : False
}

def indexUser(): #gera maneiras de acessar a aplicação, associando um valor válido a curuser e definindo admin como true ou false
    while True:
        print("Registrar [reg] - Login [log]")
        res = input().upper().strip()

        if(res == "REG"):
            if register():
                break
        elif(res == "LOG"):
            if log():
                break
        else:
            "Ação não encontrada, tente novamente"

def log():
    while True:
        nome = input("nome: ")
        senha = input("senha: ")
        try:
            admin = User.verify_login(nome,senha)
            
            logDone(nome, admin)
            return True
        except ValueError as err:
            print("algo deu errado:",err)
            res = input("voltar [vol] - tentar denovo [any]")
            if res.strip().upper() == "VOL":
                return False

def register():
    while True:
        nome = input("nome:")
        senha = input("senha:")
        try:
            nuser = User(nome, senha)
            nuser.save()
            logDone(nuser.nome, nuser.admin)
            return True
        except ValueError as err:
            print("Algo deu errado:",err)
            res = input("voltar [vol] - tentar denovo [any]")
            if res.strip().upper() == "VOL":
                return False

def logDone(nome: str, admin: bool) -> None:
    global_vars['curuser'] = nome
    global_vars['admin'] = admin
