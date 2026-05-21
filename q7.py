# Um caixa de mercado precisa calcular o troco do cliente. O resultado deve ser retornado pela função — não apenas impresso — para que o programa possa usá-lo depois.

def calcular_troco(total, pago):
    if pago < total:
        print("Erro: valor pago insuficiente.")
        troco = 0 
    else:
        troco = pago - total

    return troco

print("-- Cliente 1 --")
resultado1 = calcular_troco(47.50, 50.00)
print(f"{resultado1}")

print("-- Cliente 2 --")
resultado2 = calcular_troco(80.00, 60.00)
print(f"{resultado2}")
