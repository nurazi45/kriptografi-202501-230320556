# Laporan Praktikum Kriptografi
Minggu ke-: 2 
Topik: crytosystem
Nama: Nur Azizah 
NIM: 230320556  
Kelas: 5dsra  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
Menggambarkan proses enkripsi dan dekripsi sederhana.
Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).


---

## 2. Dasar Teori
Cipher klasik merupakan teknik penyandian pesan yang digunakan pada masa awal perkembangan kriptografi. Prinsip dasarnya adalah mengganti atau mengacak huruf dalam pesan asli (plaintext) menjadi bentuk lain (ciphertext) menggunakan aturan tertentu agar isi pesan tidak mudah dipahami oleh pihak yang tidak berwenang. Beberapa contoh cipher klasik adalah Caesar Cipher, yang menggeser setiap huruf dengan jumlah tertentu dalam alfabet, dan Vigenère Cipher, yang menggunakan kunci berupa kata untuk melakukan pergeseran huruf secara berulang.

Konsep penting dalam cipher klasik adalah aritmetika modular, yaitu operasi matematika yang dilakukan dalam sistem bilangan tertentu (modulo n). Dalam konteks kriptografi, modular aritmetika digunakan untuk melakukan proses enkripsi dan dekripsi, seperti perhitungan pergeseran huruf. Misalnya, pada Caesar Cipher dengan pergeseran 3, huruf A (posisi 0) akan menjadi D (posisi (0+3) mod 26 = 3). Dengan konsep ini, proses penyandian dapat dilakukan secara sistematis dan mudah diimplementasikan dalam algoritma komputer.

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
# file: praktikum/week2-cryptosystem/src/simple_crypto.py

def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = "<nim><nama>"
    key = 5

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)


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
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

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
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
