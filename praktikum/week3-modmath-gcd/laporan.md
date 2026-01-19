# Laporan Praktikum Kriptografi
Minggu ke-: 3 
Topik: modular math  
Nama: Nur Azizah  
NIM: 230320556  
Kelas: 5dsra 

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menyelesaikan operasi aritmetika modular.
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Modular arithmetic adalah sistem perhitungan di mana angka "berputar" kembali ke nol setelah mencapai nilai tertentu, yang disebut modulus. Ide utama dari aritmetika modular adalah bekerja dengan sisa hasil pembagian bilangan, bukan dengan bilangan itu sendiri.
GCD (Greatest Common Divisor) atau dalam bahasa Indonesia dikenal sebagai PBB (Pembagi Bersama Terbesar), adalah bilangan bulat terbesar yang dapat membagi dua bilangan bulat tanpa menyisakan sisa. GCD menjadi dasar penting dalam teori bilangan, termasuk dalam algoritma Euclidean yang digunakan untuk mencari GCD secara efisien.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan 
- so windows
---

## 4. Langkah Percobaan
praktikum/week3-modmath-gcd/
├─ src/
├─ screenshots/
└─ laporan.md
Membuat file src/modular_math.py.

Menyalin kode dari panduan praktikum ke dalam file tersebut.

Menjalankan program dengan perintah:

python src/modular_math.py

Melakukan screenshot hasil eksekusi dan menyimpannya di screenshots/hasil.png.

Melakukan commit ke repository GitHub dengan pesan:

week3-modmath-gcd

---

## 5. Source Code
Aritmetika Modular
def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)  # eksponensiasi modular

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))

GCD & Algoritma Euclidean
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))

Extended Euclidean Algorithm
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))  # hasil: 4

Logaritma Diskrit (Discrete Log)
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil: 4

---Uji program--
# Aritmetika Modular
def mod_add(a, b, n):
    return (a + b) % n

def mod_sub(a, b, n):
    return (a - b) % n

def mod_mul(a, b, n):
    return (a * b) % n

def mod_exp(base, exp, n):
    return pow(base, exp, n)  # eksponensiasi modular

print("7 + 5 mod 12 =", mod_add(7, 5, 12))          # Output: 0
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))          # Output: 11
print("7^128 mod 13 =", mod_exp(7, 128, 13))        # Output: 9


# GCD & Algoritma Euclidean
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))                 # Output: 6


# Extended Euclidean Algorithm & Invers Modular
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None  # Invers tidak ada jika gcd != 1
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))           # Output: 4


# Logaritma Diskrit (Discrete Log)
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))   # Output: 4


## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
1.Apa peran aritmetika modular dalam kriptografi modern?
Aritmetika modular memiliki peran penting dalam kriptografi modern karena menjadi dasar operasi matematika pada algoritma kunci publik seperti RSA dan Diffie–Hellman. Operasi modular memungkinkan pembentukan grup dan medan terbatas (finite fields) yang digunakan dalam pembuatan kunci, enkripsi, dan dekripsi. Dengan aritmetika modular, perhitungan tetap dalam rentang terbatas sehingga memudahkan proses komputasi dan menjaga keamanan informasi.

2.Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)?
Invers modular sangat penting dalam algoritma kunci publik seperti RSA karena digunakan dalam proses dekripsi. RSA mendefinisikan kunci publik dan kunci privat berdasarkan modulus dan eksponen, dan invers modular eksponen kunci publik terhadap totien modulus menghasilkan eksponen kunci privat. Tanpa invers modular, tidak mungkin mendapatkan kunci privat yang digunakan untuk membuka pesan terenkripsi, sehingga konsep ini mendasari keamanan algoritma RSA.

3.Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar?
Tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar adalah masalah komputasi yang sangat sulit dan memakan waktu. Kesulitan ini mendasari keamanan skema kriptografi berbasis logaritma diskrit seperti ElGamal dan DSA. Semakin besar modulus, semakin kompleks perhitungannya, sehingga memberikan tingkat keamanan yang tinggi.
---

## 8. Kesimpulan
Pada praktikum ini, mahasiswa telah berhasil menerapkan operasi aritmetika modular, algoritma Euclidean, dan logaritma diskrit menggunakan Python. Konsep-konsep ini menjadi dasar penting bagi algoritma kriptografi modern yang menggunakan operasi bilangan besar secara modular.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit ajijah
Author: Nur Azizah nura56975@gmail.com
Date:   2025-10-31

   week3-modmath-gcd: implementasi modular arithmetic, GCD, invers modular, dan logaritma diskrit