import hashlib
import random

class AppTools:
    def __init__(self):
        self.key = random.randint(1, 25)

    def crypt(self, text: str):
        """Encrypts text using a Caesar cipher with a new random key."""
        self.key = random.randint(1, 25)
        encrypted = ""
        for char in text:
            if char.isalpha():
                shift = self.key % 26
                base = ord('A') if char.isupper() else ord('a')
                encrypted += chr((ord(char) - base + shift) % 26 + base)
            else:
                encrypted += char
        return encrypted

    def decrypt(self, text: str, key: any):
        try:
            k = int(key)
        except (ValueError, TypeError):
            return "Invalid Key"
            
        decrypted = ""
        for char in text:
            if char.isalpha():
                shift = k % 26
                base = ord('A') if char.isupper() else ord('a')
                decrypted += chr((ord(char) - base - shift) % 26 + base)
            else:
                decrypted += char
        return decrypted

    def hash(self, text: str):
        """Generates a SHA-256 hash of the given text."""
        if not text:
            return ""
        return hashlib.sha256(text.encode()).hexdigest()

    def compare_hash(self, text: str, hash_to_compare: str):
        """Compares the hash of the given text with a provided hash."""
        return self.hash(text) == hash_to_compare