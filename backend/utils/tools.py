import hashlib
import secrets
import hmac
import base64

class AppTools:
    def __init__(self):
        self.key = self.generate_key()

    def generate_key(self, length=32):
        """Generate a secure random key."""
        return secrets.token_bytes(length)

    # --- Encryption (simple XOR + base64 for demo, not industrial crypto) ---
    def crypt(self, text: str):
        """Encrypt text using XOR with a secure random key."""
        key = self.generate_key(len(text))
        encrypted_bytes = bytes([b ^ k for b, k in zip(text.encode(), key)])
        return base64.b64encode(encrypted_bytes).decode(), base64.b64encode(key).decode()

    def decrypt(self, encrypted_text: str, key: str):
        try:
            encrypted_bytes = base64.b64decode(encrypted_text)
            key_bytes = base64.b64decode(key)
        except Exception:
            return "Invalid input"

        decrypted_bytes = bytes([b ^ k for b, k in zip(encrypted_bytes, key_bytes)])
        return decrypted_bytes.decode(errors="ignore")

    # --- Hashing sécurisé avec salt ---
    def hash(self, text: str):
        """Hash with salt using SHA-256."""
        if not text:
            return ""

        salt = secrets.token_bytes(16)
        hashed = hashlib.pbkdf2_hmac('sha256', text.encode(), salt, 100000)

        return base64.b64encode(salt + hashed).decode()

    def compare_hash(self, text: str, stored_hash: str):
        """Secure comparison with salt."""
        try:
            data = base64.b64decode(stored_hash)
            salt = data[:16]
            real_hash = data[16:]

            test_hash = hashlib.pbkdf2_hmac('sha256', text.encode(), salt, 100000)

            return hmac.compare_digest(real_hash, test_hash)
        except Exception:
            return False
