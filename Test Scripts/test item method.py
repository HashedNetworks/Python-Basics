# import random
# import re

# rows = 3
# cols = 3

# symbols_count = {
#     'A' : 3,
#     'B' : 5,
#     'C' : 7,
#     'D' : 8
# }

# def get_slot_machine_spin():
#     symbols = []
#     for symbol, symbol_value in  symbols_count.items():
#         for _ in range(symbol_value):
#             symbols.append(symbol)



#     for i in range(3):
#         columns[i] = []


#   #  for _ in range(cols):
#         column = []
#         current_symbols = symbols[:]
#         for _ in range(rows):
#             symbol_1 = random.choice(current_symbols)
#             symbols.remove(symbol_1)

#       #  columns.append(column)

#     #return columns




import random

#get_slot_machine_spin()

columns = [[] , [] , []]
symbols = ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D']
for i in range(3):
    j=i
    new_symbols  = symbols[:]
    #print(columns)
    for j in range(3):
       symbol = random.choice(new_symbols)
       columns[j].append(symbol)
       new_symbols.remove(symbol)
print(columns)
# print(len(columns))
# print(len(columns[0]))

for row in range(len(columns[0])):
    for i, data in enumerate(columns):
        print( data[row], end =" | ")

    print()