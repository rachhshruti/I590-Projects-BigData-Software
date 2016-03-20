def fizzbuzz(n):
    for i in range(0,int(n)):
        if ((i+1)%2) == 0 and ((i+1)%3) == 0:
            print "fizzbuzz"
        elif ((i+1)%2) == 0:
            print "fizz"
        elif ((i+1)%3) == 0:
            print "buzz"
        else:
            print (i+1)
n = raw_input("Enter an integer n: ")
fizzbuzz(n)
