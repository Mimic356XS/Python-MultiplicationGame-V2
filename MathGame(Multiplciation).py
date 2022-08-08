def main():
    import random
    import colorama # <-- you will have to install the pakage "colorama"
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)

    from tqdm import tqdm # <-- you will also have to install the pakage "tqdm"
    import time

    with tqdm(total=500) as pbar: # <-- Loading bar
        for i in range(10):
            time.sleep(0.1)
            pbar.update(50)

    print(f"{Fore.RED}{Style.DIM}-------------------------------------------------",
          f"{Fore.LIGHTGREEN_EX}{Style.DIM}Done Loading!")
    # Title \/----------------------------------------------------------------------------------------------------------------\/
    print(
        f"{Fore.RED}{Back.BLACK}{Style.DIM}                                                                                                                                                                                                      ")
    print(
        f"{Fore.MAGENTA}{Back.BLACK}{Style.DIM}  ███╗░░░███╗░█████╗░████████╗██╗░░██╗" + f"{Fore.MAGENTA}{Style.DIM}    ░██████╗░░█████╗░███╗░░░███╗███████╗  " + f"{Fore.BLUE}{Back.BLACK}{Style.DIM}  ░░██╗███╗░░░███╗██╗░░░██╗██╗░░░░░████████╗██╗██████╗░██╗░░░░░██╗░█████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗██╗░░  ")
    print(
        f"{Fore.MAGENTA}{Back.BLACK}{Style.DIM}  ████╗░████║██╔══██╗╚══██╔══╝██║░░██║" + f"{Fore.MAGENTA}{Style.DIM}    ██╔════╝░██╔══██╗████╗░████║██╔════╝  " + f"{Fore.BLUE}{Back.BLACK}{Style.DIM}  ░██╔╝████╗░████║██║░░░██║██║░░░░░╚══██╔══╝██║██╔══██╗██║░░░░░██║██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║╚██╗░  ")
    print(
        f"{Fore.MAGENTA}{Back.BLACK}{Style.DIM}  ██╔████╔██║███████║░░░██║░░░███████║" + f"{Fore.MAGENTA}{Style.DIM}    ██║░░██╗░███████║██╔████╔██║█████╗░░  " + f"{Fore.BLUE}{Back.BLACK}{Style.DIM}  ██╔╝░██╔████╔██║██║░░░██║██║░░░░░░░░██║░░░██║██████╔╝██║░░░░░██║██║░░╚═╝███████║░░░██║░░░██║██║░░██║██╔██╗██║░╚██╗  ")
    print(
        f"{Fore.MAGENTA}{Back.BLACK}{Style.DIM}  ██║╚██╔╝██║██╔══██║░░░██║░░░██╔══██║" + f"{Fore.MAGENTA}{Style.DIM}    ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  " + f"{Fore.BLUE}{Back.BLACK}{Style.DIM}  ╚██╗░██║╚██╔╝██║██║░░░██║██║░░░░░░░░██║░░░██║██╔═══╝░██║░░░░░██║██║░░██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║░██╔╝  ")
    print(
        f"{Fore.MAGENTA}{Back.BLACK}{Style.DIM}  ██║░╚═╝░██║██║░░██║░░░██║░░░██║░░██║" + f"{Fore.MAGENTA}{Style.DIM}    ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  " + f"{Fore.BLUE}{Back.BLACK}{Style.DIM}  ░╚██╗██║░╚═╝░██║╚██████╔╝███████╗░░░██║░░░██║██║░░░░░███████╗██║╚█████╔╝██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║██╔╝░  ")
    print(
        f"{Fore.MAGENTA}{Back.BLACK}{Style.DIM}  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝" + f"{Fore.MAGENTA}{Style.DIM}    ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  " + f"{Fore.BLUE}{Back.BLACK}{Style.DIM}  ░░╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝╚═╝░░░░░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░  ")
    print(
        f"{Fore.RED}{Back.BLACK}{Style.DIM}                                                                                                                                                                                                      ")
    # ----------------------------------------------------------------------------------------------------------------------
    # Play the game or Not
    Play_Game = input(
        f"{Fore.LIGHTMAGENTA_EX}{Style.DIM}Type " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Play" + f" to Start the game (Or type " + f"{Fore.RED}{Style.DIM}Quit" + " to quit the game) : ")
# Quit
    if Play_Game.lower() == "Quit":
        exit()
    if Play_Game.lower() == "quit":
        exit()
# Play
    if Play_Game.lower() == "Play":
        pass
    if Play_Game.lower() == "play":
        pass
# other
    if Play_Game.lower() == "":
        exit()

    # Asking for name
    Player_name = input(f"{Fore.LIGHTGREEN_EX}{Style.DIM}What is your name? : ")
    Player_score: int = 0
    Player_lives = 3
    Level = 1

    while True:
        x = random.randint(1, 12) # <-- the higher the second number, the harder the questions will be
        y = random.randint(1, 12) # <-- the higher the second number, the harder the questions will be

        print(f"{Fore.BLUE}{Style.DIM}|---------------------|")
        print(f"{Fore.BLUE}{Style.DIM}| what is " + str(x) + " times " + str(y) + " ?") # <-- the question being printed
        print(f"{Fore.BLUE}{Style.DIM}|---------------------|")
        answer = int(input(f"{Fore.LIGHTWHITE_EX}{Style.DIM}Answer: "))
        # Checking Answer and Scoring
        if answer == (x * y): # <-- checking if the answer is correct and determine if the player will get a point or not

            print(f"{Fore.LIGHTGREEN_EX}{Style.DIM}Correct!")
            Player_score += 1
            print(f"{Fore.LIGHTYELLOW_EX}{Style.DIM}Score : ", Player_score,
                  f"{Fore.CYAN}{Style.DIM} Level : ", Level,
                  f"{Fore.RED}{Style.DIM} Lives ❤ : ", Player_lives)
        else: # <-- if the player gets the question incorrect
            Player_score -= 2
            Player_lives -= 1
            print(f"{Fore.LIGHTRED_EX}{Style.DIM}Incorrect Answer. The answer was " + str(x * y),
                  f"{Fore.CYAN}{Style.DIM} Level : ", Level,
                  f"{Fore.RED}{Style.DIM} Lives : ", Player_lives)

        # Lives
        if Player_score == 30:
            Player_lives += 1
            print(f"{Fore.LIGHTRED_EX}{Style.DIM} [ +1 Lives ❤]")

        if Player_score == 30:
            Player_lives += 1
            print(f"{Fore.LIGHTRED_EX}{Style.DIM} [ +1 Lives ❤]")

        # Levels
        if Player_score == 10 and Level == 1:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 20 and Level == 2:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 30 and Level == 3:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 40 and Level == 4:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 50 and Level == 5:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 60 and Level == 6:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 70 and Level == 7:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 80 and Level == 8:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 90 and Level == 9:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 100 and Level == 10:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 110 and Level == 11:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 120 and Level == 12:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 130 and Level == 13:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 140 and Level == 14:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 150 and Level == 15:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 160 and Level == 16:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 170 and Level == 17:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 180 and Level == 18:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 190 and Level == 19:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 200 and Level == 20:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 210 and Level == 21:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 220 and Level == 22:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 230 and Level == 23:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 240 and Level == 24:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 250 and Level == 25:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 260 and Level == 26:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 270 and Level == 27:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 280 and Level == 28:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 290 and Level == 29:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 300 and Level == 30:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 310 and Level == 31:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 320 and Level == 32:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 330 and Level == 33:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 340 and Level == 34:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 350 and Level == 35:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 360 and Level == 36:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 370 and Level == 37:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 380 and Level == 38:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 390 and Level == 39:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 400 and Level == 40:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")

        if Player_score == 410 and Level == 41:
            Level += 1
            print(
                f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |"
                                                                                                    f"{Fore.LIGHTGREEN_EX}{Style.DIM} ! You have reached max level !")
        # You can also add more levels if you want, just copy  this \/
        #         if Player_score == 400 and Level == 40:
        #             Level += 1
        #             print(
        #                 f"{Fore.LIGHTGREEN_EX}{Style.DIM}| " + f"{Fore.LIGHTGREEN_EX}{Style.DIM}Level +1" + f"{Fore.LIGHTGREEN_EX}{Style.DIM} |")
        # and add the Player_score by 10 and the level by 1
        # ------------------------------------------------------------------------------------------------------------------

        if Player_score < 0:
            Player_score = 0
            print(f"{Fore.RED}{Style.DIM}You have a score of zero")

        if Player_lives == 0:
            print("   ")
            print(f"{Fore.RED}{Style.DIM}[ GAME OVER ] "
                  )
            print("   ")
            restart: str = input(
                f"{Fore.MAGENTA}{Style.DIM}Type Restart to restart the game, type quit to quit the game : ")
            if restart.lower() == "Restart": # <-- restart the game
                main()
            if restart.lower() == "restart":
                main()
            if restart.lower() == "quit": # <-- quit the game
                exit()
            if restart.lower() == "Quit":
                exit()
            else:
                break


main()
