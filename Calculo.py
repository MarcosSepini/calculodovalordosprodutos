Pessoadados= []
numero_de_pedidos = 1
pedpequeno = 300
pedmedio = 800
pedmaior = 801

def login ():
    nome = input("Seu nome:")
    Pessoadados.append(nome)

def pedidos ():
    numerodepedidos = int(input("numero de pedidos:"))
    if numerodepedidos == 1 :
        ped1 = float(input("Valor do seu pedido:"))
        somapedidos= ped1
        porcentodedesconto10 = somapedidos *(10/100)
        porcentodedesconto20 = somapedidos *(20/100)
        comdesconto10 = somapedidos - porcentodedesconto10
        comdesconto20 = somapedidos - porcentodedesconto20
        if somapedidos < 300:
            print("Seu pedido é pequeno!\n")
            print("A sua soma doos valores dso produtos ficou em:",somapedidos, "\n")
            tipodepedido= "pequeno"
            
        elif somapedidos > pedpequeno  <=  pedmedio :  
            print("Seu pedido é médio!") 
            tipodepedido="médio"
            if somapedidos > 500 and somapedidos< 999 :
                print("você recebeu 10%  de desconto")
                total = somapedidos - porcentodedesconto10 +1 -1
                print("A sua soma dos valores dos produtos ficou em:",somapedidos, "-",porcentodedesconto10 ,"=", comdesconto10,"\n" )
                Pessoadados.append(comdesconto10)
            print("A sua soma dos valores dos produtos ficou em:",somapedidos,"\n")

        elif somapedidos >= pedmaior :
            print("seu pedido é grande!\n")
            tipodepedido ="grande"
            if somapedidos >= 1000:
                print("você recebeu 20% de desconto\n") 
                total = somapedidos - porcentodedesconto20 +1 -1
                print("A sua soma dos valores dos produtos ficou em:",somapedidos, "-",porcentodedesconto20, "=" ,comdesconto20 ,"\n" )
                Pessoadados.append(comdesconto20)

            print("A sua soma dos valores dos produtos ficou em:",somapedidos,"\n")
    elif numerodepedidos == 2 :
        ped1 = float(input("Valor do seu pedido:"))
        ped2 = float(input("Valor do seu pedido:"))
        somapedidos= ped1+ped2
        porcentodedesconto10 = somapedidos *(10/100)
        porcentodedesconto20 = somapedidos *(20/100)
        comdesconto10 = somapedidos - porcentodedesconto10
        comdesconto20 = somapedidos - porcentodedesconto20
        if somapedidos < 300:
            print("Seu pedido é pequeno!")
            print("A sua soma doos valores dso produtos ficou em:",somapedidos)
            tipodepedido= "pequeno"
            
        elif somapedidos > pedpequeno  <=  pedmedio :  
            print("Seu pedido é médio!") 
            tipodepedido="médio"
            if somapedidos > 500 and somapedidos< 999 :
                print("você recebeu 10%  de desconto")
                total = somapedidos - porcentodedesconto10 +1 -1
                print("A sua soma doos valores dso produtos ficou em:",somapedidos, "-",porcentodedesconto10 ,"=", comdesconto10 )
            print("A sua soma doos valores dso produtos ficou em:",somapedidos)

        elif somapedidos >= pedmaior :
            print("seu pedido é grande!")
            tipodepedido ="grande"
            if somapedidos >= 1000:
                print("você recebeu 20% de desconto") 
                total = somapedidos - porcentodedesconto20 +1 -1
                print("A sua soma doos valores dso produtos ficou em:",somapedidos, "-",porcentodedesconto20, "=" ,comdesconto20 )
            print("A sua soma doos valores dso produtos ficou em:",somapedidos)
    
    elif numerodepedidos == 3:
        ped1 = float(input("Valor do seu pedido:"))
        ped2 = float(input("Valor do seu pedido:"))
        ped3 = float(input("Valor do seu pedido:"))
        somapedidos= ped1+ped2+ped3
        porcentodedesconto10 = somapedidos *(10/100)
        porcentodedesconto20 = somapedidos *(20/100)
        comdesconto10 = somapedidos - porcentodedesconto10
        comdesconto20 = somapedidos - porcentodedesconto20
        if somapedidos < 300:
            print("Seu pedido é pequeno!\n")
            print("A sua soma doos valores dso produtos ficou em:",somapedidos, "\n")
            tipodepedido= "pequeno"
            
        elif somapedidos > pedpequeno  <=  pedmedio :  
            print("Seu pedido é médio!") 
            tipodepedido="médio"
            if somapedidos > 500 and somapedidos< 999 :
                print("você recebeu 10%  de desconto")
                total = somapedidos - porcentodedesconto10 +1 -1
                print("A sua soma dos valores dos produtos ficou em:",somapedidos, "-",porcentodedesconto10 ,"=", comdesconto10,"\n" )
                Pessoadados.append(comdesconto10)
            print("A sua soma dos valores dos produtos ficou em:",somapedidos,"\n")

        elif somapedidos >= pedmaior :
            print("seu pedido é grande!\n")
            tipodepedido ="grande"
            if somapedidos >= 1000:
                print("você recebeu 20% de desconto\n") 
                total = somapedidos - porcentodedesconto20 +1 -1
                print("A sua soma dos valores dos produtos ficou em:",somapedidos, "-",porcentodedesconto20, "=" ,comdesconto20 ,"\n" )
                Pessoadados.append(comdesconto20)

            print("A sua soma dos valores dos produtos ficou em:",somapedidos,"\n")
    
    elif numerodepedidos == 4:
        ped1 = float(input("Valor do seu pedido:"))
        ped2 = float(input("Valor do seu pedido:"))
        ped3 = float(input("Valor do seu pedido:"))
        ped4 = float(input("Valor do seu pedido:"))
        somapedidos= ped1+ped2+ped3+ped4
        porcentodedesconto10 = somapedidos *(10/100)
        porcentodedesconto20 = somapedidos *(20/100)
        comdesconto10 = somapedidos - porcentodedesconto10
        comdesconto20 = somapedidos - porcentodedesconto20
        if somapedidos < 300:
            print("Seu pedido é pequeno!\n")
            print("A sua soma doos valores dso produtos ficou em:",somapedidos, "\n")
            tipodepedido= "pequeno"
            
        elif somapedidos > pedpequeno  <=  pedmedio :  
            print("Seu pedido é médio!") 
            tipodepedido="médio"
            if somapedidos > 500 and somapedidos< 999 :
                print("você recebeu 10%  de desconto")
                total = somapedidos - porcentodedesconto10 +1 -1
                print("A sua soma dos valores dos produtos ficou em:",somapedidos, "-",porcentodedesconto10 ,"=", comdesconto10,"\n" )
                Pessoadados.append(comdesconto10)
            print("A sua soma dos valores dos produtos ficou em:",somapedidos,"\n")

        elif somapedidos >= pedmaior :
            print("seu pedido é grande!\n")
            tipodepedido ="grande"
            if somapedidos >= 1000:
                print("você recebeu 20% de desconto\n") 
                total = somapedidos - porcentodedesconto20 +1 -1
                print("A sua soma dos valores dos produtos ficou em:",somapedidos, "-",porcentodedesconto20, "=" ,comdesconto20 ,"\n" )
                Pessoadados.append(comdesconto20)

            print("A sua soma dos valores dos produtos ficou em:",somapedidos,"\n")

    elif numerodepedidos == 5:
        ped1 = float(input("Valor do seu pedido:"))
        ped2 = float(input("Valor do seu pedido:"))
        ped3 = float(input("Valor do seu pedido:"))
        ped4 = float(input("Valor do seu pedido:"))
        ped5 = float(input("Valor do seu pedido:"))
        somapedidos = ped1+ped2+ped3+ped4+ped5
        porcentodedesconto10 = somapedidos *(10/100)
        porcentodedesconto20 = somapedidos *(20/100)
        comdesconto10 = somapedidos - porcentodedesconto10
        comdesconto20 = somapedidos - porcentodedesconto20
        if somapedidos < 300:
            print("Seu pedido é pequeno!\n")
            print("A sua soma doos valores dso produtos ficou em:",somapedidos, "\n")
            tipodepedido= "pequeno"
            
        elif somapedidos > pedpequeno  <=  pedmedio :  
            print("Seu pedido é médio!") 
            tipodepedido="médio"
            if somapedidos > 500 and somapedidos< 999 :
                print("você recebeu 10%  de desconto")
                total = somapedidos - porcentodedesconto10 +1 -1
                print("A sua soma dos valores dos produtos ficou em:",somapedidos, "-",porcentodedesconto10 ,"=", comdesconto10,"\n" )
                Pessoadados.append(comdesconto10)
            print("A sua soma dos valores dos produtos ficou em:",somapedidos,"\n")

        elif somapedidos >= pedmaior :
            print("seu pedido é grande!\n")
            tipodepedido ="grande"
            if somapedidos >= 1000:
                print("você recebeu 20% de desconto\n") 
                total = somapedidos - porcentodedesconto20 +1 -1
                print("A sua soma dos valores dos produtos ficou em:",somapedidos, "-",porcentodedesconto20, "=" ,comdesconto20 ,"\n" )
                Pessoadados.append(comdesconto20)
            
            print("A sua soma dos valores dos produtos ficou em:",somapedidos,"\n")
    
    else:
        print("error, try again")
        numerodepedidos += numerodepedidos
    Pessoadados.append(somapedidos)
    Pessoadados.append(tipodepedido)


while True:
    print("\nSeja bem-vindo(a) a nossa loja!")
    print("\nFaça Login:")
    login()
    print("\nlogin feito com sucesso!")
    print("-----------------------------------------------------------------------------------")
    for n in range(numero_de_pedidos) :
        print("cloque seus pedidos:")
        print("ATENÇÃO! numero maximo de pedidos é 5.")
        pedidos()
        print("resultados:\n")
        print(Pessoadados,"\n")
        print("Agradeço pela confiança, volte sempre!")
    break
