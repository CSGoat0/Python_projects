# Purpose: The player who reaches 100 first wins
# Author: Abdelrahman Nabil

print("***** Welcome to our game! *****\n\n")
print("Our rules is very easy, the first player who reaches 100 wins.\n")
print("Increment is only between 1 to 10 , no overflow after 100.\n")
print("Let's get started\n\n")
# num refers to the main game progress
num:int = 0
while num < 100:
    # saver is a variable i will use to save game progress to handel most errors (To avoid num to be more than 100)
    saver:int = int(num)
    # T1 and T2 here refers to first player turn and second player turn respectivly
    T1:int = int(input("Player 1, please enter a number from 1 to 10\n"))
    num += T1
    if (10 < T1 < 1) or (num > 100):
        if num > 100:
            print("Progress overflow\n")
        # this line is to return num to it's value before last increment
        num:int = int(saver)
        print("Invalid input, try again!\n")
        continue
    if num == 100:
        print("Player 1 wins, congrats!\n")
        break

    # This line to represent progress after addition process
    print("Progress:", num, "\n")

    saver:int = int(num)
    T2:int = int(input("Player 2, please enter a number from 1 to 10\n"))
    num += T2
    while (10 < T1 < 1) or (num > 100):
        if num > 100:
            print("Progress overflow\n")
        num:int = int(saver)
        print("Invalid input, try again!\n")
        T2:int = int(input())
        num += T2
    if num == 100:
        print("Player 2 wins, congrats!\n")
        break
    print("Progress:", num, "\n")
