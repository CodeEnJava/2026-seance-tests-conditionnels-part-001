

#assignation des variable

moyenne_1 = float (input("entrer  votre moyenne :"))

if moyenne_1 < 8 :
    print("refusé")
elif 8 <= moyenne_1 < 10 :
    print("admis au second groupe")
elif 10 <= moyenne_1 < 12 :
    print("admis")
elif 12<= moyenne_1 < 14 :
    print("admis mention assez bien ")
elif 14 <= moyenne_1 <16 :
    print("admis mention bien ")
elif 16 <= moyenne_1 :
    print("admis mention tres bien")


#solution 1 bis

moyenne_2 = float(input("entrer la moyenne : "))
if moyenne_2 in range ( 0,8) :
    print("refusé")
elif moyenne_2 in range (8,10):
    print("admis au second groupe")
elif moyenne_2 in range (10,12):
    print("admis")
elif moyenne_2 in range (12 , 14):
    print("admis mention assez bien ")
elif moyenne_2 in range (14,16):
    print("admis mention bien ")
else :
    print("admis mention tres bien")


#solution 2

moyenne_3 = float (input("entrer votre moyenne : "))

if moyenne_3 < 8 :
    print("refusé")
elif moyenne_3 < 10 :
    print("admis au second groupe")
elif moyenne_3 < 12 :
    print("admis")
elif moyenne_3 < 14 :
    print("admis mention assez bien")
elif moyenne_3 < 16:
    print("admis mention bien")
else :
    print("admis mention tres bien")


#solution 3 conditions imbriquées

moyenne_4 = float (input("entrer votre moyenne : "))

if moyenne_4 >= 8 :
    if moyenne_4 >= 10 :
        if moyenne_4 >= 12 :
            if moyenne_4 >= 14 :
                if moyenne_4 >= 16 :
                    print("admis mention bien")
                else:
                    print("admis mention bien")
            else:
                print("admis mention assez bien")
        else:
            print("admis")
    else:
        print("admis au second groupe")
else:
    print("refusé")


