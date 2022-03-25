def StasticsModule() :
    """

    """
    print("Taking List of scores as input")
    lus = []
    len1 = int(input("Enter num of scores in list "))
    for i in range(0,len1) :
        lus.append(float(input("Enter individual scores of dataset ")))
    print("----------------------------------------------------------------")
    print("Actual Data Set : ",lus)

    ls=[]
    ls=sorted(lus)
    print("Sorted Data Set : ",ls)
    print("----------------------------------------------------------------")
    print("MEASURE OF CENTRALITY")
    print("----------------------------------------------------------------")
    Mean = (sum(lus))/len1
    print("Mean = ",Mean)

    #calculate Median
    if(len1%2==1) :
        i=int((len1/2))
        Median = ls[i]
        print("Median = ",Median)
    else :
        i=int((len1/2))-1
        Median = ((ls[i]+ls[i+1])/2)
        print("Median = ",Median)

    #Find Mode
    """FIND MODE LATER """
    print(" To Find Mode ")
    Freq = []
    for i in lus :
        count=0
        for j in lus :
            if(i==j) :
                count=count+1
        Freq.append(float(count))
    print("     Actual DataSet : ",lus)
    print("     Freq__ DataSet : ",Freq)
    k= Freq.index(max(Freq))
    Mode = lus[k]
    print("Mode ",Mode)


    #COUNT FREQUENCY OF REPETATION OF EACH SCORE by comparing each element with other using a counter and put it to list
    #then get mode out of it
    print("----------------------------------------------------------------")
    print("MEASURE OF SPREAD")
    print("----------------------------------------------------------------")
    Min = min(ls)
    Max = max(ls)
    print("Minimum ",Min)
    print("Maximum ",Max)
    print("Range is ",Max-Min)
    print("----------------------------------------------------------------")
    #InterQuartileRange
    import math
    print("Quartiles")
    IQr0=ls[0]
    print("IQR0 0% ",IQr0)
    IQr1=ls[int(math.floor((len1)*0.25))]
    print("IQR1 25% ",IQr1)
    IQr2=ls[int(math.floor((len1)*0.5))]
    print("IQR2 50% ",IQr2)
    IQr3=ls[int(math.floor((len1)*0.75))]
    print("IQR3 75% ",IQr3)
    IQr4=ls[int(len1-1)]
    print("IQR4 100% ",IQr4)

    print("InterQuartile Range is from ",IQr1," to ",IQr3)
    print("----------------------------------------------------------------")
    #Percentile P given calculate lp , find yp
    print("To calculate score yp for Percentile rank P  ")
    P = int(input("Enter the percentile p to find "))
    j = int((len1*P)/100) - 1
    yp = ((ls[j] + ls[j + 1]) / 2)
    print("for Percentile Rank ",P,"Score is ",yp)


    print("----------------------------------------------------------------")
    OutL = []

    for num in ls :
        if (num<(-1.5*IQr1)) :
            OutLi = num
            OutL.append(OutLi)
    for num in ls :
        if (num>(1.5*IQr3)) :
            OutLi = num
            OutL.append(OutLi)
    print("Outliers",OutL)
    print("----------------------------------------------------------------")


    """#Trimmed Mean
    #remove outliers extreme both sides"""
    lso = ls[:]
    for m in OutL :
        lso.remove(m)
    print("List after removing outlier",lso)
    TrimmedMean = (sum(lso))/(len(lso))
    print("Actual Mean",Mean)
    print("Trimmed Mean",TrimmedMean)


    print("----------------------------------------------------------------")

    print("MEASURE OF CENTRALITY")

    print("----------------------------------------------------------------")

    print("Quintiles")
    IQn0=ls[0]
    print("IQn0 0% ",IQn0)
    IQn1=ls[int(math.floor((len1)*0.2))]
    print("IQn1 20% ",IQn1)
    IQn2=ls[int(math.floor((len1)*0.4))]
    print("IQn2 40% ",IQn2)
    IQn3=ls[int(math.floor((len1)*0.6))]
    print("IQn3 60% ",IQn3)
    IQn4=ls[int(math.floor((len1)*0.8))]
    print("IQn4 80% ",IQn4)
    IQn5=ls[int(len1-1)]
    print("IQn5 100% ",IQn5)


    print("----------------------------------------------------------------")

    print("Similarly We can Do For Deciles")
    print("----------------------------------------------------------------")
    print("Deviation")
    DevL =[]
    for i in range(0,len1) :
        devi=round(lus[i]-Mean,1)
        DevL.append(devi)
    print("Original Data Set ",lus)
    print("Deviation List",DevL)

    VarList = [round(x**2,2) for x in DevL]
    print("VarList (Sqr of Devl) ",VarList)
    Variance = (sum(VarList))/len1
    print("Variance ",Variance)
    StdDev = round((math.sqrt(Variance)),2)
    print("Standard Deviation ",StdDev)
