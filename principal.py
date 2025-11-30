import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'modos_jogo')))

def recusa():
    menu()
    

def menu():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("musicas/somPrincipal.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1) 

    os.system("cls")
    print("----------------\n  | TERM.IO | \n----------------\n     menu: \n")
    dificuldade = {1:'medio', 2:'dificil',3:"como jogar", 4:"créditos", 5:"sair"}
    entradas = []
    for chave in dificuldade.keys():
        entradas.append(chave)
        
    for i in range(len(dificuldade)):
        print(entradas[i],".", dificuldade[i+1])
    print('\n')

    escolha = input()
    while True:
        match escolha:
            case '1':
                from medio import medio
                pygame.mixer.music.stop()
                medio()
                sys.exit()
                break
            case '2':
                pygame.mixer.music.stop()
                import dificil
                sys.exit()
                break
            case '3':
                import como_jogar
                como_jogar.instrucoes()
                sys.exit()
                break
            case '4':
                os.system("cls")
                import creditos
                creditos.creditos()
                sys.exit()
                break
            case '5':
                os.system("cls")
                sys.exit("saindo...")
            case '08122022':
                pygame.mixer.music.stop()
                os.system("cls")
                import joy
                sys.exit()
                break
            case _:
                escolha = 0
                return recusa()
        break
            
menu()
