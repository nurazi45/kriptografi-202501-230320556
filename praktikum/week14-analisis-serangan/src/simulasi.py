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