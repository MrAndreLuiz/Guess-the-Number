import random

def guess_the_number():
    print("Bem-vindo ao Guess the Number!\n")
    print("O jogo selecionou um número inteiro entre 1 e 100. Você tem 10 tentativas para adivinhar o número.\n")
    number = random.randint(1, 100)
    attempts = 10
    while attempts > 0:
        guess = int(input("Digite um número entre 1 e 100: "))
        if guess == number:
            print("Parabéns! Você adivinhou o número!")
            break
        elif guess < number:
            print("O número é maior.")
        else:
            print("O número é menor.")
        attempts -= 1
        print(f"Você ainda tem {attempts} tentativas restantes.\n")
    else:
        print("Você perdeu. O número era:", number)

guess_the_number()