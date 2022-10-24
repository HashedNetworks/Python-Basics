#  Text based Slot Machine
#  The user will depositor amount of money and bet 1, 2 or three lines
#  If they won, we need to multiply the bet times the value of the line and add that to balance.
#  Allow them to play until money runs out, or cash out.
#  Steps:
#   1. Collect user deposit
#   2. Add that to balance
#   3. Allow to bet in 1 line or multiple line
#   4. See if they got any of those lines
#   5. Spin the slow machine
#   6. Generate differenet item in the slot machine reels
#   7. add whatever they won bacl to the balance account


import random

ROWS = 3
COLS = 3

symbols_count = {
    'A' : 3,
    'B' : 5,
    'C' : 7,
    'D' : 8
}


def get_deposit():
    
    while True:
        amount = input('Please enter your deposit amount: $')
        if  amount.isdigit() and int(amount) > 0:
            break
        else:
            print(f'This is not a valid input. Amount should be positive interger')
    print(f'Your Initial balance is ${amount}' )
    print('')

    return int(amount)

def get_lines():
     while True:
            lines = input(f'Please enter the number of lines you want to bet on (1-3): ')
            if  lines.isdigit() and ( 1 <= int(lines) <= 3) :
                break
            else:
                print(f'This is not a valid input. Please choose from 1-3')
                print('')

     return int(lines)

def get_bet():
    while True:
            bet = input('Please enter how much do you want to bet per line: $')
            if  bet.isdigit() and int(bet) > 0 :
                break
            else:
                print(f'This is not a valid input. Amount should be positive interger')
                print('')
  
    return int(bet)

def get_slot_machine_symbols():
    symbols = []
    for symbol, symbol_value in  symbols_count.items():             # Creating all posible symbols. .item() used to get key:value pair
        for _ in range(symbol_value):                               # Anonymous variable _.  We can use it If we don't need to count.
           symbols.append(symbol)
    return symbols

def get_slot_machine_spin(rows, cols, symbols):   # Spinning slot machine
    columns = []
    for col in range(rows):
        columns.append([])

    
    for i in range(cols):
        new_symbols  = symbols[:]
        for j in range(rows):
            symbol = random.choice(new_symbols)
            columns[j].append(symbol)
            new_symbols.remove(symbol)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, data in enumerate(columns):
            print( data[row], end =" | ")

        print()





def main():
    balance = get_deposit()     # Getting initial deposit
    lines = get_lines()         # Getting amount of line to bet
    bet = get_bet()             # Getting amount to bet
    total_bet= bet*lines        # Getting total bet per lines
    
    
    while total_bet > balance:
        print(f' You are betting a total of {total_bet}.  You cannot bet more that your current blance of ${balance} ')
        print('')
        bet = get_bet()
        total_bet= bet*lines
            
    print(f'You will be betting ${bet*lines}' )

    while True:
        game = input(f' Press Enter to spin again or letter q to quit: ')
        symbols = get_slot_machine_symbols()
        columns = get_slot_machine_spin(ROWS, COLS, symbols)    # Spinning slot machine
        print_slot_machine(columns)
        if game == 'q':
            break
        else:
            continue




main()