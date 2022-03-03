"""This module searches for the highest diference number sum that will
prove the Goldbach Conjecture, in case it is false, it will return no
said sum."""

import math

# cache to save known prime results
known_primes = {1: False, 2: True, 3: True, 4: False}


def digitsum(number):
    """The digitsum function returns the sum of each digit in
    a number."""
    digits = [int(digit) for digit in str(number)]
    return sum(digits)


def sieve(number):
    """The sieve function allows to search if a number has
    divisors or not, it serves to prove a number's primality"""
    limit = int(math.sqrt(number))
    primes = {2}
    basic_primes = {2, 3, 5, 7}
    for prime in range(2, limit + 1):
        primes.add(prime)
    for j in basic_primes:
        for k in basic_primes:
            if k % j == 0 and k not in basic_primes:
                k = 0
    while 0 in primes:
        primes.discard(0)
    for prime in primes:
        if number % prime == 0:
            return False
    return True


def isprime(number):
    """This function returns if a number is prime or not, it performs a quick
    discard test to know if a number is prime, in case none was accesed it calls
    the sieve function to perform a more rigorous check"""

    if number in known_primes:
        return known_primes[number]
    else:
        if number in {2, 3, 5, 7}:
            known_primes[number] = True
            return True
        elif number % 10 in {0, 2, 4, 5, 6, 8}:
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


def sum_search(original_number):
    """The sum_search function handles the search for the sum of two primes
    whose sum will return back the orginal number"""
    golbach = False
    for number in range(1, original_number):
        if isprime(number) and isprime(original_number - number):
            print(original_number, "=", number, "+", original_number - number)
            golbach = True
            break
        if number >= int(original_number / 2):
            break
    if golbach is False:
        print("Goldbach's conjecture is wrong.")


def main():
    """The main function handles the input of data and packs all the other functions
    together"""
    running = True
    while running:
        number = int(input())
        if number != 0:
            sum_search(number)
        else:
            break


if __name__ == "__main__":
    main()
