from ..modelo.User import User

curuser = ""  #não poder usuário com nome vazio, não podem usuários com o mesmo nome
admin = False

usuarios = list() #vai vir do banco de dados

def indexUser(): # essa função gera valores para "curuser" e "admin"
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

def log():
    while True:
        nome = input("nome:").upper().strip()
        senha = input("senha:")

        for i in range(0, len(usuarios), 1):
            if nome == (usuarios[i].nome).upper().strip():
                if senha == usuarios[i].senha:
                    curuser = usuarios[i].nome
                    admin = usuarios[i].admin
                    return True
        print("usuário ou senha inválidos")
        res = input("voltar [vol]\ntentar outro [any]")
        if res.strip().upper() == "VOL":
            return False
def register():
    while True:
        nome = input("nome:")
        valid = (User.getWhereUserName(nome) == "") and (nome != "")
        if valid:
            print("nome valido")
            senha = input("senha:")
            nuser = User(nome,senha)
            nuser.save()
        else:
            print("esse nome ja existe ou é vaziu , tente novamente")
            print("caso deseje voltar ")



