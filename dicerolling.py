import random


def roll_dice():
    return random.randint(1, 6)


def dice():
    print("How many dices you want to roll?")
    n = int(input())
    dice_sum = 0

    for i in range(n):
        dice = roll_dice()
        dice_sum += dice
        print(dice, end=" ")
    print('\n')

    print("Your sum is", dice_sum, '\n')


def main():
    while True:
        dice()
        print('To restart type any button')
        print('To exit type "exit"')
        if input() == "exit":
            break


if __name__ == "__main__":
    main()
