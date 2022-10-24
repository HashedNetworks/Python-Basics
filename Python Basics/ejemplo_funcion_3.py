def funcion2():
    global x
    x = 100
    x = x + 10 
    print("X en funcion2 vale" , x)

def main():
    funcion2()
    global x
    x = x + 100 
    print("X en main vale" , x)

main()
