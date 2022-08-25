# Goldbachs-Conjecture

This code is set to solve https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=484 problem. The problem states that a number can be
expresed as the sum of two prime numbers. This conjecture was proposed by Goldbach to Euler, and thus it is called the Goldbach's Conjecture.

The code receives an input of a number which is then analyzed iteratively by a loop in which i is substracted from the original number. If i and the substraction are both
prime numbers, and their sum is equal to the original number, then the program outputs the sum of both numbers. On the other hand, in case said sum does not exist, 
"Goldbach's Theory is wrong." is printed instead.

For the prime test I used two functions to check if a number is prime or not. The first test is based on the number, for example if it ends in an even number or if it's
last digit is 5, then it is divisible by 2 or 5 respectively. This fast test works by using a modulus, and if the residue is 0 then we know it is not a prime. Nonetheless,
prime numbers can divide the original number such as 121 would not be prime because it is divisible by 11. To check for this case if none of the past checks returned true
or false I would use a sieve based function in which the program would analyze determine the primes and try to divide the number by them, if none had a residue of 0 then 
the number would be a prime.

That is the basic functionality of the program, I also used sets and a dictionary based cache for the repetitive prime calculations, this would make the code faster and it
takes around 0.9 seconds to run under the input of Online Judge. Ya arreglado
