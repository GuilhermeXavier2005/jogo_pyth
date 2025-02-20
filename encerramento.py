def encerra_jogo():
    import os, sys, time
    print("\n", 
        "            _________   _______   ________     ____    _____        __   _______ ","\n",
        "           |___   ___| |   ____| |  ___   /   |  _ \  /  _  |      |  | |  ___  |", "\n",
        "               | |     |  |___   | |   / /    | | \ \/  / | |      |  | | |   | |",   "\n",
        "               | |     |   ___|  | |___\ \    | |  \__ /  | |      |  | | |   | |", "\n",
        "               | |     |  |      |   __   \   | |         | |      |  | | |   | |", "\n",
        "               | |     |  |____  |  |  \   \  | |         | |  ___ |  | | |___| |", "\n",
        "               |_|     |_______| |__|   \___\ |_|         |_| /__/ |__| |_______|", 2*"\n",
        
        "                      Parabéns você completou todas palavras no adivinha", 2*'\n', 2*"\n")
    print("...")
    time.sleep(5)
    from principal import menu
    menu()
    sys.exit()

encerra_jogo()