def verificar_aprovacao(nota):
    if nota >= 6:
        return "Aprovado!"
    else:
        return "Reprovado!"

nota_aluno = float(input("Digite a nota do aluno: "))
print(verificar_aprovacao(nota_aluno))
