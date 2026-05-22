# Você vai criar uma função que exibe um cabeçalho formatado no terminal — útil para organizar a saída de qualquer sistema.

def cabecalho (titulo):
    print(f"""
----------------------------------------
{titulo.center(40)}
----------------------------------------
""")
    # espaco = int((40-len(titulo))/2)
    # print("-"*40)
    # print(f"{" "*espaco}{titulo}{" "*espaco}")
    # print("-"*40)
    
cabecalho("CADASTRO DE CLIENTES")
cabecalho("RELATÓRIO DE VENDAS")
cabecalho("CONFIGURAÇÕES")