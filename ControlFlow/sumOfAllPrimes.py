def sumOfAllPrimes(n):
    sumPrime = 0 
    for i in range(2, n + 1):
        if isPrime(i): sumPrime += i
    return sumPrime

def isPrime(number):
    for n in range(2, number):
        if number % n == 0:
            return False
            
    return number > 1
