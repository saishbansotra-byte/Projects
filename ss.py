print("====TRIP CALCULATOR====")
expences=[]
while True:
    a={1:"ADD EXPENCES",
        2:"SPLIT CHECK :",
        3:"TOTAL EXPENDITURE TILL NOW ",
        4:'EXIT'}
    b=int(input("ENTER1: ADD EXPENCES\nENTER2: CHECK SPLIT\nENTER3: TOTAL EXPENDITURE TILL NOW\nENTER4:EXIT\n::"))
    print("I DECIDED TO ",a[b])
    if b==1:
        if (expences)==0:
            print("ADD SOME EXPENCES FIRST")
        else:
            date=input("ENTER THE DATE HERE : ")
            friends=int(input("ENTER THE NUMBER OF FRIENDS"))
            moneyspend=float(input("ENTER THE EXPENDITURE : RS."))
            expence={"date":date,
                    "friends":friends,
                    "moneyspend":moneyspend}
            expences.append(expence)
            print("EXPENCES SUCESSFULLY ADDED BROOO")
            print("=================================")
    elif b==2:
        total=0
        for items in expences:
            print(items["date"],items["friends"],items["moneyspend"])
            total+=items["moneyspend"]
            print(total)
            c=total/friends
            print("THE SPLIT WILL BE : ",c)
            print("======================")
    elif b==3:
       total=0
       for items in expences:
                   print(items["date"],items["friends"],items["moneyspend"])
                   total+=items["moneyspend"]
                   print(total)
    elif b==4:
        print("GOODBYE")
        print("=========")
        break
              



        