# elabore um programa que valide um nome e caso
# seja Flavio,Douglas ou Nico, mostre seja bem vindo,
# caso contrário mostre usuário não identificado

nome = input("Digite um nome: ")

if (nome == "Flávio"):
    print(f"Seja Bem Vindo,{nome}!!")
elif (nome == "Douglas"):
    print(f"Seja Bem Vindo,{nome}!!")
elif(nome == "Nico"):
    print(f"Seja Bem Vindo,{nome}!!")
else:
    print("usuário não identificado")

