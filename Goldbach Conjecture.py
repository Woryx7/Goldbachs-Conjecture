import math
# cache variable to save known prime results
known_primes = {1:False,2:True,3:True,4:False}
# Function to find the sum of a number's digits
def digitsum(number):
    digitsum = 0
    digits = [int(d) for d in str(number)]
    for i in range(len(digits)):
        digitsum += digits[i]
    return digitsum
# Function to search for a number's divisors
def sieve(number):
    limit = int(math.sqrt(number))
    primes = {2}
    basic_primes = {2,3,5,7}
    for i in range(2,limit+1):
        primes.add(i)
    for j in basic_primes:
        for k in basic_primes:
            if k % j == 0 and k not in basic_primes:
                k = 0
    while 0 in primes:
        primes.discard(0)
    for h in primes:
        if number % h == 0:
            return False
    return True
# Quick primality test based of the number's composition
def isprime(number):
    if number in known_primes:
        return known_primes[number]
    else:
        if number in {2,3,5,7}:
            known_primes[number] = True
            return True
        elif number % 10 in {0,2,4,5,6,8}:
            known_primes[number] = False
            return False
        elif digitsum(number) % 3 == 0:
            known_primes[number] = False
            return False
        elif number == 1:
            known_primes[number] = False
            return False
        else:
            result = sieve(number)
            known_primes[number] = result
            return result
# Function to find the sum of two prime numbers to give the original number
def sum_search(number):
    golbach = False
    for i in range(1,number):
        if isprime(i)  and isprime(number-i):
            print(number,"=",i,"+",number-i)
            golbach = True
            break
        if i >= int(number/2):
            break
    if golbach == False:
        print("Goldbach's conjecture is wrong.")
# Main part of the code
def main():
    running = True
    while running:    
        number = int(input())
        if number != 0:
            sum_search(number)
        else:
            break
if __name__ == '__main__':
    main()
