# Laporan Praktikum Kriptografi
Minggu ke-: 1 
Topik: Week1 
Nama: Nur Azizah 
NIM: 230320556 
Kelas: 5DSRA  

---

## 1. Tujuan
1.	Menjelaskan sejarah dan evolusi kriptografi dari masa klasik hingga modern.
2.	Menyebutkan prinsip Confidentiality, Integrity, Availability (CIA) dengan benar.
3.	Menyimpulkan peran kriptografi dalam sistem keamanan informasi modern.
4.	Menyiapkan repositori GitHub sebagai media kerja praktikum.

---

## 2. Dasar Teori
1.Kriptografi berasal dari bahasa Yunani, yaitu kryptos (tersembunyi) dan graphein (menulis), yang berarti menulis secara tersembunyi. Pada masa klasik, kriptografi digunakan untuk menjaga kerahasiaan pesan militer dan diplomatik. Metode awal yang digunakan adalah cipher substitusi dan transposisi, seperti Caesar Cipher, di mana huruf-huruf digeser beberapa posisi dalam alfabet, serta Vigenère Cipher, yang menggunakan kata kunci untuk mengatur pergeseran huruf.Seiring perkembangan teknologi, terutama setelah Perang Dunia II, kriptografi mulai menggunakan prinsip matematika dan komputerisasi. Kemunculan kriptografi modern ditandai dengan algoritma seperti DES (Data Encryption Standard), RSA (Rivest–Shamir–Adleman), dan AES (Advanced Encryption Standard). Kini, kriptografi tidak hanya digunakan untuk menyembunyikan pesan, tetapi juga untuk menjamin keamanan data digital, seperti enkripsi pada komunikasi internet, tanda tangan digital, dan sistem blockchain

2. Confidentiality (Kerahasiaan) → memastikan bahwa informasi hanya dapat diakses oleh pihak yang berwenang. Misalnya, data pengguna di sistem login harus dienkripsi agar tidak bocor.
Integrity (Integritas) → menjamin bahwa data tidak diubah tanpa izin selama proses penyimpanan atau pengiriman. Hal ini sering dijaga menggunakan hash function atau digital signature.
Availability (Ketersediaan) → memastikan bahwa sistem dan data selalu tersedia bagi pengguna yang berhak saat dibutuhkan, misalnya dengan menjaga server dari serangan denial of service (DoS).

3.kriptografi menjadi pondasi utama keamanan siber. Kriptografi melindungi data dari akses tidak sah, menjamin keaslian identitas pengguna, serta memastikan integritas dan keabsahan transaksi. Aplikasi modernnya dapat ditemukan dalam berbagai bidang, seperti komunikasi aman (HTTPS, VPN), penyimpanan data terenkripsi, tanda tangan digital, hingga blockchain dan cryptocurrency. Tanpa kriptografi, sistem keamanan modern seperti perbankan online, e-commerce, dan pertukaran data rahasia tidak akan dapat berfungsi dengan aman.

4.1.Pastikan akun GitHub aktif.
2.Fork repositori template dosen:"https://github.com/mhbahara/kriptografi-202501"
3.Ubah nama hasil fork menjadi:
4.Clone ke komputer lokal:
5.Buat folder untuk tugas minggu 1:

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Quiz Singkat
1.Siapa tokoh yang dianggap sebagai bapak kriptografi modern?
Tokoh yang dianggap sebagai bapak kriptografi modern adalah Whitfield Diffie dan Martin Hellman. Pada tahun 1976, mereka memperkenalkan konsep kriptografi kunci publik melalui karya berjudul “New Directions in Cryptography.” Penemuan ini menjadi dasar bagi berbagai sistem keamanan digital modern karena memungkinkan dua pihak berkomunikasi secara aman tanpa harus bertukar kunci rahasia secara langsung.

2.Sebutkan algoritma kunci publik yang populer digunakan saat ini.
Algoritma kunci publik yang populer digunakan saat ini antara lain RSA (Rivest–Shamir–Adleman), Elliptic Curve Cryptography (ECC), dan Diffie–Hellman Key Exchange. Ketiga algoritma ini banyak diterapkan dalam berbagai sistem keamanan seperti HTTPS, SSL/TLS, VPN, dan tanda tangan digital, karena mampu menjaga kerahasiaan dan keaslian data dalam komunikasi online.

3.Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
Perbedaan utama antara kriptografi klasik dan modern terletak pada pendekatannya. Kriptografi klasik menggunakan teknik sederhana seperti substitusi dan transposisi yang bekerja pada huruf atau teks, sedangkan kriptografi modern menggunakan konsep matematika kompleks dan komputasi digital. Jika kriptografi klasik bergantung pada kerahasiaan algoritma, kriptografi modern justru mengandalkan keamanan kunci serta kekuatan perhitungan matematis.
---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

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
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  


---
 

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20
comit : Nur Azizah
Author :Nur Azizah
Date : 2025-10-09

    week1-intro-cia)
```
