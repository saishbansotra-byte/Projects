a='***KAUN BANEGA CROREPATI***'
print(a.center(50))
q={1:"HOW MANY DAYS ARE THERE IN A WEEK ",
   2:"LARGEST STATE IN INDIA",
   3:"WHAT IS CALLED AS CHICKEN NECK OF INDIA",
   4:"SIDDU IS FAMOUS IN WHICH STATE",
   5:"WHICH SATE IS CALLED AS PARAGLIDING CAPITAL OF INDIA"}
o={1:"A-7,B-8,C-9,D-5",
   2:"A-GOA,B-RAJASTHAN,C-CHENNAI,D-DELHI",
   3:"A-JK , B- NORTH EAST, C- SIKKIM , D-HP",
   4:"A-JK , B-HP, C- UK , D- MUSSORIE",
   5:"A-MANALI, B- MCLEODGUNJ , C- BIR BILLING , D - UNA"}
a={1:"A",2:"B",3:"C",4:"B",5:"C"}
p={1:"$1000",2:"$2000",3:"$3000",4:'$4000',5:"$5000"}
print(q[1])
print(o[1])
c=input('ENTER YOUR ANSWER : ')
if c==a[1]:
    print('AAP JEET GAYE HAI ')
    print(p[1])
    print("-"*30)

    print("**/NEXT QUESTION/**")
    print(q[2])
    print(o[2])
    d=input("ENTER YOUR ANSWER : ")
    if d ==a[2]:
        print("AAP PHIR JEET GAYE")
        print("AAP JEET GAYE : ", p[2])
        print("-"*30)
        print("**/NEXT QUESTION/**")
        print(q[3])
        print(o[3])
        e=input("ENTER YOUR ANSWER : ")
        if e ==a[3]:
            print("AAP PHIR JEET GAYE")
            print("AAP JEET GAYE : ", p[3])
            print("**/NEXT QUESTION/**")
            print(q[4])
            print(o[4])
            f=input("ENTER YOUR ANSWER : ")
            if f ==a[4]:
                print("AAP PHIR JEET GAYE")
                print("AAP JEET GAYE : ", p[4])
                print("**/NEXT QUESTION/**")
                print(q[5])
                print(o[5])
                g=input("ENTER YOUR ANSWER : ")
                if g ==a[3]:
                    print("AAP PHIR JEET GAYE")
                    print("AAP JEET GAYE : ", p[5])
            
        
else:
    print("APSOS AAP HAAR GAYE ")
        
    