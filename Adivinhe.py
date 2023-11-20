#cabeçalho do programa
print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 42

chute_str = input("Digite um número: ")
chute = int(chute_str)

if(chute == numero_secreto):
    print("Acertou")
elif( numero_secreto > chute):
    print("O número é maior ")
else:
    print("O número é menor")
