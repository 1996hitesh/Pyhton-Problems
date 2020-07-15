#Write a program to accept 10 numbers through command
#line arguments and calculate the sum of prime numbers among them

from sys import argv

def isprime(n):
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6

    return True

sum = 0
for i in range(1,11):
    if (isprime(int(argv[i]))):
        sum += int(argv[i])
print(sum)
