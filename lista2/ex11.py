valor_produto = float(input("Valor do produto: "))
opcao = int(input("Opção de pagamento: "))

match opcao:
    case 1:
        desconto = valor_produto * 0.1
        valor = valor_produto - desconto
        print(f"Desconto {desconto} novo valor {valor}")
    case 2:
        desconto = valor_produto * 0.05
        valor = valor_produto - desconto
        print(f"Desconto {desconto} novo valor {valor}")
    case 3:
        parcela = valor_produto / 2
        print(f"Pagamento em 2 parcelas sem juros de {parcela}")
    case 4:
        valor = valor_produto * 1.07
        parcela = valor / 4
        print(f"Valor a ser pago: {valor} em 4x de {parcela}")