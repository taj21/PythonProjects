import random
correct_answer= random.randint(1,10)
while True:
    try:
        user_guess = int(input("Choose a number between 1 to 10:  "))
        if 0<user_guess<11:
            if user_guess == correct_answer:
                print("You are a genius")
            break
        else:
            print("enter a number between 1 and 10")
    except ValueError:
        print("Please do not enter a text value")
        continue


