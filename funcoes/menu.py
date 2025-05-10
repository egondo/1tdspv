def menu() -> int:
    opcao = -1
    while opcao != 5:
        print('1) Converta a frase para maiúscula')
        print('2) Converta a frase para minúscula')
        print('3) Substitua a letra a pela letra o')
        print('4) Conte a quantidade de vogais')
        print('5) Sair')
    opcao = int(input("Escolha: "))


texto = input("Digite uma frase:")
opcao = menu()
if opcao == 1:
    print(frase.upper())
elif opcao == 2:
    print(frase.lower())
elif opcao == 3:
    print(frase.replace('a', 'o'))
elif opcao == 4:
    print("Fazer como exercicio!")
elif opcao != 5:
    print("Opção inválida!")