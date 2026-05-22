# Um professor precisa de um programa que calcule a média de cada aluno e informe automaticamente sua situação. A função de média deve apenas calcular e retornar — a decisão sobre a situação fica fora dela.

def calcular_media(n1, n2, n3, n4):
    media = (n1+n2+n3+n4) / 4
    return media

def verificar_situacao(nome, media):
    if media >= 7:
        situacao = "APROVADO"
    elif media >= 5:
        situacao = "RECUPERAÇÃO"
    elif media < 5:
        situacao = "REPROVADO"
    else:
        situacao = "MÉDIA INVÁLIDA"

    print(f"{nome} | {media:.2f} | {situacao}")

print("== ALUNO 1 ==")
media1 = calcular_media(8, 7.5, 9, 8.5)
verificar_situacao("Lucas", media1)

print("== ALUNO 2 ==")
verificar_situacao("Marina", calcular_media(5, 6, 4.5, 5.5))

print("== ALUNO 3 ==")
media3 = calcular_media(3, 4, 2.5, 3.5)
verificar_situacao("Pedro", media3)