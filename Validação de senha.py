usuario_certo = "admin1" # o usuário deverá digitar o nome de usuário "admin1" corretamente para dar certo
senha_certa = "23046" # o usuário deve digitar a senha "23046" corretamente para dar certo

while True: # enquanto for verdadeiro
    usuario = input("Nome de usuário: ") # deverá digitar o nome de usuário corretamente
    senha = input("Senha: ") # deverá digitar a senha corretamente

    if usuario == usuario_certo and senha == senha_certa: # se o usuário digitar ambos corretamente, irá aparecer a mensagem abaixo
        print("O login digitado foi bem-sucedido!") # se estiver correto
        break # se o usuario tiver digitado o login corretamente o programa deve parar
    else: # caso contrário
        print("Usuário ou senha incorreto! Tente novamente.") # o usuário deverá tentar novamente