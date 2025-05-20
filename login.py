import getpass

while True:
    nome_usuario = input("Digite seu nome de usuário: ")
    
    # Solicita a senha de forma oculta (não visível ao digitar)
    senha = getpass.getpass("Digite sua senha: ")

    # Verificação do nome de usuário
    if len(nome_usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        continue

    # Verificação da senha
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    # Se passar por todas as verificações
    print("Cadastro realizado com sucesso!")
    break
