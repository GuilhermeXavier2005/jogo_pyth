def instrucoes():
    import os, sys, time
    os.system("cls")
    print(" O modo de jogo principal é composto por duas dificuldades", 2*"\n", 
    "Dificil: o jogador deve adivinhar duas palavras que são aleatóriamente sorteadas", 2*"\n", "        chances restantes: N", "\n")
    print("palavra1 7 letras: _ _ _ _ _ _ _ ","\n")
    print("palavra2 4 letras: _ _ _ _ ","\n")
    time.sleep(7)

    os.system("cls")
    print( "Médio: o jogador deve adivinhar somente uma palavra que é aleatóriamente gerada", 2*"\n", "        chances restantes: N", "\n")
    print("palavra1 7 letras: _ _ _ _ _ _ _ ","\n")
    time.sleep(5)

    os.system("cls")
    print("O jogo possui a opção de dicas ao jogador \nrevelando uma vogal que pertence a uma/alguma das palavras\n\n a 'vogal qualquer' pertence a alguma palavra",
        2*"\n",  "a dificuldade média e difícil possuem a mesma mecânica ", 2*"\n", "uma vogal repetida na tela também é repetida na palavra misteriosa")
    time.sleep(5)

    os.system("cls")
    print("a função dica consome 10 chances, cuidado ao usa-la", 2*"\n", "zerando as suas chances o jogo é fechado, perdendo o progresso")
    time.sleep(4)
    os.system("cls")
    print("boa sorte...")
    time.sleep(3)
    from principal import menu
    os.system("cls")
    menu()
    sys.exit()
    
instrucoes()
