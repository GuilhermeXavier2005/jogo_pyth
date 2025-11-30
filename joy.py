import time
import sys
import os

AZUL = "\033[34m"
RESET = "\033[0m"
VERMELHO = "\033[31m"

estrofe1 = """I guess i should stop. \n"""
estrofe2 = """looking out for youu.\n"""
estrofe3 = """like i always do.\n"""
estrofe4 = """when will you. \n"""
estrofe5 = """start looking for me too. \n"""
estrofe6 = """instead of leaving me staring at my shoes. \n"""
estrofe7 = """just a wayy you´re glancing at me. \n"""
estrofe8 = """something about you just makes me feel guilty for. \n"""
estrofe9 = """liking you. \n"""
estrofe10 = """when you´re with him ... when you´re with him. \n"""
refrao = """this is a love song for a girl, who will never knows is about her. \n"""
estrofe11 = """know pretty stupid but i´m much too shy to tell her.\n"""
estrofe12 = """she´s beaming that smile all the while. \n"""
estrofe13="""i´m all chocked up on my own throat. \n"""
estrofe14="""I guess there is no hope. \n"""
estrofe15="""when you walk out in the snow. \n"""
estrofe16="""i say i guess i....       should go.\n"""
estrofe17="""and we´re talk about someone else.\n"""
estrofe18="""when we should...         be talking about ourselves. \n"""
estrofe19="""it´s same old situation, you always got me waiting. \n"""
estrofe20="""come on dear, i think times a wastin´before we have to go back...   inside and return.\n"""
estrofe21="""to our normal lives...\n"""

principal="""      _______  ___    ___  ____  ________      __     _____       _______          ___        ______     ___       ___    ______        _____     _____    ____   __    _______ \n"""
principal2="""      |__   _| | |    | |  |  |  |   ____]    |  |   |  ___]     /  ____ \        |   |      /  ___ \    \  \     /  /   |   ___|      |  ___]   / ___ \   |   \ /  |  /   ____\  \n"""
principal3="""         | |   | |____| |  |  |  |   |___     |  |   | [___     /  /____\ \       |   |     |  |   | |    \  \   /  /    |  [__        |  [_    |  |  | |  | | \  | | |  [     \n """
principal4="""        | |   |  ____  |  |  |  [_____  ]    |  |   |___  ]   |   _____   |      |   |     |  |   | |     \  \ /  /     |  ___]       |___ ]   |  |  | |  | |  \ | | |  [   __\n"""
principal5="""         | |   | |    | |  |  |   _____| ]    |  |    ___| |   |  |     |  |      |   |___  |  \__/  |      \     /      | |____        __| ]   |  \__/ |  | |    \ | |  [__]  |\n"""
principal6="""         |_|   |_|    |_|  |__|  |_______|    |__|   |_____|   |__|     |__|      |_______|  \______/        \___/       |______|      |____|    \_____/   |_|    \_|  \_______/  \n"""

letraTotal = """I guess i should stop.
looking out for you.
like i always do."""

os.system('cls')

def refraogrande():
    sys.stdout.write(VERMELHO+principal+RESET+VERMELHO+principal2+RESET+VERMELHO+principal3+RESET+VERMELHO+principal4+RESET+VERMELHO+principal5+RESET+VERMELHO+principal6+RESET)
    sys.stdout.flush()


def musica():
    import pygame
    pygame.init()
    pygame.mixer.music.load("musicas/musicaEla.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

    time.sleep(22.5)
    for char in estrofe1:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.1)  # velocidade da animação (ajuste aqui)
    time.sleep(1.5)
    for char in estrofe2:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1.1)
    for char in estrofe3:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1.5)
    for char in estrofe4:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1.2)
    for char in estrofe5:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(.1)
    for char in estrofe6:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.09)
    time.sleep(.3)
    for char in estrofe7:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(.3)
    for char in estrofe8:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(.7)
    for char in estrofe9:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1)
    for char in estrofe10:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(1)
    ##refraogrande()
    for char in refrao:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(1)
    for char in estrofe11:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(1)
    for char in estrofe12:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(1)
    for char in estrofe13:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(1)
    for char in estrofe14:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(17.5)
    os.system('cls')
    for char in estrofe15:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(1)
    for char in estrofe16:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(2.3)
    for char in estrofe17:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(2.3)
    for char in estrofe18:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(.7)
    for char in estrofe19:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(1.3)
    for char in estrofe20:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(2.6)
    for char in estrofe21:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(1.7)
    ##refraogrande()
    for char in refrao:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(1)
    for char in estrofe11:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(1)
    for char in estrofe12:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(1)
    for char in estrofe13:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(1)
    for char in estrofe14:
        sys.stdout.write(AZUL + char + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(23.5)


    time.sleep(1)

musica()
from principal import menu
menu()