# Sistema de Controle de Alunos em uma Academia

nome = input("Qual o seu nome? "),
idade = input("Qual a sua idade? "),
altura = input("Qual a sua altura? "),
avaliacoes = input("Digite suas nova separando-as com espaços únicos: ")

for i in range(5):
    alunos = [{"nome": nome,"idade": idade, "altura": altura, "avaliacoes": avaliacoes}]

print(alunos)