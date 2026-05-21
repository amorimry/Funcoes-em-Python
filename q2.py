# Você vai criar uma função que exibe a tabuada de qualquer número — o mesmo código servirá para qualquer valor que for passado.

def tabuada(numero):
    print(f"== Tabuada do {numero} ==")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i:2d} = {resultado:3d}")
        print()

tabuada(5)
tabuada(7)