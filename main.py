import timeit

from iteratif import is_prime_iterative
from rekursif import is_prime_recursive

array = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
        20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

time_rekursif = []
time_iteratif = []

for num in array:
    start_time = timeit.default_timer()
    result = is_prime_recursive(num)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    # print(f"Angka {num:2d}: {'PRIMA' if result else 'BUKAN PRIMA'} - Waktu: {execution_time:.8f} detik")
    time_rekursif.append(execution_time)

for num in array:
    start_time = timeit.default_timer()
    result = is_prime_iterative(num)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    # print(f"Angka {num:2d}: {'PRIMA' if result else 'BUKAN PRIMA'} - Waktu: {execution_time:.8f} detik")
    time_iteratif.append(execution_time)

print(f"\nAngka | is_prime | Rekursif | Iteratif")
print(f"-----------------------------------------------------")
for i in range(len(array)):
    print(f"{array[i]:2d} | {is_prime_recursive(array[i])} | {time_rekursif[i]:.8f} detik | {time_iteratif[i]:.8f} detik")