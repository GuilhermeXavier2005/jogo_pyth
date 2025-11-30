
def medio():
    import os, time
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    import pygame

    pygame.mixer.init()
    
    os.system('cls')
    facil = [['agua', 'crer', 'ovos', 'ler', 'saia', 'piso', 'luz', 'pera', 'maca', 'caju'], 
            ['pedra', 'lapis', 'rocha', 'papel', 'feixe', 'faixa', 'caixa', 'danca', 'preco', 'lazer'], 
            ['conceito', 'concepcao', 'teoria', 'evidencia', 'crenca', 'lancamento', 'leitura', 'republica', 'automoveis', 'socorro']]

    letrada = ''
    exibir = ''
    qtd_palavras_acertar=0
    tentativa = ""
    vogais = ['a', 'e', 'i', 'o', 'u']

    def dica():
        os.system("cls")
        ajuda = "" 
        for vogal in range(len(vogais)):
            for letras in range(len(letras_palavra)):
                if vogais[vogal] == letras_palavra[letras]:
                    ajuda+= " "+vogais[vogal]
                    print(f"a vogal '{vogais[vogal]}' pertence a palavra misteriosa")
                    break
        time.sleep(5)

    #sortear uma lista random.randint(0,3)
    import random

    while qtd_palavras_acertar<10:
    #sortear quais palavras serão passadas pra o jogador advinhar
        indice_array = random.randint(0,2)
        palavra_escolhida = random.randint(0,9)
        letras_palavra = list(facil[indice_array][palavra_escolhida])
        qtd_letras = len(letras_palavra)
        chances = 26
    #enquanto o jogador não acertar dentro das chances  repita  
        
        while tentativa != facil[indice_array][palavra_escolhida] or chances == 0:
            os.system("cls")

            if chances <= 0: 
                exit("suas chances de adivinha zeraram") 
            else: 
                chances -=1

            print("          TERM.IO            ", 2*"\n", qtd_letras, "letras       chances:",chances, 2*"\n", exibir if exibir != "" else qtd_letras*" _ ", 3*"\n", "----------palavras usadas-------\n", letrada, "\n")
            print(" ----------------------------")
            tentativa = str(input(" Digite uma palavra: "))
            print(3*"\n")

            exibir = ""
            
            #dica() if tentativa == '"dica"' else exibir
            match tentativa:
                case '"dica"':
                    dica()
                    chances-=9
                case _:
                    for letra in range(qtd_letras):
                #para cada verificacao, verifica se não ocorrerá erros
                        try:
                            if letras_palavra[letra] == list(tentativa)[letra]:
                                exibir += " "+ list(tentativa)[letra]
                            else: 
                                exibir += " _ "
                #usando da função try e except para melhor dinamizar o jogo e ajudar o jogador
                        except:
                            exibir += " _ "
            
            letrada += str(tentativa) + " "

        exibir = ""
        letrada = ""
        qtd_palavras_acertar+=1
    import encerramento
    encerramento.encerra_jogo()
    #o jogo só finaliza quando encerrar todas as 10 palavras, mesmo se errar todas elas