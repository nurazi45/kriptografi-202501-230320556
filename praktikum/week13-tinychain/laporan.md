# Laporan Praktikum Kriptografi
Minggu ke-: 14 
Topik: TinyChain – Proof of Work (PoW)  
Nama: Nur Azizah  
NIM: 230320556 
Kelas:5dsra  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1.Menjelaskan peran hash function dalam blockchain.
2.Melakukan simulasi sederhana Proof of Work (PoW).
3.Menganalisis keamanan cryptocurrency berbasis kriptografi.


---

## 2. Dasar Teori
Blockchain adalah buku besar digital terdistribusi yang terdiri dari daftar catatan yang terus bertambah, disebut blok, yang dihubungkan dan diamankan menggunakan kriptografi. Setiap blok biasanya memuat hash kriptografis dari blok sebelumnya, stempel waktu (timestamp), dan data transaksi. Sifat keterhubungan ini membuat blockchain resisten terhadap modifikasi data; mengubah satu blok akan mengubah hash-nya dan membatalkan validitas seluruh blok berikutnya dalam rantai tersebut.

Salah satu komponen kunci dalam blockchain adalah fungsi hash (seperti SHA-256) yang mengubah input data menjadi string berukuran tetap. Selain itu, untuk menambahkan blok baru secara aman, digunakan mekanisme konsensus seperti Proof of Work (PoW). PoW mengharuskan komputer (miner) melakukan usaha komputasi untuk menemukan nilai variabel (biasanya disebut nonce) sehingga hash blok yang dihasilkan memenuhi target kesulitan (difficulty) tertentu, misalnya diawali dengan sejumlah angka nol.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Library Python: hashlib (untuk fungsi hashing SHA-256) dan time (untuk timestamp), yang merupakan library bawaan (standard library) Python.
- 

---

## 4. Langkah Percobaan
1.Membuat folder kerja (misalnya praktikum/week13-tinychain/src/).
2.Membuat file baru bernama tinychain.py.
3.Menuliskan kode program implementasi Blockchain sederhana yang mencakup:
-Class Block: Menyimpan atribut index, timestamp, data, previous_hash, nonce, dan hash.
-Metode calculate_hash: Menghasilkan hash SHA-256 dari properti blok.
-Metode mine_block: Melakukan Proof of Work dengan mencari nonce hingga hash memenuhi difficulty.
-Class Blockchain: Mengelola rantai blok (list) dan fungsi penambahan blok.
4.Menjalankan program melalui terminal Visual Studio Code dengan perintah: python tinychain.py atau melalui fitur run di editor.
M5.engamati output pada terminal untuk melihat proses mining dan hash yang dihasilkan.

---

## 5. Source Code


```python
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        # Loop hingga hash dimulai dengan sejumlah '0' sesuai difficulty
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4 # Tingkat kesulitan mining

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# Uji coba blockchain
my_chain = Blockchain()
print("Mining block 1...")
my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

print("Mining block 2...")
my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))


---

## 6. Hasil dan Pembahasan
1.Berdasarkan hasil eksekusi di atas, program berhasil menjalankan simulasi blockchain sederhana dengan rincian sebagai berikut:
2.Mining Block 1:
-Sistem memproses blok dengan data "Transaksi A → B: 10 Coin".
-Karena difficulty diatur ke angka 4, program melakukan perulangan (looping) mencari nilai nonce hingga ditemukan hash yang diawali dengan empat angka nol (0000).
-Hasil hash yang ditemukan: 0000191b815527... (Hash ini valid karena 4 digit pertamanya adalah 0).
3.Mining Block 2:
-Sistem memproses blok selanjutnya dengan data "Transaksi B → C: 5 Coin".
-Blok ini mengambil hash dari blok sebelumnya sebagai previous_hash untuk menjaga integritas rantai.
-Proses mining kembali dilakukan hingga ditemukan hash yang valid: 00003a046aec5b....


## 7. Jawaban Pertanyaan
1.Mengapa fungsi hash sangat penting dalam blockchain? Fungsi hash (seperti SHA-256) penting karena bertindak sebagai "sidik jari" digital yang unik untuk setiap blok. Hash menjamin integritas data; jika ada satu karakter saja pada data transaksi yang diubah, hash blok akan berubah total secara drastis (avalanche effect). Selain itu, hash digunakan untuk menghubungkan blok (chaining) melalui previous_hash, sehingga menciptakan rantai yang tidak dapat diputus atau disisipi tanpa merusak validitas seluruh rantai setelahnya.

2.Bagaimana Proof of Work mencegah double spending? Meskipun PoW utamanya adalah mekanisme konsensus dan pencegahan spam, ia membantu mencegah double spending (pengeluaran ganda) dengan membuat penulisan ulang sejarah transaksi menjadi sangat mahal secara komputasi. Jika penyerang ingin melakukan double spending (menggunakan koin yang sama untuk transaksi berbeda), mereka harus memodifikasi blok lama dan menambang ulang (re-mine) blok tersebut serta semua blok setelahnya agar rantai mereka menjadi valid dan lebih panjang daripada rantai utama (karena aturan Longest Chain). Dengan PoW, hal ini membutuhkan daya komputasi (>51% total jaringan) yang sangat besar dan nyaris mustahil dilakukan pada jaringan yang matang.

3.Apa kelemahan dari PoW dalam hal efisiensi energi? Kelemahan utama PoW adalah konsumsi energi yang sangat boros. Mekanisme ini mengharuskan jutaan perangkat keras komputer bekerja terus-menerus melakukan perhitungan matematis (tebak-tebakan nonce) secara brute force. Sebagian besar energi ini terbuang karena hanya satu penambang yang berhasil menemukan hash yang valid, sementara usaha komputasi penambang lain menjadi sia-sia untuk blok tersebut. Hal ini memicu dampak lingkungan yang signifikan.
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
Date:   2026-01-28

    TinyChain – Proof of Work (PoW) )
```
