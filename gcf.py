def gcf(x,y):
    factors = []
    for i in range(x):
        if x % (i+1) == 0 and y % (i+1) == 0:
            factors.append(i+1)
    print(factors[-1])
gcf(int(input("give me number 1: ")), int(input("give me number 2: ")))

'''
    factors_x = []
    for i in range(1,x+1):
        if x % i == 0:
            factors_x.append(i)
    factors_y = []
    for i in range(1,y+1):
        if y % i == 0:
            factors_y.append(i)
    for i in range(1, int(len(factors_x)) + 1):
        a = i
        for i in range(int(len(factors_y))):
            if factors_x[-a] == factors_y[i]:
                print("the gcf is:")
                print(factors_y[i])
                return
'''