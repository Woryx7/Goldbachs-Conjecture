import math
known_primes = {1:False,2:True,3:True,4:False}

def digitsum(number):
    digitsum = 0
    digits = [int(d) for d in str(number)]
    for i in range(len(digits)):
        digitsum += digits[i]
    return digitsum
def sieve(number):
    limit = int(math.sqrt(number))
    listn = {2}
    primen = {2,3,5,7}
    for i in range(2,limit+1):
        listn.add(i)
    for j in primen:
        for k in primen:
            if k % j == 0 and k not in primen:
                k = 0
    while 0 in listn:
        listn.discard(0)
    for h in listn:
        if number % h == 0:
            return False
    return True
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
def iteration(ornum):
    golbach = False
    for i in range(1,ornum):
        if isprime(i)  and isprime(ornum-i):
            print(ornum,"=",i,"+",ornum-i)
            golbach = True
            break
        if i >= int(ornum/2):
            break
    if golbach == False:
        print("Goldbach's conjecture is wrong.")
def main():
    running = True
    while running:    
        ornum = int(input())
        if ornum != 0:
            iteration(ornum)
        else:
            break
main()
