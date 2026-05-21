# Leia o código abaixo com atenção e responda as três perguntas sem executar o programa. O objetivo é entender o que acontece com variáveis de mesmo nome em escopos diferentes.

x = 10

def dobrar():
    x = 20
    print(x)

dobrar()
print(x)

# a) Escreva exatamente o que será impresso no terminal, linha por linha. Justifique cada linha com base no conceito de escopo.

# Terminal:
# 20
# 10
# Justificativa: o código primeiramente, com uma variavel global (x), me fornece um número 10, logo em seguida temos a função "dobrar", dentro dele a minha variavel local (x) é 20 e depois dessa variavel receber esse valor ele é impresso com o "print". Fora da função, a própria é chamada, sem parâmetro, me dando um valor "20" no terminal, justamente porque está pegando a variavel local e imprimindo ela. Após o chamado da função, é colocado um "print(x)" que vai retornar o valor "10", que ta guardado na variavel global, já que a mesma variavel x que esta dentro da função só existe dentro da função.

# b) A linha x = 20 dentro de dobrar() altera o valor do x que está fora da função? Explique por quê.

# Não, pois o que tem dentro da função só existe dentro dela, não interferindo em nada no código se não for chamada.

# c) Reescreva a função dobrar de forma correta: ela deve receber um número por parâmetro, calcular o dobro e retornar o resultado. Fora da função, chame-a com x = 10 e exiba o resultado com print.

def dobrar(x):
    resultado = x * 2
    return resultado

result = dobrar(10)
print(f"O dobro de {x} é {result}")