
def isprime(num):
    #some ineficcient way to check if a number is prime ->boolean
    for i in range(2,num):
        #print("%i checking if devisable by"%i)
        if num%i == 0:
            return False
    return True


if __name__ == "__main__":
    for i in range(1, 1001):
        if isprime(i):
            print("%i is a prime number"%i)
        else:
            print("%i is not prime"%i)
