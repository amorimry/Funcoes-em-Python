# Você vai criar uma função que exibe um cabeçalho formatado no terminal — útil para organizar a saída de qualquer sistema.

def cabecalho (titulo):
    print(f"""
----------------------------------------
{titulo.center(40)}
----------------------------------------
""")
    
cabecalho("CADASTRO DE CLIENTES")
cabecalho("RELATÓRIO DE VENDAS")
cabecalho("CONFIGURAÇÕES")