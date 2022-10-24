import random
import time

def guess(x):
    random_num = random.randint(1, x)
    return(random_num)

#def computer(y):
#   comp_num = random.randint(1 , y)    comp_num = random.randint(1 , y)
#   return(comp_num)


def main():
    num = int(input("Input a number to generate secret number: "))
    rand_num = guess(num)
    time.sleep(3)
    print("Ramdon number between 1 and" , rand_num , "Generated!")
    print("Now try Guessing the random number")
    guess_num = num

    while guess_num != rand_num:
        if guess_num < rand_num:
            print(guess_num , rand_num, "You number is lower than secret number, please try again")
            guess_num = (guess_num + 1)
        if guess_num > rand_num:
            print(guess_num , rand_num, "You number is higher than secret number, please try again")
            guess_num = (guess_num - 1)      
    print("That is Correct!, the secret number is" , rand_num)

  
main()    