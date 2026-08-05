print("====BMI CALCULATOR====")
h=float(input('ENTER YOUR HEIGHT HERE : '))
w=float(input("ENTER YOUR WEIGHT HERE : "))
h=h/100
f=w/(h*h)
print("YOUR BMI IS ",round(f))
if f<18.5:
    print("AAP MACHIS HO MERE BHAI")
elif f>18.5 and f<24.9:
    print("YOU ARE BALANCED MY FRIEND ")
elif f>25 and f<29.9:
    print("YOU ARE OVERWEIGHT MY FRIEND ")
elif f>30 and f<100:
    print("AAP GIAN HO BHAI")
else:
    pass