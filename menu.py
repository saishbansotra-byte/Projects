print("====WELCOME TO THE RESTRAUNT'S MENU OPTION==== ")

items={"PIZZA":200,
        "PASTA": 150,
        "COFFEE":100,
       "MAGGI":40,
       "COKE":20}
print(items)
total=0
a=input("WHAT WOULD YOU LIKE TO ORDER SIR : ")
if a in items:
    print(f'YOU ITEM {a} HAS BEEN ADDED SUCESSFULLY ')
    total+=items[a]
    print("===========================================")
else:
     print(f"ITEM {a} IS NOT AVAILABLE NOW ")
     print("===========================================")
while True:
    b=input("WOULD YOU LIKE TO ORDER ANYTHING ELSE SIR : YES / NO ")
    if b=="YES":
        c=input("WHAT ELSE YOU WOULD LIKE TO ORDER SIR : ")
        if c in items:
            print(f"YOUR ITEM {c} IS SUCCESSFULLY ADDED ")
            total+=items[c]
            print("======================================")
    else:
        print("YOUR GRANDTOTAL IS ", total)
        print("THANKYOU FOR ORDERING ")
        print("============================")
        break

