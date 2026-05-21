# Uma academia precisa de um programa que calcule e exiba o IMC de seus alunos. Cada chamada da função representa um aluno diferente.

def calcular_imc(nome, peso, altura):
    imc = peso / altura**2
    print(f"""
Nome: {nome}
IMC: {imc:.2f}
""")

calcular_imc("Ana", 62, 1.65)
calcular_imc("Carlos", 90, 1.80)
calcular_imc("Beatriz", 55, 1.58)