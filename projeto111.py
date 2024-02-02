import random  


response = "y"

while response == "y":
    dice_roll = random.randint(1, 6)

    print("Você lançou o dado e obteve:")
    
    if dice_roll == 1:
        print("---------")
        print("|       |")
        print("|   *   |")
        print("|       |")
        print("---------")
    elif dice_roll == 2:
        print("---------")
        print("| *     |")
        print("|       |")
        print("|     * |")
        print("---------")
    elif dice_roll == 3:
        print("---------")
        print("| *     |")
        print("|   *   |")
        print("|     * |")
        print("---------")
    elif dice_roll == 4:
        print("---------")
        print("| *   * |")
        print("|       |")
        print("| *   * |")
        print("---------")
    elif dice_roll == 5:
        print("---------")
        print("| *   * |")
        print("|   *   |")
        print("| *   * |")
        print("---------")
    else:
        print("---------")
        print("| *   * |")
        print("| *   * |")
        print("| *   * |")
        print("---------")


    response = input("Deseja jogar novamente? (y/n): ").lower()


print("Fim do jogo. Obrigado por jogar!")
