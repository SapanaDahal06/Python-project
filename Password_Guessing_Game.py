import random
easy_word = ["Instagram","Apple","Tiger","Adellise","BMW@456"]
medium_word = ["python","Avocado","Elephant","Dimond","Gen-Z"]
hard_word = ["Mountain","Dinosour","Adore","Torus","Isthmus"]
print("Welcome to the password Gussing game")
print("Choose a difficulty level: easy,medium or hard")

level = input('Enter difficulty:').lower()
if level == "easy":
    secret = random.choice(easy_word)
elif level == "medium":
    secret = random.choice(medium_word)
if level == "hard":
    secret = random.choice(hard_word)
else:
    print("Invalid choice.Defaulting to easy level")
    secret = random.choice(easy_word)
attempts = 0 
print("\nGuess the secret password")
#Game loop .
while True:
    guess = input("Enter your guess:").lower()
    attempts +=1
    
    if guess == secret:
        print('Congratulations you guessed it in{attempts} attempts.')
        break
    #Give a hint . show which letter are corect .
    hint = ""
    for i in range(len(secret)):
        if i <len(guess)and guess[i] ==secret[i]:
            hint+= guess[i]
        else:
            hint += "_"
            print("Hint:"+hint)
            
            print("Game Over") 
        
        