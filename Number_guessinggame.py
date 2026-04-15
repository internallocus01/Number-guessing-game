print("-----NUMBER GUESSING GAME-----")
import random
x = random.randint(1,100)
choice = input("Enter choice(easy/medium/hard):")
while choice != "easy" and choice != "medium" and choice != "hard":
    print("Please enter a valid choice")
    choice = input("Enter choice(easy/medium/hard):")
num = int(input("Guess a number:")) 
attempts = 0  
if choice == "easy":   
    limit = 20
elif choice == "medium":
    limit = 15
elif choice == "hard":
    limit = 5
while num != x and attempts < limit:
        if num > x:
            print("Incorrect guess try lower numbers")
        else:
            print("Incorrect guess try higher numbers")
        num = int(input("Guess a number again:"))
        attempts = attempts + 1      
if num == x:
    print("\nThat is a correct guess")
    print(f"You got it in {attempts} attempts")
else:
    print("\nFailed!Run out of attempts,TRY AGAIN")
#Add a little complexity later like limit attempts✓,difficulty levels(easy,medium or hard) and asking if the user want to play again

    