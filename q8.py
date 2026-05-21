# Um professor precisa de um programa que calcule a média de cada aluno e informe automaticamente sua situação. A função de média deve apenas calcular e retornar — a decisão sobre a situação fica fora dela.

def calcular_media(n1, n2, n3, n4):
    media = (n1+n2+n3+n4) / 4

    return media

print("== ALUNO 1 ==")
media = calcular_media(8, 7.5, 9, 8.5)
if media >= 7:
    situacao = "APROVADO"
elif media >= 5:
    situacao = "RECUPERAÇÃO"
elif media > 5:
    situacao = "REPROVADO"
else:
    situacao = "MÉDIA INVÁLIDA"

print(f"Aluno 1 | Média: {media} | Situação: {situacao}")

print("== ALUNO 2 ==")
media = calcular_media(5, 6, 4.5, 5.5)
if media >= 7:
    situacao = "APROVADO"
elif media >= 5:
    situacao = "RECUPERAÇÃO"
elif media > 5:
    situacao = "REPROVADO"
else:
    situacao = "MÉDIA INVÁLIDA"

print(f"Aluno 2 | Média: {media} | Situação: {situacao}")

print("== ALUNO 3 ==")
media = calcular_media(3, 4, 2.5, 3.5)
if media >= 7:
    situacao = "APROVADO"
elif media >= 5:
    situacao = "RECUPERAÇÃO"
elif media > 5:
    situacao = "REPROVADO"
else:
    situacao = "MÉDIA INVÁLIDA"

print(f"Aluno 3 | Média: {media} | Situação: {situacao}")
