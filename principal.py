

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'modos_jogo')))

def recusa():
    menu()

def menu():
    import os, sys
    os.system("cls")
    print("----------------\n  | TERM.IO | \n----------------\nseleciona uma dificuldade: \n")
    dificuldade = {1:'medio', 2:'dificil',3:"como jogar", 4:"sair"}
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
                medio()
                sys.exit()
                break
            case '2':
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
                sys.exit("saindo...")
            case _:
                escolha = 0
                return recusa()
        break
            
menu()