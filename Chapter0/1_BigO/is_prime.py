import math
from random import randrange

def isPrime(n):
    # If n == 1, which is not a prime.
    if n == 1:
        return False
    # If n == 2, which is THE ONLY PRIME for even.
    elif n == 2:
        return True
    # If bit-wise `n` start from `0`, e.g. `0100`, it is even.
    # `&` AND operator, 0 & 1 == False (0).
    # To summarize, this simply check n is even or not.
    # If n is even, then this is NOT PRIME.
    elif (n & 1) == 0:
        return False

    # We use Sieve of Eratosthenes.
    # For detail, please check here.
    # https://www.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/pi/level-4-sieve-of-eratosthenes

    sqrt = math.ceil(math.sqrt(n))
    print("sqrt: ", sqrt)
    print("Now we start...")

    # To iterate until sqrt value, we need to add +1 to the loop.
    for i in range(2, sqrt + 1):
        # check `n` is muiliple of `i` or not.
        print("check n is muiliple of ", i)
        if (n % i) == 0:
            return False

    return True

print('Enter # of candidates to test prime')
n = int(input())
print("int: ", n)

s = "Prime" if (isPrime(n)) else "Not prime"
print(s)