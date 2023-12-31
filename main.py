#Guess game

Secret_Number = 7
Guess_Count = 0
Guess_Limit = 3
while Guess_Count < Guess_Limit:
    Guess = int(input("Guess the number: "))
    Guess = int(Guess)
    Guess_Count = Guess_Count + 1
    if Guess == Secret_Number:
        print("Congrats! You Won")
        break
else:
    print("Sorry, You lost")
    
    

