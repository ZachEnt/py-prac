# Enter a number and and find all the prime numbers leading to that number

numberIn = int(input("Enter a number: "))


isValid = False
primes = []

if numberIn > 2:
    isValid = True
    for n in range(2, numberIn + 1):
        isPrime = True
        for i in range(2, n):
            if n % i == 0:
                isPrime = False
                break
        if isPrime == True:
            primes.append(n)

if isValid:
    print(primes)
else:
    print("Invalid Requests")
