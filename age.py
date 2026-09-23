age = float((input("what is your age?")))
if age > 123:
    print("please dont lie saying your that old, the oldest person was 122")
elif age > 65 or age == 65:
    print("You are a senior citizen")
elif age > 18 or age == 18:
    print("you are an adult")
elif age > 0:
    print("you are a child")
elif age == 0:
    print("so your not born? if you are not one enter as a decimal")
    age = float((input("what is your age?")))
else:
    print("1 your not negitive age, 2 LIAR TRY AGAIN")
    age = float((input("what is your age?")))
 #float allows decimals, int is only whole numbers