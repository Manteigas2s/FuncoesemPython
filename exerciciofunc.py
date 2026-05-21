def cabecalho(titulo):
    print("-" *40)
    print(titulo.center(40))
    print("-" *40)

cabecalho("CADASTRO DE CLIENTES")
cabecalho("RELATÓRIO DE VENDAS")
cabecalho("CONFIGURAÇÕES")

def tabuada(numero):
    for i in range(1, 11):
        print(f"{i:2d}")

