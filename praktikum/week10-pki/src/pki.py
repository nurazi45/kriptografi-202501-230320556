from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Baca sertifikat
with open("cert.pem", "rb") as f:
    cert = x509.load_pem_x509_certificate(f.read())

# Ambil public key (CA / issuer)
public_key = cert.public_key()

# Verifikasi tanda tangan sertifikat
try:
    public_key.verify(
        cert.signature,
        cert.tbs_certificate_bytes,
        padding.PKCS1v15(),
        cert.signature_hash_algorithm,
    )
    print("Verifikasi berhasil: Sertifikat valid dan asli.")
except Exception as e:
    print("Verifikasi gagal: Sertifikat tidak valid.")