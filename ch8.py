while(True):
    numbers = [3,2,4,5]
    guess = input("Guess a number in the list or type q to quit\n")
    if(guess == 'q'):
        break;
    if int(guess) in numbers:
        print("You guessed right")
    else:
        print("Incorrect")

lst = [8, 19, 148, 4]
lst2 = [9, 1, 33, 83]
lst3 = []
for x in range(len(lst)):
    lst3.append(lst[x]*lst2[x])

print(lst3)
