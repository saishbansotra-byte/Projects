print("***WELCOME TO EXPENCE CALCULATOR ")
expenses=[]
while True:    
    a={1:"ADD EXPENDITURE :",
            2:"FIND THE TOTAL EXPENDITURE :",
            3:"EXIT"}
    b=int(input("""ENTER 1 : ADD EXP\nENTER 2: TOTAL SPEND\nENTER 3 : EXIT\n"""))
    print("I CHOOSE",a[b])
    
    if b==1:
        if expenses == 0:
            print("ADD EXPENCES FIRST ")
        else:
            print("***ADD EXPENCES HERE PLEASE***")
            date=input("ENTER THE DATA HERE :")
            commodity=input("ENTER THE COMMODITY HERE : ")
            cost=int(input("ENTER THE TOTAL COST HERE :  "))
            expense={"date":date,
                     "commodity":commodity,
                     "cost":cost}
            expenses.append(expense)
            print("EXPENCESES SUCESSFULLY ADDED ")
    elif b==2:
        if not expenses:
            print("NO EXPENSES FOUND")
        else:
            total=0
            print("\nDATE\t,\nCOMMODITY\t,\nCOST\t")
            for items in expenses:
                print( items["date"],items["commodity"],items["cost"])
                total+=items["cost"]
                print("TOTAL EXPENCES ARE ",total)
    elif b==3:
        break
    else:
        pass



 