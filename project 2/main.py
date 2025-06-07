import random
n=random.randint(0, 100)
guesses=0
a=-1
while(a != n):
    
    a=int(input("Guess the number: "))
    guesses +=1
    if(a>n):
        print("Lower number please")
        
    elif(a<n):
        print("Higher number please!")
    

    else:
        print(f"You have guessed the number {n} correctly in {guesses} attempts")