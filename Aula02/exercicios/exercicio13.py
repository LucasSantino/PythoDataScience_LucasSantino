'''
3) Solicite o nome de usuário e a senha. Permita o acesso apenas quando o usuário 
for "admin" e a senha for "1234".
'''

print("Olá, seja bem vindo!")

try:
    user_name = input("\nInsira o nome de usario: ")
    senha = input("\nInsira uma senha para entrar: ")

    if user_name == "admin" and senha == "1234":
        print("\nUsuario autorizao! Seja bem vindo ao sistema!")
    else:
        print("\nUsuario e senha não identificados! Acesso não autorizado!")

except Exception as erro:
    print("\nOcorreu um erro inesperavel!")

