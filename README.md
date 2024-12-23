![Poster disini](https://)

# Penjelasan kode

## Metode Rekursif `rekursif.py`

### Fungsi is_prime_recursive(n, divisor)

Fungsi rekursif untuk mengecek apakah sebuah bilangan adalah bilangan prima.

- `n` : Bilangan yang akan dicek.
- `divisor` : Pembagi yang digunakan untuk rekursi. Nilai awalnya adalah `None` dan akan diinisialisasikan dari hasil operasi `n - 1`.
- Fungsi akan mengembalikan `True` jika `n` merupakan bilangan prima, `False` jika `n` bukan bilangan prima.

Algoritma:

1. Jika `n` kurang dari atau sama dengan 1, kembalikan `False` karena bilangan prima harus lebih besar dari 1.
2. Jika divisor bernilai `None`, maka diatur menjadi `n - 1` untuk memulai pemeriksaan dari bilangan sebelum `n`.
3. Jika `divisor` sudah mencapai 1, kembalikan `True` karena berarti `n` hanya habis dibagi oleh 1 dan `n` sendiri.
4. Jika `n` habis dibagi oleh `divisor`, kembalikan `False`, artinya `n` bukan bilangan prima.
5. Panggil kembali fungsi `is_prime_recursive` dengan `divisor` dikurangi 1 untuk melanjutkan pemeriksaan.

### Fungsi find_primes_recursive(arr, index, result)

Fungsi rekursif untuk mencari bilangan prima dalam sebuah array.

- `arr` : Array bilangan yang akan diperiksa.
- `index` : Index saat ini dalam array. Nilai awalnya adalah 0.
- `result` : Nilai awailnya adalah `None` dan akan diinisialisasikan menjadi array kosong.

Algoritma:

1. Jika `result` bernilai `None`, maka diinisialisasi menjadi array kosong.
2. Jika `index` sudah mencapai panjang array, kembalikan `result` yang berisi daftar bilangan prima.
3. Jika elemen pada index saat ini merupakan bilangan prima (`is_prime_recursive` mengembalikan `True`), tambahkan elemen tersebut ke dalam `result`.
4. Panggil kembali fungsi `find_primes_recursive` dengan `index` bertambah 1 untuk memeriksa elemen berikutnya.

## Metode Iteratif `iteretif.py`

### Fungsi is_prime_iterative(n)

Fungsi untuk mengecek apakah sebuah bilangan adalah bilangan prima menggunakan metode iteratif.

- `n` : Bilangan yang akan dicek.
- Fungsi akan mengembalikan `True` jika `n` merupakan bilangan prima, `False` jika `n` bukan bilangan prima.

Algoritma:

1. Jika `n <= 1`, kembalikan `False` karena bilangan prima harus lebih besar dari 1.
2. Lakukan iterasi dari `i = 2` hingga akar kuadrat dari `n` (`int(n**0.5) + 1`). Pemeriksaan hingga akar kuadrat cukup karena faktor bilangan prima selalu simetris di sekitar akar kuadratnya.
3. Jika `n % i == 0` (artinya `n` habis dibagi oleh `i`), kembalikan `False`, karena `n` bukan bilangan prima.
4. Jika tidak ditemukan pembagi selain 1 dan `n` itu sendiri, kembalikan `True`.

### Fungsi find_primes_iterative(arr)

Fungsi untuk mencari bilangan prima dalam sebuah array menggunakan metode iteratif.

- `arr` : Array bilangan yang akan diperiksa.

Algoritma:

1. Inisialisasi list kosong `primes` untuk menyimpan bilangan prima yang ditemukan.
2. Lakukan iterasi pada setiap elemen `num` dalam array `arr`.
3. Gunakan fungsi `is_prime_iterative(num)` untuk memeriksa apakah elemen tersebut adalah bilangan prima.
4. Jika `num` adalah bilangan prima, tambahkan ke list `primes`.
5. Setelah semua elemen diperiksa, kembalikan list `primes`.
