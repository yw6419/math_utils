
def isprime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i)==0:
                print("False") 
        else:
                print("True")
    else:
        print("False")



