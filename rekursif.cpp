#include <iostream>
#include <vector>
using namespace std;

// Fungsi rekursif untuk memeriksa apakah sebuah bilangan adalah prima
bool isPrimeRecursive(int num, int divisor) {
    if (num < 2) {
        return false;
    }
    if (divisor == 1) {
        return true;
    }
    if (num % divisor == 0) {
        return false;
    }
    return isPrimeRecursive(num, divisor - 1);
}

// Fungsi rekursif untuk mencari bilangan prima dalam array
void findPrimesRecursive(const vector<int>& arr, vector<int>& primes, int index) {
    if (index == arr.size()) {
        return;
    }
    if (isPrimeRecursive(arr[index], arr[index] - 1)) {
        primes.push_back(arr[index]);
    }
    findPrimesRecursive(arr, primes, index + 1);
}

int main() {
    vector<int> arr;
    vector<int> primes;
    int n;

    cout << "Masukkan jumlah elemen dalam array: ";
    cin >> n;

    cout << "Masukkan elemen-elemen array:\n";
    for (int i = 0; i < n; ++i) {
        int temp;
        cin >> temp;
        arr.push_back(temp);
    }

    findPrimesRecursive(arr, primes, 0);

    cout << "Bilangan prima dalam array adalah:\n";
    for (int prime : primes) {
        cout << prime << " ";
    }
    cout << endl;

    return 0;
}
