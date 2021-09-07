import random
from emoji import emojize
import time

itens = ('pedra','papel','tesoura')

jogador = int(input("Escolha:\n0- Pedra\n\n1- Papel\n\n2- tesoura\n\nOpção: "))

time.sleep(1)
print("JÓ...\n")
time.sleep(1)
print("KEM...\n")
time.sleep(1)
print("PO\n")


CPU = random.randint(0,2)

if CPU == 0:
    if jogador == 0:
        print(emojize("os dois escolheram PEDRA, então deu empate!:wink:",use_aliases=True))
    elif jogador == 1:
        print(emojize("O Jogador escolheu PAPEL e a CPU escolheu PEDRA... O jogador venceu:wink:",use_aliases=True))
    elif jogador == 2:
        print(emojize("A Jogador escolheu TESOURA e a CPU jogou PEDRA... A CPU VENCEU!!!:stuck_out_tongue_winking_eye:",use_aliases=True))
elif CPU == 1:
    if jogador == 0:
        print(emojize("O jogador escolheu PEDRA e a CPU jogou PAPEL... A CPU VENCEU!!!:fu:",use_aliases=True)) 
    elif jogador == 1:
        print(emojize("Os dois escolheram PAPEL, ENTÃO DEU EMPATE!:eyes:",use_aliases=True)) 
    elif jogador == 2:
        print(emojize("O jogador jogou TESOURA e a CPU jogou PAPEL... O JOGADOR VENCEU!!!!:sunglasses:",use_aliases=True)) 
elif CPU == 2:
    if jogador == 0:
        print(emojize("O jogador escolheu PEDRA e a CPU escolheu TESOURA... O JOGADOR VENCEU:facepunch:",use_aliases=True))  
    elif jogador == 1:
        print(emojize("O jogador escolheu PAPEL e a CPU escolheu TESOURA... A CPU VENCEU:joy:",use_aliases=True))
    elif jogador == 2:
        print(emojize("os dois escolheram TESOURA,ENTÃO DEU EMPATE:rage3:",use_aliases=True))