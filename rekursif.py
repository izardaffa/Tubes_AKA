def is_prime_recursive(n, divisor=None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor - 1)

def find_primes_recursive(arr, index=0, result=None):
    if result is None:
        result = []
    if index == len(arr):
        return result
    if is_prime_recursive(arr[index]):
        result.append(arr[index])
    return find_primes_recursive(arr, index + 1, result)

array = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
primes = find_primes_recursive(array)
print("Bilangan prima dalam array:", primes)
