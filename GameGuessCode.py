def GuessGameModule() :
    import random
    print("Welcome to Number Guessing Game ")
    n = int(input("Enter max range of number to guess"))

    for i in range(0,5) :
        l1 = random.randint(0, n)
        print("Enter any number between 0 to ",n)
        i1 = int(input())
        if (i1 == l1) :
            print("Congratulations you won game ")
            break
        else :
            if (i1 > l1) :
                print("Secret number is greater than ",i1)
            if (i1 < l1):
                print("Secret number is lesser than ", i1)
            print("Try Again ")
    else :
        print("GAME OVER \nYour 5 attempts exhausted , Sorry , \nYou can Restart the game")