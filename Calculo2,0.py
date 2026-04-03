pedpequeno = 300
pedmedio = 800
pedmaior = 801


def login():
    nome = input("Seu nome: ")
    return nome


def pedidos():
    somapedidos = 0
    numerodepedidos = 0

    print("\nDigite os pedidos (digite '0' para parar)\n")

    while True:
        valor = float(input(f"Valor do pedido {numerodepedidos + 1}: "))

        if valor == 0:
            break

        if valor < 0:
            print("Valor inválido! Tente novamente.")
            continue

        somapedidos += valor
        numerodepedidos += 1

    if numerodepedidos == 0:
        print("Nenhum pedido foi inserido.\n")
        return

    total = somapedidos
    comdesconto = "Não"

    # descontos
    desconto10 = somapedidos * 0.10
    desconto20 = somapedidos * 0.20

    valor_com_10 = somapedidos - desconto10
    valor_com_20 = somapedidos - desconto20

    # classificação
    if somapedidos <= pedpequeno:
        print("Seu pedido é pequeno!\n")
        tipodepedido = "pequeno"

    elif pedpequeno < somapedidos <= pedmedio:
        print("Seu pedido é médio!\n")
        tipodepedido = "médio"

        if somapedidos > 500:
            comdesconto = "Sim"
            total = valor_com_10
            print("Você recebeu 10% de desconto!")
            print(f"{somapedidos} - {desconto10} = {valor_com_10}\n")

    elif somapedidos >= pedmaior:
        print("Seu pedido é grande!\n")
        tipodepedido = "grande"

        if somapedidos >= 1000:
            comdesconto = "Sim"
            total = valor_com_20
            print("Você recebeu 20% de desconto!")
            print(f"{somapedidos} - {desconto20} = {valor_com_20}\n")

    print(f"Total sem desconto: {somapedidos}\n")

    Pessoadados = {
        "quantidade de pedidos": numerodepedidos,
        "tipo de pedido": tipodepedido,
        "valor original": somapedidos,
        "desconto aplicado": comdesconto,
        "valor final": total,
    }

    print("Resultados:\n")
    print(Pessoadados, "\n")



while True:

    print("\nSeja bem-vindo(a) à nossa loja!")
    print("\nFaça Login:")
    nome = login()

    print(f"\nLogin feito com sucesso! Bem-vindo, {nome}!")
    print("--------------------------------------------------")

    pedidos()

    print("Agradecemos pela confiança, volte sempre!\n")

    sair = input("Deseja sair? (s/n): ").lower()
    if sair == "s":
        print("Encerrando sistema...")
        break
