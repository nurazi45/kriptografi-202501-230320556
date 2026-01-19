# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik:  Cipher Klasik 
Nama: Nur Azizah
NIM: 230320556 
Kelas: 5dsra  

---

## 1. Tujuan
1.Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
2.Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
3.Mengimplementasikan algoritma transposisi sederhana.
4.Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori
Caesar Cipher adalah salah satu teknik enkripsi substitusi paling sederhana dan tertua. Algoritma ini bekerja dengan menggeser setiap huruf dalam plaintext sejumlah posisi tertentu dalam alfabet.

Rumus Matematika:

Enkripsi: C = (P + k) mod 26
Dekripsi: P = (C - k) mod 26
Dimana:

C = Ciphertext
P = Plaintext
k = Kunci (shift value)
Karakteristik:

Menggunakan substitusi monoalfabetik
Hanya ada 25 kemungkinan kunci (mudah di-brute force)
Tidak aman untuk komunikasi modern
1.2 Vigenère Cipher
Vigenère Cipher adalah pengembangan dari Caesar Cipher yang menggunakan serangkaian Caesar Cipher berdasarkan huruf-huruf kunci. Cipher ini menggunakan substitusi polialfabetik.

Rumus Matematika:

Enkripsi: Ci = (Pi + Ki) mod 26
Dekripsi: Pi = (Ci - Ki) mod 26
Dimana:

Ki = huruf kunci ke-i (berulang jika plaintext lebih panjang)
Karakteristik:

Lebih kuat dari Caesar Cipher
Menggunakan kata/frasa sebagai kunci
Rentan terhadap Kasiski examination dan analisis frekuensi jika kunci pendek
1.3 Transposition Cipher
Transposition Cipher tidak mengubah huruf dalam plaintext, tetapi mengubah posisi/urutannya. Implementasi yang digunakan adalah Columnar Transposition.

Cara Kerja:

Tulis plaintext dalam bentuk grid dengan jumlah kolom = kunci
Baca per kolom untuk mendapatkan ciphertext
Untuk dekripsi, proses dibalik
Karakteristik:

Tidak mengubah frekuensi huruf (kelemahan utama)
Bisa dikombinasikan dengan cipher substitusi untuk keamanan lebih baik
Memerlukan kunci (jumlah kolom) yang tepat untuk dekripsi

---



---


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
Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher?
Caesar Cipher:

Kunci sangat terbatas: Hanya ada 25 kemungkinan kunci (shift 1-25), mudah diserang dengan brute force
Mudah dipecahkan: Dengan mencoba semua 25 kemungkinan, pesan dapat didekripsi tanpa kunci
Substitusi monoalfabetik: Setiap huruf selalu diganti dengan huruf yang sama, pola dapat dikenali
Tidak ada kerahasiaan kunci: Jika satu pesan dipecahkan, semua pesan dengan kunci sama dapat dibaca
Vigenère Cipher:

Analisis Kasiski: Jika kunci pendek, pola berulang dalam ciphertext dapat dideteksi untuk menemukan panjang kunci
Analisis frekuensi: Setelah panjang kunci diketahui, cipher dapat dipecah menjadi beberapa Caesar Cipher dan diserang dengan analisis frekuensi
Kunci berulang: Jika plaintext jauh lebih panjang dari kunci, pola pengulangan kunci dapat dieksploitasi
Rentan terhadap known-plaintext attack: Jika sebagian plaintext diketahui, kunci dapat ditemukan
3.2 Mengapa cipher klasik mudah diserang dengan analisis frekuensi?
Cipher klasik mudah diserang dengan analisis frekuensi karena:

Mempertahankan pola bahasa:

Dalam bahasa alami, huruf-huruf tertentu muncul lebih sering (misal: E, T, A dalam bahasa Inggris)
Caesar Cipher hanya menggeser, sehingga frekuensi relatif tetap sama
Huruf paling sering dalam ciphertext kemungkinan adalah huruf paling sering dalam bahasa tersebut yang digeser
Substitusi konsisten:

Setiap huruf plaintext selalu diganti dengan huruf ciphertext yang sama
Memudahkan identifikasi pola dan hubungan antar huruf
Pola kata dan bigram/trigram:

Pola kata umum (seperti "THE", "AND" dalam bahasa Inggris) dapat dikenali
Kombinasi huruf tertentu yang sering muncul bersama membantu mengidentifikasi substitusi
Ukuran sampel:

Dengan ciphertext yang cukup panjang, distribusi frekuensi menjadi lebih jelas dan analisis lebih akurat
Tidak ada difusi yang baik:

Perubahan satu huruf plaintext hanya mempengaruhi satu huruf ciphertext
Tidak ada pencampuran (mixing) informasi antar karakter
3.3 Bandingkan kelebihan dan kelemahan cipher substitusi vs transposisi
Aspek	Cipher Substitusi	Cipher Transposisi
Cara Kerja	Mengganti huruf dengan huruf/simbol lain	Mengubah urutan/posisi huruf
Kelebihan	• Mengubah frekuensi huruf jika polialfabetik
• Dapat membuat teks tidak terbaca sama sekali
• Implementasi sederhana	• Mempertahankan informasi asli (semua huruf ada)
• Dapat dikombinasikan dengan substitusi
• Relatif cepat untuk teks panjang
Kelemahan	• Rentan analisis frekuensi (monoalfabetik)
• Pola bahasa dapat terdeteksi
• Kunci terbatas (Caesar)	• Tidak mengubah frekuensi huruf
• Analisis frekuensi langsung membocorkan huruf
• Rentan analisis pola kata
Keamanan	Rendah-Sedang (tergantung kompleksitas)	Rendah (jika digunakan sendiri)
Penggunaan Modern	Tidak digunakan (terlalu lemah)	Tidak digunakan sendiri, tapi konsep diffusion masih relevan
Kombinasi	Dapat dikombinasikan dengan transposisi	Dapat dikombinasikan dengan substitusi

## 8. Kesimpulan
1.Implementasi berhasil: Ketiga algoritma cipher klasik (Caesar, Vigenère, dan Transposisi) berhasil diimplementasikan dan menghasilkan enkripsi/dekripsi yang benar.

2.Kelemahan fundamental: Cipher klasik memiliki kelemahan mendasar:
Caesar: terlalu sederhana (25 kemungkinan kunci)
Vigenère: rentan Kasiski examination
Transposisi: tidak mengubah frekuensi huruf

3.Nilai edukatif: Meskipun tidak aman untuk penggunaan modern, cipher klasik memberikan pemahaman dasar tentang konsep kriptografi:
Substitusi (confusion)
Transposisi (diffusion)
Pentingnya panjang kunci
Kelemahan pola deterministik

4.Relevansi modern: Konsep-konsep dari cipher klasik masih digunakan dalam algoritma modern:
AES menggunakan substitusi (S-Box) dan transposisi
Prinsip confusion dan diffusion dari Shannon
Pentingnya iterasi berulang

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

    week5-cryptosystem: implementasi Caesar Cipher dan laporan )
```
