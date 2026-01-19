# Laporan Praktikum Kriptografi
Minggu ke-: 12
Topik: Aplikasi TLS & E-commerce 
Nama: Nur Azizah  
NIM: 230320556 
Kelas: 5dsra 

---

## 1. Tujuan
(Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
Menjelaskan enkripsi dalam transaksi e-commerce.
Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.)

---

## 2. Dasar Teori
Kriptografi pada layanan email dan protokol SSL/TLS berfungsi untuk menjamin kerahasiaan, keutuhan, serta keaslian data selama proses pertukaran informasi. Pada sistem email, teknologi seperti PGP dan S/MIME memanfaatkan enkripsi kunci publik sehingga hanya pihak penerima yang memiliki kunci yang sesuai yang dapat membaca isi pesan. Selain itu, tanda tangan digital digunakan untuk memastikan identitas pengirim serta mencegah pemalsuan pesan. Sementara itu, SSL/TLS berperan dalam mengamankan komunikasi antara klien dan server di jaringan internet dengan cara mengenkripsi data yang ditransmisikan, sehingga mampu menghindari penyadapan maupun serangan man-in-the-middle.

Dalam konteks transaksi e-commerce, enkripsi memiliki peran krusial dalam menjaga keamanan data sensitif, seperti informasi kartu kredit, data identitas pengguna, dan rincian transaksi. Penggunaan protokol HTTPS yang berbasis SSL/TLS memastikan bahwa data yang dikirimkan antara pengguna dan server tetap terlindungi dari upaya pembacaan maupun manipulasi oleh pihak yang tidak berwenang. Selain itu, penerapan kriptografi juga mendukung proses autentikasi serta non-repudiation, yang pada akhirnya meningkatkan tingkat kepercayaan antara penjual dan pembeli dalam aktivitas perdagangan daring.

Dari perspektif etika dan privasi, kriptografi menjadi sarana penting dalam melindungi hak privasi individu dengan mencegah akses ilegal terhadap data pribadi. Namun demikian, tantangan etis muncul ketika enkripsi tingkat tinggi dimanfaatkan untuk menutupi aktivitas yang melanggar hukum atau ketika pemerintah dan institusi tertentu berupaya membatasi maupun mengakses informasi yang terenkripsi. Oleh sebab itu, penerapan kriptografi perlu disertai dengan kebijakan yang adil dan bertanggung jawab agar tercipta keseimbangan antara keamanan, perlindungan privasi.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

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
Berdasarkan hasil pengecekan sertifikat digital pada website Shopee melalui browser, diketahui bahwa Shopee telah menggunakan sertifikat keamanan HTTPS yang valid dan terpercaya. Sertifikat ini berfungsi untuk menjamin keamanan pertukaran data antara pengguna dan server, terutama pada aktivitas sensitif seperti login dan transaksi online.

Issuer CA (Certificate Authority): Sertifikat Shopee diterbitkan oleh GlobalSign nv-sa dengan Common Name GlobalSign GCC R6 AlphaSSL CA 2023. GlobalSign merupakan salah satu Certificate Authority internasional yang terpercaya dan diakui oleh browser modern.

Masa Berlaku Sertifikat: Sertifikat mulai berlaku pada 24 Maret 2025 dan akan berakhir pada 25 April 2026, dengan masa berlaku sekitar satu tahun sesuai standar keamanan TLS saat ini.

Algoritma Enkripsi yang Digunakan: Sertifikat menggunakan algoritma RSA sebagai algoritma kunci publik dan SHA-256 sebagai algoritma hash untuk tanda tangan digital. Dalam komunikasi HTTPS, Shopee menggunakan protokol TLS dengan algoritma enkripsi simetris seperti AES untuk menjaga keamanan data selama proses transmisi.

Website yang menggunakan HTTPS memiliki tingkat keamanan yang jauh lebih baik dibandingkan website yang masih menggunakan HTTP. HTTPS memastikan data pengguna terenkripsi dan identitas website terverifikasi, sedangkan website tanpa HTTPS sangat rentan terhadap penyadapan dan manipulasi data.
---

## 7. Jawaban Pertanyaan
(Pertanyaan 1: Perbedaan mendasar antara HTTP dan HTTPS terletak pada aspek keamanannya. HTTP mentransmisikan data dalam bentuk teks biasa tanpa perlindungan enkripsi, sehingga informasi yang dikirim mudah untuk disadap atau dimanipulasi. Sebaliknya, HTTPS menggunakan protokol TLS untuk mengenkripsi data, sehingga informasi yang dipertukarkan menjadi lebih aman dan terlindungi dari akses pihak yang tidak berwenang.

Pertanyaan 2: Sertifikat digital memiliki peran penting dalam komunikasi berbasis TLS karena digunakan untuk melakukan verifikasi identitas suatu website. Dengan adanya sertifikat digital, pengguna dapat memastikan bahwa koneksi yang terjalin benar-benar menuju server yang sah, sehingga mencegah risiko komunikasi dengan pihak palsu atau berbahaya.

Pertanyaan 3: Kriptografi berkontribusi besar dalam menjaga privasi komunikasi digital dengan cara mengenkripsi data agar hanya dapat diakses oleh pihak yang memiliki otorisasi. Namun, di sisi lain, penerapan kriptografi yang kuat juga menimbulkan tantangan dari aspek hukum dan etika, karena dapat membatasi proses pengawasan oleh aparat penegak hukum serta memunculkan perdebatan terkait keseimbangan antara keamanan, perlindungan privasi, dan kepentingan publik.)
---

## 8. Kesimpulan
Kesimpulan: Berdasarkan percobaan dan analisis yang dilakukan, kriptografi terbukti berperan penting dalam menjaga keamanan komunikasi digital, baik pada email maupun transaksi e-commerce melalui penerapan SSL/TLS dan enkripsi data. Penggunaan HTTPS dan sertifikat digital mampu melindungi data sensitif dari penyadapan dan serangan pihak tidak berwenang. Namun, penerapan kriptografi juga menimbulkan tantangan etika dan hukum, sehingga diperlukan kebijakan yang seimbang antara perlindungan privasi, keamanan, dan kepentingan publik.

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
Date:   2026-01-17

    week12-apliaksi-tls: implementasi Aplikasi TLS & E-commerce Shopee  )
```
