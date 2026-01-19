# Laporan Praktikum Kriptografi
Minggu ke-: 11  
Topik: Secret Sharing (Shamir’s Secret Sharing) 
Nama: Nur Azizah 
NIM: 230320556 
Kelas: 5DSRA 

---

## 1. Tujuan
1.Menjelaskan konsep Shamir Secret Sharing (SSS).
2.Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
3.Menganalisis keamanan skema distribusi rahasia.


---

## 2. Dasar Teori
Shamir Secret Sharing (SSS) merupakan sebuah skema kriptografi yang dirancang untuk memecah suatu rahasia menjadi beberapa bagian (share) dan mendistribusikannya kepada sejumlah pihak. Rahasia tersebut hanya dapat dikembalikan ke bentuk semula apabila sejumlah minimum bagian tertentu (threshold) digabungkan. Skema ini didasarkan pada konsep polinomial dalam matematika, di mana nilai rahasia ditempatkan sebagai konstanta pada sebuah polinomial dengan derajat tertentu, kemudian setiap pihak memperoleh satu titik dari polinomial tersebut. Proses pemulihan rahasia dilakukan melalui interpolasi Lagrange ketika jumlah share yang memenuhi nilai threshold telah tersedia.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan secretsharing )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(import random
p = 2**521 - 1 # A large prime number threshold = 3 jumlah_share = 5

## rahasia yang akan dibagikan
secret_string = "KRIPTOGRAFIUPB2025/2026" secret = int.from_bytes(secret_string.encode(), 'big')

## fungsi untuk membantu
def eval_polynomial(coeffs, x, p): "Menghitung nilai f(x) = a0 + a1x + a2x^2 + ... (mod p)" result = 0 for power, coeff in enumerate(coeffs): result = (result + coeff * pow(x, power, p)) % p return result

def generate_shares(secret, k, n, p): "Membangun polinomial dan membagi shares" coeffs = [secret] + [random.randrange(1, p) for _ in range(k-1)] shares = [] for x in range(1, n + 1): y = eval_polynomial(coeffs, x, p) shares.append((x, y)) return shares

def lagrange_interpolation(shares, p): "Rekonstruksi secret dengan Lagrange Interpolation" secret = 0 for j, (xj, yj) in enumerate(shares): numerator = 1 denominator = 1 for m, (xm, _) in enumerate(shares): if m != j: numerator = (numerator * (-xm)) % p denominator = (denominator * (xj - xm)) % p lagrange_coeff = (numerator * pow(denominator, -1, p)) % p secret = (secret + yj * lagrange_coeff) % p return secret

proses
shares = generate_shares(secret, threshold, jumlah_share, p) print("Shares yang dihasilkan:") for share in shares: print(share)

milih minimal k shares
selected_shares = shares[:threshold] recovered_secret = lagrange_interpolation(selected_shares, p)

konversi kembali ke string
recovered_string = recovered_secret.to_bytes((recovered_secret.bit_length() + 7) // 8, 'big').decode() print("\nRahasia yang direkonstruksi:") print(recovered_string)
```
)

---

## 6. Hasil dan Pembahasan
(Berdasarkan hasil pengujian program Shamir Secret Sharing (SSS), sistem berhasil membagi sebuah rahasia berupa teks “KRIPTOGRAFIUPB2025/2026” menjadi lima buah share menggunakan skema ambang batas (k, n) = (3, 5). Rahasia terlebih dahulu dikonversi ke dalam bentuk bilangan bulat agar dapat diproses menggunakan operasi aritmatika modulo pada medan hingga dengan bilangan prima besar p = 2^521 − 1.

Proses pembangkitan share dilakukan dengan membentuk sebuah polinomial berderajat dua, di mana nilai rahasia disimpan sebagai konstanta polinomial, sedangkan koefisien lainnya dipilih secara acak. Setiap share yang dihasilkan berupa pasangan nilai (x, y) yang diperoleh dari hasil evaluasi polinomial pada nilai x tertentu. Nilai share yang dihasilkan berukuran sangat besar, yang disebabkan oleh penggunaan bilangan prima berukuran besar untuk menjaga keamanan sistem.

Selanjutnya, proses rekonstruksi rahasia dilakukan dengan memilih tiga share sesuai dengan nilai threshold. Rekonstruksi dilakukan menggunakan metode interpolasi Lagrange untuk menghitung kembali nilai konstanta polinomial. Hasil pengujian menunjukkan bahwa rahasia berhasil direkonstruksi secara tepat, ditandai dengan kembalinya teks rahasia “KRIPTOGRAFIUPB2025/2026” tanpa mengalami perubahan.

Hasil tersebut menunjukkan bahwa implementasi Shamir Secret Sharing telah berjalan dengan benar. Rahasia tidak dapat diperoleh apabila jumlah share yang digunakan kurang dari threshold, sedangkan penggunaan jumlah minimal share yang memenuhi threshold sudah cukup untuk mengembalikan rahasia secara utuh. Dengan demikian, skema ini memiliki sifat perfect secrecy dan mampu melindungi rahasia dari kebocoran sebagian data maupun akses oleh pihak yang tidak berwenang.
)

---

## 7. Jawaban Pertanyaan
(Pertanyaan 1: Apa keuntungan utama Shamir Secret Sharing dibandingkan membagikan salinan kunci secara langsung? Keunggulan utama Shamir Secret Sharing terletak pada peningkatan aspek keamanan, karena tidak ada satu pihak pun yang memegang kunci rahasia secara lengkap. Apabila terjadi kebocoran data pada satu atau beberapa pihak, rahasia tetap terlindungi selama jumlah share yang bocor belum memenuhi nilai threshold. Hal ini berbeda dengan pembagian salinan kunci secara langsung, di mana kebocoran pada satu pihak saja sudah cukup untuk mengompromikan seluruh sistem.

Pertanyaan 2: Apa peran threshold (k) dalam keamanan secret sharing? Threshold (k) berfungsi menentukan jumlah minimum share yang diperlukan untuk melakukan rekonstruksi rahasia. Parameter ini menjadi faktor utama dalam mengatur keseimbangan antara tingkat keamanan dan toleransi kesalahan. Semakin besar nilai k, semakin tinggi tingkat keamanan karena dibutuhkan lebih banyak pihak untuk bekerja sama, namun fleksibilitas sistem menjadi berkurang. Sebaliknya, nilai k yang lebih kecil meningkatkan kemudahan akses, tetapi berpotensi menurunkan tingkat keamanan.

Pertanyaan 3: Berikan satu contoh skenario nyata di mana Shamir Secret Sharing sangat bermanfaat. Shamir Secret Sharing sangat efektif diterapkan pada pengelolaan kunci utama dalam sistem perbankan atau pusat data. Dalam skenario ini, kunci enkripsi dibagi ke beberapa pejabat atau administrator, dan hanya dapat digunakan apabila sejumlah pihak yang telah ditentukan menggabungkan share yang mereka miliki. Pendekatan ini mencegah penyalahgunaan kunci oleh satu individu dan meningkatkan kontrol serta keamanan sistem.
)
---

## 8. Kesimpulan
(Berdasarkan hasil percobaan, Shamir Secret Sharing terbukti mampu membagi serta merekonstruksi rahasia secara aman melalui mekanisme threshold, di mana rahasia hanya dapat dikembalikan apabila jumlah minimum share telah terpenuhi. Penerapan polinomial dengan operasi modulo bilangan prima menunjukkan bahwa skema ini memiliki tingkat keamanan yang tinggi, karena kepemilikan share dalam jumlah kurang dari threshold tidak memberikan informasi apa pun mengenai rahasia. Oleh karena itu, SSS dinilai sangat efektif dalam meningkatkan keamanan distribusi kunci dan mencegah potensi penyalahgunaan oleh satu pihak. )

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
commit Secret Sharing
Author: Nur Azizah <nura56975@gmail.com>
Date:   2026-01-17

   week11-Secret Sharing-(Shamir’s Secret Sharing) )
```
