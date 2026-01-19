# Laporan Praktikum Kriptografi
Minggu ke-: 4 
Topik: Entropy & Unicity Distance  
Nama: Nur Azizah  
NIM: 230320556  
Kelas:5dsra  

---

## 1. Tujuan
1.Menyelesaikan perhitungan sederhana terkait entropi kunci.
2.Menggunakan teorema Euler pada contoh perhitungan modular & invers.
3.Menghitung unicity distance untuk ciphertext tertentu.
4.Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5.Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori
Teori entropi dalam kriptografi berasal dari konsep entropi informasi yang diperkenalkan Claude Shannon, yang mengukur tingkat ketidakpastian atau keacakan suatu data. Semakin tinggi entropi, semakin sulit diprediksi atau ditebak isi data tersebut. Dalam kriptografi, entropi penting untuk menghasilkan angka acak atau kunci yang kuat sehingga sistem kriptografi menjadi lebih aman terhadap serangan.

Unicity distance adalah konsep yang menunjukkan jumlah data ciphertext minimum yang diperlukan agar sebuah algoritma kriptografi dapat dilemahkan dan kunci enkripsi bisa ditemukan dengan hanya mencoba semua kemungkinan kunci. Intinya, ini mengukur batas seberapa banyak pesan yang bisa dienkripsi dengan satu kunci sebelum kunci tersebut mulai rentan dikorelasikan dan diketahui oleh penyerang. Unicity distance tergantung pada entropi sumber pesan dan ukuran kunci.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan 

---

## 4. Langkah Percobaan
praktikum/week4-entropy-unicity/
├─ src/
├─ screenshots/
└─ laporan.md


---

## 5. Source Code
## Perhitungan Entropi
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")

HK_caesar = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK_caesar))

HK_aes128 = entropy(2**128)
print("Unicity Distance untuk AES-128 =", unicity_distance(HK_aes128))

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")

## Menghitung Unicity Distance
def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))

## Analisis Brute Force
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
---

## 6. Hasil dan Pembahasan
Hasil eksekusi menunjukkan entropi Caesar Cipher sangat rendah (hanya 26 kemungkinan kunci), sehingga sangat muda ditembus brute force .
Pada AES-128, entropi sangat besar dan unicity distance tinggi menunjukkan cipher modern sangat kuat terhadap analisis maupun brute force.
Tidak ada error pada program, semua fungsi berjalan sesuai harapan dengan hasil numerik yang benar.

---

## 7. Jawaban Pertanyaan
Pertanyaan 1: Nilai entropi pada ruang kunci menunjukkan berapa banyak kemungkinan kunci yang dapat dipilih secara acak oleh algoritma kriptografi. Semakin besar nilai entropi, semakin sulit bagi seorang penyerang untuk menebak kunci yang benar secara acak, sehingga meningkatkan kekuatan keamanan sistem .
Pertanyaan 2: Unicity distance penting karena mengukur titik di mana jumlah ciphertext yang ada cukup untuk membedakan satu kunci yang valid di antara semua kemungkinan, menggunakan analisis statistik bahasa. Jika unicity distance kecil, cipher lebih mudah dipecahkan .
Pertanyaan 3: Brute force tetap menjadi ancaman pada sistem dengan ruang kunci kecil atau pengelolaan kunci yang buruk. Pada cipher lama seperti Caesar, brute force sangat efektif karena kunci sangat sedikit. Namun, pada cipher modern (AES atau RSA), brute force menjadi tidak praktis karena besarnya ruang kunci membuat waktu yang dibutuhkan melebihi umur alam semesta .

## 8. Kesimpulan
Pelaksanaan praktikum menunjukkan bahwa ukuran ruang kunci, entropi, dan unicity distance memegang peranan penting dalam menilai keamanan suatu kriptosistem. Cipher dengan entropi dan unicity distance rendah sangat rentan terhadap brute force dan analisis statistik, sedangkan cipher modern dengan entropi tinggi amat kuat melawan serangan tersebut .
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
commit abc12345
Author: Nur Azizah <nura56975@gmail.com>
Date:   2025-09-20

    week4-cryptosystem: implementasi entrophy unicity distance dan brute force
