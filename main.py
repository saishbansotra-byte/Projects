print("***EXPENCE TRACKER APP***")
expences=[]
while True:
    print("***MENU***")
    print("1 : ADD EXPENCES ")
    print("2 : VIEW ALL EXPENCES ")
    print("3 : VIEW TOTAL EXPENCES ")
    print("4 : EXIT")
    choice=int(input("ENTER THE CHOICE HERE : "))
    if choice==1:
        print("***PLEASE ADD YOUR EXPENCES HERE*** ")
        date=input("DATA OF EXPENDITURE : ")
        category=input("ENTER THE CATEGORY OF EXPENDITURE : ")
        totalspend=input("ENTER THE TOTAL MONEY SPEND : ")
        expences={"date":date,
                  "category":category,
                  "totalspend":totalspend}
        # expences.append(expences)
        print("EXPENDITURE ADDED BROO")
    if choice==2:
        if totalspend==0:
            print("ADD EXPENCES FIRST BROO")
        else:
            print("HERE YOUR EXPENCES ")
            count=1
            for eachexpences in expences:
                print(f"THE EXPENCES ARE {expences["date"]},{expences["category"]},{expences["totalspend"]}")
                count=count+1
    elif choice==3:
        totalspend=0
        for eachexpences in expences:
            total=totalspend+eachexpences["totalspend"]
            print(total)
