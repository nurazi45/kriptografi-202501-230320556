# Laporan Praktikum Kriptografi
Minggu ke-: 15  
Topik: Proyek Kelompok – TinyCoin ERC20  
Nama: Nur AZIZAH  
NIM: [230320556 
Kelas: 5dsra 

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1.Mengembangkan proyek sederhana berbasis algoritma kriptografi.
2.Mendokumentasikan proses implementasi proyek ke dalam repository Git.
3.Menyusun laporan teknis hasil proyek akhir.

---

## 2. Dasar Teori
RC20 Token Standard ERC20 (Ethereum Request for Comment 20) adalah standar teknis untuk fungible tokens (token yang dapat dipertukarkan) pada blockchain Ethereum. Standar ini mendefinisikan sekumpulan fungsi wajib yang harus diimplementasikan oleh smart contract, seperti totalSupply, balanceOf, transfer, approve, transferFrom, dan allowance. Dengan mengikuti standar ini, token baru dapat dipastikan kompatibel dengan berbagai dompet digital (wallet) dan bursa pertukaran (exchange) tanpa perlu penyesuaian teknis yang rumit. Smart Contract dan Solidity Smart contract adalah program komputer yang berjalan di atas blockchain yang mengeksekusi instruksi secara otomatis ketika kondisi tertentu terpenuhi. Solidity adalah bahasa pemrograman berorientasi objek tingkat tinggi yang digunakan untuk menulis smart contract pada platform Ethereum. Solidity versi 0.8.0 ke atas memiliki fitur keamanan bawaan, seperti pengecekan overflow/underflow aritmatika secara otomatis, yang meningkatkan keamanan kontrak dibandingkan versi sebelumnya.

OpenZeppelin Library OpenZeppelin adalah perpustakaan (library) standar industri untuk pengembangan smart contract yang aman. Dalam praktikum ini, kontrak ERC20 tidak ditulis dari nol, melainkan mewarisi (inherit) dari implementasi OpenZeppelin. Pendekatan ini meminimalkan risiko celah keamanan (bugs) karena menggunakan kode yang telah diaudit secara luas oleh komunitas global.

---

## 3. Alat dan Bahan
1.Perangkat Lunak:
Web Browser (Google Chrome / Brave / Edge).
Remix IDE (Lingkungan pengembangan terintegrasi berbasis web).
Metamask (Ekstensi dompet kripto untuk interaksi dengan testnet).
2.Bahasa Pemrograman & Library:
Solidity Compiler versi ^0.8.0.
OpenZeppelin Contracts (diimpor langsung melalui Remix).
3.Jaringan:
Remix VM (untuk pengujian lokal) atau Testnet Ethereum (Sepolia/Holešky) untuk verifikasi.

---

## 4. Langkah Percobaan
1.Persiapan Lingkungan: Membuat struktur folder praktikum/week15-tinycoin-erc20/contracts/ dan menyiapkan file laporan.md.
2.Penulisan Kode: Membuat file TinyCoin.sol di Remix IDE dan menyalin kode kontrak yang mengimpor modul ERC20 dari OpenZeppelin.
3.Kompilasi: Melakukan kompilasi kode menggunakan menu Solidity Compiler dengan versi 0.8.26 (atau yang sesuai dengan pragma).
4.Deployment:
Membuka menu Deploy & Run Transactions.
Memasukkan argumen initialSupply sebesar 100000000000.
Melakukan deploy kontrak.
Verifikasi (Opsional): Melakukan verifikasi kode sumber kontrak melalui layanan Sourcify atau Etherscan plugin di Remix (seperti yang terlihat pada log screenshot).
5.Pengujian Fungsi: Menguji fungsi balanceOf, transfer, dan melihat detail kontrak yang telah dideploy.

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 {
    // Constructor menerima input jumlah suplai awal token
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        // Mencetak (mint) token sejumlah initialSupply ke alamat penyebaran kontrak
        _mint(msg.sender, initialSupply);
    }
}
```
)

---

## 6. Hasil dan Pembahasan
Berdasarkan percobaan yang dilakukan di Remix IDE, smart contract TinyCoin berhasil di-deploy ke jaringan. Berikut adalah analisis dari hasil eksekusi:

Status Deployment: Kontrak berhasil dibuat pada alamat 0x2818B992A24c0F657FF853BB8c7B2B121829976D. Hal ini ditandai dengan ikon centang hijau pada log transaksi di bagian bawah Remix IDE.
Verifikasi Kontrak: Pada log output terlihat pesan [Sourcify] Verification Successful!. Ini menunjukkan bahwa kode sumber kontrak telah diverifikasi secara otomatis menggunakan layanan Sourcify, yang menjamin transparansi kode di blockchain.
Fungsionalitas Token: Pada panel Deployed Contracts, fungsi-fungsi standar ERC20 telah tersedia dan dapat digunakan:
Minting Awal: Constructor dijalankan dengan input 100000000000. Fungsi _mint memberikan saldo awal tersebut ke alamat pembuat kontrak (msg.sender).
Metadata: Nama token terdaftar sebagai "TinyCoin" dengan simbol "TNC".
Interaksi: Tombol oranye (approve, transfer) menunjukkan fungsi yang mengubah state blockchain (membutuhkan gas), sedangkan tombol biru (balanceOf, allowance) adalah fungsi view (gratis) untuk membaca data. Tidak ditemukan error saat proses kompilasi maupun deployment. Peringatan (warning) hanya terkait lisensi SPDX yang sudah diselesaikan dengan menambahkan komentar lisensi di baris pertama.


---

## 7. Jawaban Pertanyaan
1.Apa fungsi utama ERC20 dalam ekosistem blockchain? Fungsi utama ERC20 adalah menciptakan interoperabilitas. Sebelum adanya standar ini, setiap token memiliki cara unik untuk mentransfer atau mengecek saldo, sehingga dompet (wallet) dan bursa (exchange) harus menulis kode khusus untuk setiap token baru. Dengan ERC20, semua token "berbicara bahasa yang sama", memungkinkan integrasi instan dengan ribuan aplikasi terdesentralisasi (DApps), wallet, dan exchange.

2.Bagaimana mekanisme transfer token bekerja dalam kontrak ERC20? Mekanisme transfer tidak memindahkan token secara fisik antar dompet, melainkan hanya memperbarui "buku besar" (ledger) internal di dalam smart contract. Saat fungsi transfer(address recipient, uint256 amount) dipanggil:

Kontrak mengecek apakah pengirim (msg.sender) memiliki saldo yang cukup (>= amount).
Kontrak mengurangi saldo pengirim (balances[sender] -= amount).
Kontrak menambah saldo penerima (balances[recipient] += amount).
Event Transfer dipancarkan (emit) untuk mencatat aktivitas tersebut ke log blockchain.
3.Apa risiko utama dalam implementasi smart contract dan bagaimana cara mitigasinya? Risiko utama meliputi:
Reentrancy Attack: Penyerang memanggil kembali fungsi kontrak sebelum eksekusi sebelumnya selesai untuk menguras dana.
Mitigasi: Menggunakan pola Checks-Effects-Interactions atau modifier nonReentrant dari OpenZeppelin.
Integer Overflow/Underflow: Nilai angka melebihi kapasitas penyimpanan variabel.
Mitigasi: Menggunakan Solidity versi ^0.8.0 (yang sudah memiliki pengecekan otomatis) atau library SafeMath.
Access Control: Fungsi kritis (seperti mint) dapat diakses oleh sembarang orang.
Mitigasi: Menggunakan modifier onlyOwner (dari library Ownable). Dalam praktikum ini, risiko diminimalisir dengan menggunakan library OpenZeppelin yang telah teruji keamanannya dan Solidity versi 0.8.
---

## 8. Kesimpulan
Praktikum ini berhasil mengimplementasikan token ERC20 bernama TinyCoin (TNC) menggunakan Solidity dan Remix IDE. Penggunaan library OpenZeppelin terbukti mempermudah pengembangan smart contract sekaligus meningkatkan standar keamanan. Kontrak berhasil di-deploy pada alamat 0x2818B992A24c0F657FF853BB8c7B2B121829976D dan terverifikasi via Sourcify, menunjukkan kesiapan kontrak untuk berinteraksi dalam ekosistem Ethereum.

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

    week15-tinycoin-erc20 )
```
