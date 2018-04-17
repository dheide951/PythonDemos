

import random

def hangman(word=""):
    wrong = 0
    default = ["apple", "banana", "cat", "key", "ball"]
    stages = ["",
              "________           ",
              "|                  ",
              "|        |         ",
              "|        O         ",
              "|      / | \       ",
              "|       / \        ",
              "|                  "]
    if word == "":
        word = default[random.randint(0,len(default))]
        
    rletters = list(word)
    board = ["__"]*len(word)
    #print(board)
    win = False
    print("Welcome to Hangman")
    while(wrong < len(stages) - 1):
        print(" ")
        guess = input("Guess a letter " )
        if guess in rletters:
            for x in range(len(rletters)):
                if rletters[x] == guess:
                    board[x] = guess
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if "__" not in board:
            print("You Win")
            #print("".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! it was {}".format(word))
            
        

hangman()
    
