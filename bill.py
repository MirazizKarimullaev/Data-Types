def service():
    bill = float(input("how much was the bill?"))
    quality = input("how was the service; bad, okay, good, or great? ")
    if quality == "bad":
        print("the total will be $" + str(bill))
    elif quality == "okay":
        print("the total will be $" + str(bill * 1.15))
    elif quality == "good":
        print("the total will be $" + str(bill * 1.20))
    elif quality == "great":
        print("the total will be $" + str(bill * 1.25))
    else:
        print("I dont understand can u repeat yourself")
        service()
service()