import math

def digitsum(number):
    digitsum = 0
    digits = [int(d) for d in str(number)]
    for i in range(len(digits)):
        digitsum += digits[i]
    return digitsum

def sieve(number):
    limit = int(math.sqrt(number))
    listn = []
    primen = [2,3,5,7]
    for i in range(2,limit+1):
        listn.append(i)
    for j in range(len(primen)):
        for k in range(len(listn)):
            if listn[k] % primen[j] == 0 and listn[k] not in primen:
                listn[k] = 0
    while 0 in listn:
        listn.remove(0)
    for h in range(len(listn)):
        if number % listn[h] == 0:
            return False
    return True

def isprime(number):
    if number in [2,3,5,7]:
        return True
    elif number % 10 in [0,2,4,5,6,8]:
        return False
    elif digitsum(number) % 3 == 0:
        return False
    elif number == 1:
        return False
    else:
        return sieve(number)

def iteration(half,ornum):
    golbach = False
    for i in range(1,ornum):
        if isprime(i)  and isprime(ornum-i):
            print(ornum," = ","",i," + ",ornum-i)
            golbach = True
            break
    if golbach == False:
        print("Goldbach's conjecture is wrong")
def main():
    running = True
    while running:    
        ornum = int(input())
        if ornum != 0:
            iteration(int(ornum/2),ornum)
        else:
            raise SystemExit
main()