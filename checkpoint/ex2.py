#scot/tiger, spock/ncc1701 e walt/disney

login = input("Login: ")
senha = input("senha: ")

if (login == "scot" and senha == 'tiger') or (login == "spock" and senha == "ncc171") or (login == 'walt' and senha == "disney"):
    print("Usuário autenticado com sucesso!")
else:
    print("Nome/senha de usuário inválido.")