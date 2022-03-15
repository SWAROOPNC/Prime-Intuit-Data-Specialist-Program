#coffee shop ,
#welcome message : to our shop
#wat like to have : coffee or tea #refer menu
#https://www.zomato.com/bangalore/namma-filter-coffee-jayanagar-bangalore
#our menu has beverages like Coffe Tea Milk , Please enter
#if coffe selected , print following types of coffe filter, black,
#please enter your selection
#ask for which milk , zerofat, toned, thick

#sugar , brown, jaggery,
#ask quantity
#store this module
#Main program call
def CCDwelcome() :
    print("Welcome to Cafe Coffee Day ")
    print("We have following beverages ")
    BevCode = int(input("Enter 1 for Coffee, 2 for Tea , 3 for Milk "))
    if (BevCode == 1) :
        Bev = "Coffee"
        print("You have Chosen ", Bev)
        price = 20
        print("Base Price for 1 unit of ", Bev, "is", price)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("We have Following Kind of Coffee ")
        BevKindCode = int(input("Enter 1 for Filter Coffee , 2 for Black Coffee & 3 for CCD Special Coffee "))
        if (BevKindCode == 1):
            BevKind = "Filter Coffee"
            print("You have Chosen ", BevKind, "type of", Bev)
        elif (BevKindCode == 2):
            BevKind = "Black Coffee"
            print("You have Chosen ", BevKind, "type of", Bev)
        elif (BevKindCode == 3):
            BevKind = "CCD Special Coffee"
            print("You have Chosen ", BevKind, "type of", Bev)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Choose Size ")
        SizeKindCode = int(input("Enter 1 for Mini , 2 for Medium &  3 for Maha "))
        if (SizeKindCode == 1):
            SizeKind = "Mini"
            print("You have Chosen ", SizeKind, "for", Bev)
        elif (SizeKindCode == 2):
            SizeKind = "medium"
            print("You have Chosen ", SizeKind, "for", Bev)
        elif (SizeKindCode == 3):
            SizeKind = "Maha"
            print("You have Chosen ", SizeKind, "for", Bev)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Choose the type of Milk you want ")
        MilkKindCode = int(input("Enter 1 for Toned Milk, 2 for Zero Fat Milk & 3 for CCD Special Milk "))
        if (MilkKindCode == 1):
            MilkKind = "Toned Milk"
            print("You have Chosen ", MilkKind, "for", Bev)
        elif (MilkKindCode == 2):
            MilkKind = "Zero Fat Milk"
            print("You have Chosen ", MilkKind, "for", Bev)
        elif (MilkKindCode == 3):
            MilkKind = "CCD Special Milk"
            print("You have Chosen ", MilkKind, "for", Bev)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Choose Sugar Kind ")
        SugarKindCode = int(input("Enter 1 for Normal Sugar , 2 for Sugar Less & 3 for Jaggery Sugar "))
        if (SugarKindCode == 1):
            SugarKind = "Normal Sugar"
            print("You have Chosen ", SugarKind, "for", Bev)
        elif (SugarKindCode == 2):
            SugarKind = "Sugar Less"
            print("You have Chosen ", SugarKind, "for", Bev)
        elif (SugarKindCode == 3):
            SugarKind = "Jaggery Sugar"
            print("You have Chosen ", SugarKind, "for", Bev)

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        Units = int(input("Enter number of quantity you want "))
        TotalPrice = price * Units
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("ORDER SUMMARY")
        print("Beverage ", Bev)
        print("Kind ", BevKind)
        print("Size ", SizeKind)
        print("Milk ", MilkKind)
        print("Sugar ", SugarKind)
        print("Unit price ", price)
        print("Quantities ", Units)
        print(" Total Payable amount is Rs ", TotalPrice, " Only")
    elif(BevCode == 2) :
        Bev = "Tea"
        print("You have Chosen ", Bev)
        price = 20
        print("Base Price for 1 unit of ", Bev, "is", price)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("We have Following Kind of Tea ")
        BevKindCode = int(input("Enter 1 for Classic Tea , 2 for Lemon Tea & 3 for Lemon Tea "))
        if (BevKindCode == 1):
            BevKind = "Classic Tea"
            print("You have Chosen ", BevKind, "type of", Bev)
        elif (BevKindCode == 2):
            BevKind = "Lemon Tea"
            print("You have Chosen ", BevKind, "type of", Bev)
        elif (BevKindCode == 3):
            BevKind = "Ginger Tea"
            print("You have Chosen ", BevKind, "type of", Bev)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Choose Size ")
        SizeKindCode = int(input("Enter 1 for Mini , 2 for Medium &  3 for Maha "))
        if (SizeKindCode == 1):
            SizeKind = "Mini"
            print("You have Chosen ", SizeKind, "for", Bev)
        elif (SizeKindCode == 2):
            SizeKind = "medium"
            print("You have Chosen ", SizeKind, "for", Bev)
        elif (SizeKindCode == 3):
            SizeKind = "Maha"
            print("You have Chosen ", SizeKind, "for", Bev)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Choose the type of Milk you want ")
        MilkKindCode = int(input("Enter 1 for Toned Milk, 2 for Zero Fat Milk & 3 for CCD Special Milk "))
        if (MilkKindCode == 1):
            MilkKind = "Toned Milk"
            print("You have Chosen ", MilkKind, "for", Bev)
        elif (MilkKindCode == 2):
            MilkKind = "Zero Fat Milk"
            print("You have Chosen ", MilkKind, "for", Bev)
        elif (MilkKindCode == 3):
            MilkKind = "CCD Special Milk"
            print("You have Chosen ", MilkKind, "for", Bev)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Choose Sugar Kind ")
        SugarKindCode = int(input("Enter 1 for Normal Sugar , 2 for Sugar Less & 3 for Jaggery Sugar "))
        if (SugarKindCode == 1):
            SugarKind = "Normal Sugar"
            print("You have Chosen ", SugarKind, "for", Bev)
        elif (SugarKindCode == 2):
            SugarKind = "Sugar Less"
            print("You have Chosen ", SugarKind, "for", Bev)
        elif (SugarKindCode == 3):
            SugarKind = "Jaggery Sugar"
            print("You have Chosen ", SugarKind, "for", Bev)

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        Units = int(input("Enter number of quantity you want "))
        TotalPrice = price * Units
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("ORDER SUMMARY")
        print("Beverage ", Bev)
        print("Kind ", BevKind)
        print("Size ", SizeKind)
        print("Milk ", MilkKind)
        print("Sugar ", SugarKind)
        print("Unit price ", price)
        print("Quantities ", Units)
        print(" Total Payable amount is Rs ", TotalPrice, " Only")

    elif(BevCode == 3) :
        Bev = "Milk"
        print("You have Chosen ", Bev)
        price = 20
        print("Base Price for 1 unit of ", Bev, "is", price)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("We have Following Kind of Milk ")
        BevKindCode = int(input("Enter 1 for Premium Milk , 2 for Horlicks & 3 for Boost "))
        if (BevKindCode == 1):
            BevKind = "premium milk"
            print("You have Chosen ", BevKind, "type of", Bev)
        elif (BevKindCode == 2):
            BevKind = "Horlicks"
            print("You have Chosen ", BevKind, "type of", Bev)
        elif (BevKindCode == 3):
            BevKind = "Boost"
            print("You have Chosen ", BevKind, "type of", Bev)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Choose Size ")
        SizeKindCode = int(input("Enter 1 for Mini , 2 for Medium &  3 for Maha "))
        if (SizeKindCode == 1):
            SizeKind = "Mini"
            print("You have Chosen ", SizeKind, "for", Bev)
        elif (SizeKindCode == 2):
            SizeKind = "medium"
            print("You have Chosen ", SizeKind, "for", Bev)
        elif (SizeKindCode == 3):
            SizeKind = "Maha"
            print("You have Chosen ", SizeKind, "for", Bev)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Choose the type of Milk you want ")
        MilkKindCode = int(input("Enter 1 for Toned Milk, 2 for Zero Fat Milk & 3 for CCD Special Milk "))
        if (MilkKindCode == 1):
            MilkKind = "Toned Milk"
            print("You have Chosen ", MilkKind, "for", Bev)
        elif (MilkKindCode == 2):
            MilkKind = "Zero Fat Milk"
            print("You have Chosen ", MilkKind, "for", Bev)
        elif (MilkKindCode == 3):
            MilkKind = "CCD Special Milk"
            print("You have Chosen ", MilkKind, "for", Bev)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Choose Sugar Kind ")
        SugarKindCode = int(input("Enter 1 for Normal Sugar , 2 for Sugar Less & 3 for Jaggery Sugar "))
        if (SugarKindCode == 1):
            SugarKind = "Normal Sugar"
            print("You have Chosen ", SugarKind, "for", Bev)
        elif (SugarKindCode == 2):
            SugarKind = "Sugar Less"
            print("You have Chosen ", SugarKind, "for", Bev)
        elif (SugarKindCode == 3):
            SugarKind = "Jaggery Sugar"
            print("You have Chosen ", SugarKind, "for", Bev)

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        Units = int(input("Enter number of quantity you want "))
        TotalPrice = price * Units
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("ORDER SUMMARY")
        print("Beverage ", Bev)
        print("Kind ", BevKind)
        print("Size ", SizeKind)
        print("Milk ", MilkKind)
        print("Sugar ", SugarKind)
        print("Unit price ", price)
        print("Quantities ", Units)
        print(" Total Payable amount is Rs ", TotalPrice, " Only")

