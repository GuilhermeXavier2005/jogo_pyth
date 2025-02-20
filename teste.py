import time, random

vogais = ['a', 'e', 'i', 'o', 'u']
vogais_encontradas = []
n_vezes_vogais_encontradas = []
palavras = ['azedo', 'outro', 'socorra']
qtd_vogais=0

for palavra in range(len(palavras)):
    for vogal in range(len(vogais)):
        contador=0
        for letras in range(len(list(palavras[palavra]))):
            if vogais[vogal] == list(palavras[palavra])[letras]:
                contador+=1
                vogais_encontradas.append(vogais[vogal])
                print(f"letra '{vogais[vogal]}' em alguma palavra {palavras[palavra]}")

#for l in range(len(palavras)):
    #for i in range(len(vogais_encontradas)):          
        #print(f"há {contador} '{vogais_encontradas[i]}' e é uma vogal pertecente a palavra {palavras[l]}")