def CalcProFunc() :
    import random
    print(" Welcome to CalcPro Game ")
    print(" Keep Answering Correctly to stay in Game ")
    # Ans = Answer of player
    # Res = Result of Calculated statement
    Ans,Res=1,1 #just initialising Ans = Res to use it in while loop
    score = 0
    while(Ans==Res) :
        #n1 number 1
        #n2 number 2
        #on Operation Number 1 for + , 2 for - , 3 * , 4 /
        n1 = random.randint(1,9)
        n2 = random.randint(1,9)
        on = random.randint(1,4)
        if (on==1 ) :
            print("Calculate",n1," + ",n2,"=")
            Res = n1+n2
            Ans = int(input())
            if (Res != Ans ) :
                print("Wrong \n Correct Answer is ",Res)
                print("-------------------------------------")
                print("Game Over ")
                print("Your Score is ",score)
                print("-------------------------------------")
            else :
                score = score+1
                print ("Correct Answer ")
                print("Your Score is ",score)
                print("-------------------------------------")
                print("Your Next Question is ")
        elif (on==2 ) :
            print("Calculate",n1," - ",n2,"=")
            Res = n1-n2
            Ans = int(input())
            if (Res != Ans ) :
                print("Wrong \n Correct Answer is ",Res)
                print("-------------------------------------")
                print("Game Over ")
                print("Your Score is ",score)
                print("-------------------------------------")
            else :
                score = score+1
                print ("Correct Answer ")
                print("Your Score is ",score)
                print("-------------------------------------")
                print("Your Next Question is ")
        elif (on==3 ) :
            print("Calculate",n1," * ",n2,"=")
            Res = n1*n2
            Ans = int(input())
            if (Res != Ans ) :
                print("Wrong \n Correct Answer is ",Res)
                print("-------------------------------------")
                print("Game Over ")
                print("Your Score is ",score)
                print("-------------------------------------")
            else :
                score = score+1
                print ("Correct Answer ")
                print("Your Score is ",score)
                print("-------------------------------------")
                print("Your Next Question is ")
        elif (on==4 ) :
            print("Calculate",n1," / ",n2,"=")
            Res = int(n1/n2)
            Ans = int(input("Enter Only Integer Part "))
            if (Res != Ans ) :
                print("Wrong \n Correct Answer is ",Res)
                print("-------------------------------------")
                print("Game Over ")
                print("Your Score is ",score)
                print("-------------------------------------")
            else :
                score = score+1
                print ("Correct Answer ")
                print("Your Score is ",score)
                print("-------------------------------------")
                print("Your Next Question is ")