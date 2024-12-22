def is_prime_recursive(n, divisor=None):
    """
    Fungsi rekursif untuk mengecek apakah sebuah bilangan adalah bilangan prima.
    :param n: Bilangan yang akan dicek.
    :param divisor: Pembagi yang digunakan untuk rekursi.
    :return: True jika bilangan adalah prima, False jika tidak.
    """
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
    """
    Fungsi rekursif untuk mencari bilangan prima dalam sebuah array.
    :param arr: Array bilangan yang akan diperiksa.
    :param index: Indeks saat ini dalam array.
    :param result: Hasil daftar bilangan prima yang ditemukan.
    :return: Daftar bilangan prima dalam array.
    """
    if result is None:
        result = []
    if index == len(arr):
        return result
    if is_prime_recursive(arr[index]):
        result.append(arr[index])
    return find_primes_recursive(arr, index + 1, result)

# Contoh penggunaan
array = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
primes = find_primes_recursive(array)
print("Bilangan prima dalam array:", primes)
