def GuessGameModule() :
    import random
    print("Welcome to Number Guessing Game ")
    n = int(input("Enter max range of number to guess"))
    l1 = random.randint(0,n)
    for i in range(0,5) :
        print("Enter your guess number between 0 to ",n)
        i1 = int(input())
        if (i1 == l1) :
            print("Congratulations you won game as your guess was correct ")
            break
        else :
            if (l1 > i1) :
                print("Secret number is greater than ",i1)
            if (l1 < i1):
                print("Secret number is lesser than ", i1)
            if(i!=4) :
                print("Try Again ")
    else :
        print("GAME OVER \nSecret Number was ",l1,"\nYour 5 attempts exhausted , Sorry , \nYou can Restart the game")