# O código abaixo tem um erro que impede sua execução. Leia-o com atenção e responda as perguntas antes de corrigi-lo.

# contador = 0

# def incrementar():
#     contador += 1

# incrementar()
# incrementar()
# incrementar()
# print(contador)

# a) Execute o código e anote o erro exibido pelo Python. Pesquise ou explique com suas palavras o que significa UnboundLocalError e por que ele ocorre aqui.

contador = 0

def incrementar(num):
    global contador
    contador += 1

incrementar()
incrementar()
incrementar()
print(contador)

# Dá errado pois tudo que tiver dentro da função o python entende que é uma variável local, ent precisa fazer com que o python pegue a variável global para poder modificar ela.


# b) Reescreva o programa sem usar global, usando parâmetro e return. A função incrementar deve receber o valor atual do contador e retornar o valor incrementado. Fora da função, chame-a três vezes e armazene o resultado de volta na variável contador a cada chamada.

contador = 0

def incrementar(num):
    return num + 1

contador = incrementar(contador)
contador = incrementar(contador)
contador = incrementar(contador)
print(contador)