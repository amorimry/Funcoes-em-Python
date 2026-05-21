# Uma pizzaria quer registrar pedidos com diferentes personalizações. Quando o cliente não especifica tamanho ou borda, o sistema deve usar os valores padrão.

def registrar_pedido (sabor, tamanho="Média", borda="Simples"):
    print(f"""--- RESUMO DO PEDIDO ---
Sabor da pizza: {sabor}
Tamanho: {tamanho}
Borda: {borda}
""")
    
registrar_pedido("Calabresa")
registrar_pedido("Frango", "Grande")
registrar_pedido("Portuguesa", "Família", "Catupiry")
registrar_pedido("Margherita", borda="Cheddar")