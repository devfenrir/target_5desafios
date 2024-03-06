# Desafio 4

'''4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente.
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?'''

def descobrir_interruptores(): # função pra descobrir qual interruptor controla qual lampada

    lampadas = [False, False, False] #supondo que estão todas desligadas

    lampadas[0] = not lampadas[0] #primeira ida: liga o primeiro interruptor e desliga

    lampadas[1] = not lampadas[1] # Segunda ida: liga o segundo interruptor

    print("Estado das lâmpadas após a segunda ida:") 
    for i, estado in enumerate(lampadas):
        print(f"Lâmpada {i + 1}: {'Acesa' if estado else 'Apagada'}")

descobrir_interruptores()
