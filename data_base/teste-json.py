import json

user_data = {
    'username': 'davi',
    'password': '1234'
}

# Primeiro, escreva no arquivo
with open('data_base/usuarios.json', 'w', encoding='utf-8') as user_file:
    json.dump(user_data, user_file, ensure_ascii=False, indent=4)

# Depois, leia o arquivo
with open('data_base/usuarios.json', 'r', encoding='utf-8') as user_file:
    all_users = json.load(user_file)
    print(json.dumps(all_users, indent=4, ensure_ascii=False))