def is_prime_iterative(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_iterative(arr):
    primes = []
    for num in arr:
        if is_prime_iterative(num):
            primes.append(num)
    return primes

array = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
primes = find_primes_iterative(array)
print("Bilangan prima dalam array:", primes)
