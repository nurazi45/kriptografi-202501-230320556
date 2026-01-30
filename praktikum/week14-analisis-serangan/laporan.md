# Laporan Praktikum Kriptografi
Minggu ke-: 14 
Topik: Analisis Serangan Kriptografi 
Nama: Nur Azizah 
NIM: 230320556 
Kelas: 5dsra

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1.Mengidentifikasi jenis serangan pada sistem informasi nyata.
2.Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
3.Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.


---

## 2. Dasar Teori
Fungsi Hash Kriptografis adalah algoritma matematika yang memetakan data dari ukuran berapa pun ke string bit dengan ukuran tetap (disebut hash atau digest). Sifat utamanya adalah satu arah (one-way), artinya secara komputasi tidak mungkin untuk membalikkan hash kembali ke input aslinya. Contoh algoritma klasik adalah MD5 dan SHA-1.

Dictionary Attack adalah metode pembobolan keamanan di mana penyerang mencoba menebak password dengan memasukkan setiap kata dalam daftar (kamus) yang telah disiapkan sebelumnya ke dalam fungsi hash, lalu mencocokkan hasilnya dengan hash target. Serangan ini sangat efektif terhadap password yang lemah atau umum.

Salting adalah teknik pertahanan di mana data acak (salt) ditambahkan ke input password sebelum di-hash. Hal ini memastikan bahwa dua user dengan password yang sama akan memiliki hash yang berbeda, sehingga menggagalkan serangan menggunakan Rainbow Table atau Dictionary Attack massa
---

## 3. Alat dan Bahan
Python 3.x (untuk menjalankan simulasi serangan).
Visual Studio Code (sebagai code editor).
Git (untuk version control).
Library hashlib (bawaan Python, tidak perlu instalasi tambahan).
File dictionary.txt (file teks sederhana berisi daftar password umum).

---

## 4. Langkah Percobaan
1.Membuat folder kerja baru dan file bernama linkedin_hack_demo.py.
2.Membuat file teks bernama dictionary.txt yang berisi daftar password umum (misal: 123456, password, linkedin, superman).
3.Menulis kode Python untuk mensimulasikan hash SHA-1 tanpa salt (seperti kasus LinkedIn 2012).
4.Menulis fungsi serangan dictionary attack untuk mencocokkan hash yang dicuri dengan daftar kata di dictionary.txt.
5.Menjalankan program dengan perintah python linkedin_hack_demo.py di terminal.
6.Mencatat hasil output ketika password berhasil "retak" (cracked).

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
import hashlib

# 1. Simulasi Database LinkedIn 2012 (SHA-1 tanpa Salt)
# Anggap ini adalah hash yang dicuri oleh hacker
target_passwords = {
    "user_ceo": "f35a6c343467b936d07d9195e26b89799298375e", # Hash dari 'linkedin'
    "user_admin": "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8", # Hash dari 'password'
    "user_budi": "7c4a8d09ca3762af61e59520943dc26494f8941b"  # Hash dari '123456'
}

def load_dictionary(filename):
    """Membaca file dictionary password umum"""
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def crack_hashes(target_db, dictionary_list):
    print("--- MEMULAI DICTIONARY ATTACK (SHA-1) ---")
    found_count = 0
    
    # Loop setiap kata di kamus
    for word in dictionary_list:
        # Ubah kata menjadi SHA-1 hash
        word_hash = hashlib.sha1(word.encode('utf-8')).hexdigest()
        
        # Cek apakah hash tersebut ada di database target
        for user, stolen_hash in target_db.items():
            if word_hash == stolen_hash:
                print(f"[BERHASIL] {user} -> Password asli: '{word}'")
                found_count += 1
                
    print(f"--- SELESAI. {found_count} password ditemukan. ---")

# Eksekusi Utama
if __name__ == "__main__":
    # Membuat dummy dictionary list (dalam praktik nyata menggunakan file .txt besar)
    common_passwords = ["qwerty", "123456", "iloveyou", "password", "linkedin", "admin123"]
    
    crack_hashes(target_passwords, common_passwords)
```
)

---

## 6. Hasil dan Pembahasan
Hasil percobaan menunjukkan bahwa password yang disimpan hanya dengan algoritma SHA-1 (tanpa salt) sangat mudah diretas menggunakan Dictionary Attack. Program berhasil menemukan password asli user karena input 123456 akan selalu menghasilkan hash SHA-1 yang sama persis (7c4a...).

Dalam kasus LinkedIn 2012, 6.5 juta password bocor karena:

1.Kelemahan Algoritma: SHA-1 sudah dianggap usang karena kecepatannya memungkinkan jutaan percobaan tebakan per detik.
2.Kelemahan Implementasi: Tidak adanya Salt (data acak tambahan). Jika ada salt, hacker harus membuat tabel hash baru untuk setiap user yang unik, yang mana membutuhkan waktu komputasi eksponensial.

---

## 7. Jawaban Pertanyaan
1.Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack? Banyak sistem lama (legacy) dibangun ketika daya komputasi komputer masih rendah, sehingga algoritma seperti MD5 atau SHA-1 dianggap aman pada masanya. Mereka rentan karena:
Hardware Modern: GPU modern dapat menghitung miliaran hash per detik, membuat brute force menjadi sangat cepat.
Biaya Migrasi: Mengganti algoritma hash di database produksi berisiko tinggi dan membutuhkan reset password massal seluruh pengguna, yang sering dihindari perusahaan demi kenyamanan user.
Kurangnya Salt: Sistem lama sering menyimpan hash "mentah" tanpa salt, memungkinkan penggunaan Rainbow Table.
2.Apa bedanya kelemahan algoritma dengan kelemahan implementasi?
Kelemahan Algoritma: Masalah fundamental pada matematika atau logika desain algoritma itu sendiri. Contoh: MD5 memiliki kerentanan collision (dua input berbeda menghasilkan hash yang sama). Solusinya adalah mengganti algoritma.
Kelemahan Implementasi: Algoritmanya aman, tetapi cara penggunannya dalam kode salah. Contoh: Menggunakan AES-256 (sangat aman) tetapi menyimpan kuncinya (key) di dalam kode sumber (hardcoded) atau menggunakan mode operasi ECB yang tidak menyembunyikan pola data.
3.Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan?
Crypto-Agility: Mendesain sistem agar algoritma kriptografi mudah diganti/diupdate tanpa merombak seluruh aplikasi.
Mengikuti Standar NIST/OWASP: Selalu menggunakan algoritma yang direkomendasikan saat ini (misal: beralih ke Argon2id untuk password, atau ECC untuk kunci publik).
Audit Berkala: Melakukan Penetration Testing rutin untuk mencari celah implementasi.
Persiapan Post-Quantum: Mulai menjajaki algoritma Quantum-Resistant untuk data yang bersifat rahasia jangka panjang.

---

## 8. Kesimpulan
Berdasarkan analisis kasus LinkedIn 2012 dan simulasi percobaan, dapat disimpulkan bahwa penggunaan fungsi hash cepat (seperti SHA-1 atau MD5) tanpa Salting sangat tidak aman untuk penyimpanan password. Serangan Dictionary Attack dapat memulihkan password asli dalam hitungan detik.

Rekomendasi Solusi: Sistem harus beralih menggunakan algoritma Slow Hashing yang didesain khusus untuk password, seperti Bcrypt, Scrypt, atau Argon2. Algoritma ini memiliki parameter "work factor" yang dapat disesuaikan untuk memperlambat proses hashing, sehingga serangan brute force menjadi tidak layak secara ekonomi dan waktu.

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
Author: Nur Azizah <email>
Date:   2026-01-30

    week14-analisis-serangan )
```
