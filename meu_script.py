import random

def jogo_da_adivinhacao():
    numero_aleatorio = random.randint(1, 100)
    tentativas = 0
    
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Eu escolhi um número entre 1 e 100. Tente adivinhar!")
    
    while True:
        tentativa = int(input("Digite o seu palpite: "))
        tentativas += 1
        
        if tentativa < numero_aleatorio:
            print("Tente um número maior.")
        elif tentativa > numero_aleatorio:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas!")
            break
            
    jogar_novamente = input("Deseja jogar novamente? (sim/não): ")
    if jogar_novamente.lower() == "sim":
        jogo_da_adivinhacao()
    else:
        print("Obrigado por jogar!")

jogo_da_adivinhacao()
