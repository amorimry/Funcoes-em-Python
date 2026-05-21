# Uma loja quer aplicar descontos variados em seus produtos. Quando nenhum desconto for informado, o sistema deve usar 10% automaticamente.

def aplicar_desconto(preco, desconto = 10):
    valor_desconto = preco * desconto / 100
    preco_final = preco - valor_desconto
    print(f"""
Preço original : R$ {preco:.2f}
Desconto ({desconto}%) : R$ {valor_desconto:.2f}

    Preço final : R$ {preco_final:.2f}
""")
    
aplicar_desconto(200.00)
aplicar_desconto(200.00, 5)
aplicar_desconto(200.00, desconto=20)