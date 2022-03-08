
#factorial
n=int(input("enter n for factorial "))

f=1
if n == 1 :
    print("factrial is 1")
else :
    for i in range(1,n+1):
        f=f*i
print("factorial is ",f)


# fibbonci series
"""In mathematics, 
the Fibonacci numbers, commonly denoted Fₙ, form a sequence, the Fibonacci sequence, in which each number is the sum of the two preceding ones.
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,"""
#2 preceding terms added
n = int (input("enter n for fibonanci "))
print("fibonanci series is ")
#consider nth = n_1 + n_2 ( _ as -)
n_2=0
n_1=1

if n ==1 :
    print(n_2)
else :
    for i in range (0,n+1):
        #initially n_2=0 , n_1=1
        print(n_2)
        nth = n_1+n_2  #nth = n_1 + n_2
        #update values for next iterion
        n_2=n_1 #now n_2 is n_1
        n_1=nth #n_1 is nth