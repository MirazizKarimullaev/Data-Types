def oddeven():
    y = input("will your num be pos or neg? ")
    if y == pos:
        x = input("give me a WHOLE POSITIVE number: ")
    if x.isnumeric() == True:
        x=int(x)
        if x % 2 == 0:
            print("even number")
        else:
            print("odd number")
    else:
        print("enter a whole pos number")
        oddeven()
    if y == neg:
        x = input("give me a WHOLE NEGITIVE number: ")
        try:
            x = int(x)
        if 
        if x % 2 == 0:
            print("even number")
        else:
            print("odd number")
    else:
        print("enter a whole pos number")
        oddeven()
oddeven()
NOT FINISHED