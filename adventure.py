name = input("Type your name: ")
print("Welcome", name, "to this adventure!!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would like to go?  ").lower()

#conditions for left
if answer == "left":
    answer = input("You have come to a river, you can walk around it or swim across.  ")

    if answer == "swim":
        print("You swam across and were eaten by a crocodile!")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and died")
    else:
        print("A lion appeared behind you and killed you!!")

# conditons for right
elif answer == "right":
    answer = input("You have come to a bridge, it looks wobbly though, do you want to cross it or head back?  ")

    if answer == "back":
        print("You went back to main road and died")
    elif answer == "cross":
        answer = input("You crossed the bridge and met a stranger. Do you talk to him or not?  ")

        if answer == "yes":
            print("The stranger helped you")
        elif answer == "no":
            print("The starnger stabbed you in the back, literally!!")
    else:
        print("A lion appeared behind you and killed you!!")



else:
    print("You lose!!")

print("Thank you for playing", name,". Play again!")