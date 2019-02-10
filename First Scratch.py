######this is a program for finding the square root of perfect squares
x = int(input("""Enter a number  """))
if x < 0 :
    print("undefined")
else :
    ans = 0
    while ans*ans < abs(x):
        ans = ans + 1
        #print (ans)
    if ans*ans > abs(x):
        print("x is not a perfect square")
    else:
        print("the square root of " + str(x) + " is " + str(ans))