curuser = ""  #não poder usuário com nome vazio
admin = False

usuarios = list()

def index():
    while True:
        print("registrar [reg] - login [log]")
        res = input().upper().strip()

        if(res == "REG"):
            register()
        elif(res == "LOG"):
            log()
        else:
            "ação não encontrada, tente novamente"

def log():
    find = False
    while True:
        nome = input("nome:").upper().strip()
        senha = input("senha:")

        for i in range(0,len(usuarios),1):
            if nome == (usuarios[i].nome).upper().strip():
                if senha == usuarios[i].senha:
                    curuser = usuarios[i].nome
                    admin = usuarios[i].admin
                    find = True
        if find:
            break
        else:
            print("usuário ou senha inválido")
index()

