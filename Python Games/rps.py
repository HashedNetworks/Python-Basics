import random
# r > s, s > p, p > r

def rps_comp():
    comp_option = ["r" , "p" , "s"]
    comp_choice = random.choice(comp_option)
    return(comp_choice)

def rps_human():
    hum_choice = input(f"Select: Rock (r) , papper (p) or scissors (s): " )
    return(hum_choice)

def main():
    hum_points = 0
    comp_points = 0


    while (hum_points <= 2) and (comp_points <= 2):
        comp_choice = rps_comp()
        hum_choice = rps_human()

        if comp_choice == hum_choice:
            print("its a tie, no point no players")
            continue
        if (comp_choice == "r" and hum_choice == "s") or (comp_choice == "s" and hum_choice == "p") or (comp_choice == "p" and hum_choice == "r"):
            comp_points = comp_points + 1
            print("1 point for computer")
        else:
            hum_points = hum_points +1 
            print("1 point for human")
        score = print(f'Compter: {comp_points} "VS" Human: {hum_points}' )

    print(f"Someone won fp = " , {hum_points}  , "cp = " ,  {comp_points}  )


main()
        


