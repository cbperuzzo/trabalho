curuser = ""  #não poder usuário com nome vazio, não podem usuários com o mesmo nome
admin = False

usuarios = list()

def index():
    while True:
        print("registrar [reg] - login [log]")
        res = input().upper().strip()

        if(res == "REG"):
            register()
            break
        elif(res == "LOG"):
            log()
            break
        else:
            "ação não encontrada, tente novamente"

def log():  #esse código ta muito feio e ruim de entender, dps tem que mudar
    vol = False
    loop = True
    while loop:
        nome = input("nome:").upper().strip()
        senha = input("senha:")

        for i in range(0,len(usuarios),1):
            if nome == (usuarios[i].nome).upper().strip():
                if senha == usuarios[i].senha:
                    curuser = usuarios[i].nome
                    admin = usuarios[i].admin
                    loop = False
                    break
        if loop:
            print("usuário ou senha inválidos")
            res = input("tentar novamente [qualquer coisa]\nvoltar[vol]")
            if res.upper().strip() == "VOL":
                loop = False
                vol = True
    if vol:
        index()
def register():
    while True:
        nome = input("nome:")
        valid = True
        for usr in usuarios:
            if nome.upper().strip() == (usr.nome).upper().strip():
                valid = False
        if valid:
            senha = print("nome disponível\nsenha:")
            admin = False
            curuser = nome
            # cria um objeto novo e salva ele no "banco de dados" (ainda não da pra fazer)
        else:
            print("nome de usuário ja existe, tente outro")
