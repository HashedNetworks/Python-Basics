import random
import time

def guess(x):
    random_num = random.randint(1, x)
    return(random_num)


def main():
    num = int(input("Input a number to generate secret number: "))
    rand_num = guess(num)
    time.sleep(3)
    print("Generated!")
    print("Now try Guessing the random number")
    guess_num = 0

    while guess_num != rand_num:
        guess_num = int(input("Try guessing: "))
        if guess_num < rand_num:
            print("You number is lower than secret number, please try again")
        if guess_num > rand_num:
            print("You number is higher than secret number, please try again")      
    print("That is Correct!, the secret number is" , rand_num)

  
main()    