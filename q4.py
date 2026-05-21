# Um sistema de vendas precisa imprimir os itens de uma nota fiscal. Cada produto deve ser exibido com seu preço unitário, quantidade e subtotal calculado.

def exibir_produto(nome, preco, qtd):
    subtotal = preco * qtd
    print(f"""
Produto: {nome}
Preço: R$ {preco:.2f}
Quantidade: {qtd}

    Subtotal: R$ {subtotal:.2f}
""")
    
exibir_produto("Notebook", 3500, 2)
exibir_produto("Mouse", 89.90, 3)
exibir_produto("Teclado", 149, 1)