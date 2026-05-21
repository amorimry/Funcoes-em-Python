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

def incrementar():
    contador += 1
    return contador

incrementar()
incrementar()
incrementar()
print(contador)


# b) Reescreva o programa sem usar global, usando parâmetro e return. A função incrementar deve receber o valor atual do contador e retornar o valor incrementado. Fora da função, chame-a três vezes e armazene o resultado de volta na variável contador a cada chamada.