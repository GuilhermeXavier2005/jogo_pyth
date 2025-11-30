import os, random, tkinter, sys
medio = [['agua', 'crer', 'ovos', 'ler', 'saia', 'piso', 'luz', 'pera', 'maca', 'caju'], 
         ['pedra', 'lapis', 'rocha', 'papel', 'feixe', 'faixa', 'caixa', 'danca', 'preco', 'lazer'], 
         ['conceito', 'concepcao', 'teoria', 'evidencia', 'crenca', 'lancamento', 'leitura', 'republica', 'automoveis', 'socorro']]


#sortear uma lista random.randint(0,3)
qtd_palavras_acertar=0
def aleatorio():
    for dificuldade in range(2):
        indice_array.append(random.randint(0,2))  
        palavra_escolhida.append(random.randint(0,9))
        letras_palavra.append(list(medio[indice_array[dificuldade]][palavra_escolhida[dificuldade]]))
        palavra_advinha.append(medio[indice_array[dificuldade]][palavra_escolhida[dificuldade]])

def montagem_da_dica():
    vogais = ['a', 'e', 'i', 'o', 'u']
    ajuda = ""
    contador=0
    vogais_encontradas=[]
    for vogal in range(len(vogais)):
        for letras in range(len(list(palavra_advinha[0]))):
            if vogais[vogal] == list(palavra_advinha[0])[letras]:
                contador+=1
                vogais_encontradas.append(vogais[vogal])
                ajuda += f"letra '{vogais[vogal]}' em alguma palavra misteriosa \n"
    return ajuda
     

def dica():
    #configurações de janela
    janela_dica = tkinter.Tk()
    janela_dica.geometry("220x200")
    janela_dica.title("")
    janela_dica.resizable(False, False)
    janela_dica.iconbitmap("")

    #configuração de texto
    informacao_palavra = montagem_da_dica()
    informacao = tkinter.Label(janela_dica, text=str(informacao_palavra))
    informacao.pack(side=tkinter.TOP, pady=10)

    #configurações de botão
    botao_encerrar = tkinter.Button(janela_dica, text='fechar', command=janela_dica.destroy)
    botao_encerrar.pack(side=tkinter.BOTTOM, pady=1)
    janela_dica.mainloop()

def dica2():
    import time
    vogais = ['a', 'e', 'i', 'o', 'u']
    os.system("cls")
    ajuda = "" 
    for vogal in range(len(vogais)):
        for letras in range(len(letras_palavra)):
            if vogais[vogal] == letras_palavra[letras]:
                ajuda+= " "+vogais[vogal]
                print(f"a vogal '{vogais[vogal]}' pertence a palavra misteriosa")
                break
    time.sleep(5)
    
#jogo de adivinha
while qtd_palavras_acertar<5:
    comeco = 0
    limite = 2
    letrada = ''
    exibir = ["",""]
    tentativa = ""
    indice_array = []
    palavra_escolhida = []
    letras_palavra = []
    palavra_advinha = []
    chance = 20
    
    aleatorio()

    while comeco != 1 or limite != 1:

        os.system("cls")

        exit("suas chances de adivinha zeraram") if chance <=0 else print()

        print("          TERM.IO            ", 2*"\n"," chances restantes: ", chance, "\n")

        for palavras in range(comeco, limite):
            print(len(letras_palavra[palavras]),"letras" ,exibir[palavras] if exibir[palavras] != "" else len(letras_palavra[palavras])*" _", "\n")
            exibir[palavras] = ""

        print("---------- | palavras usadas | -------\n", letrada, "\n")
        print(" ----------------------------")
        tentativa = str(input(" Digite uma palavra: "))

        if tentativa == palavra_advinha[0]:
            comeco = 1
        elif tentativa == palavra_advinha[1]:
            limite = 1
        elif tentativa != '"dica"':
            for palavra in range(comeco, limite):
                for letra in range(len(letras_palavra[palavra])):
                    try:
                        if list(tentativa)[letra] == letras_palavra[palavra][letra]:
                            exibir[palavra] += " "+ letras_palavra[palavra][letra]
                        else:
                            exibir[palavra] += " _"

                    except:
                        exibir[palavra] += " _"
            chance-=1
            letrada += str(tentativa) + " "
        elif chance>=11: 
            dica()
            chance-=10
        if comeco == 1 and limite == 1:
            break

    qtd_palavras_acertar+=1
os.system('cls')
sys.exit()
from encerramento import encerra_jogo
encerra_jogo()