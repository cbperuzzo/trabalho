from ..modelo.User import User

curuser = ""  #não poder usuário com nome vazio, não podem usuários com o mesmo nome
admin = False

def indexUser(): #gera maneiras de acessar a aplicação, associando um valor válido a curuser e definindo admin como true ou false
    while True:
        print("registrar [reg] - login [log]")
        res = input().upper().strip()

        if(res == "REG"):
            if register():
                break
        elif(res == "LOG"):
            if log():
                break
        else:
            "ação não encontrada, tente novamente"
    print("--------\nusuário atual: {}\nstatus de admin: {}".format(curuser,admin))

def log():
    while True:
        nome = input("nome:")
        senha = input("senha:")
        try:
            User.verify_loggin(nome,senha)
            nuser = User(nome, senha)
            nuser.save()
            logDone(nuser)
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
            logDone(nuser)
            return True
        except ValueError as err:
            print("algo deu errado:",err)
            res = input("voltar [vol] - tentar denovo [any]")
            if res.strip().upper() == "VOL":
                return False

def logDone(usr: User):
    curuser = usr.nome
    admin = usr.admin


