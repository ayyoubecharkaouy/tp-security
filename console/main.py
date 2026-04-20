import sys
import os

# Ajouter le dossier backend au path pour pouvoir importer AppTools
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from utils.tools import AppTools

def main():
    tools = AppTools()
    
    while True:
        print("\n========== Outil de Sécurité (Console) ========")
        print("1. Chiffrer un texte")
        print("2. Déchiffrer un texte")
        print("3. Hacher un texte")
        print("4. Comparer des hash")
        print("5. Quitter")
        
        choix = input("\n Choisissez une option (1-5): ")
        
        if choix == '1':
            text = input("Texte à chiffrer: ")
            encrypted, key = tools.crypt(text)
            print(f"\n Texte chiffré (Base64): {encrypted}")
            print(f"Clé de déchiffrement: {key}")
            
        elif choix == '2':
            text = input("Texte chiffré (Base64): ")
            key = input("Clé de déchiffrement: ")
            decrypted = tools.decrypt(text, key)
            print(f"\n Résultat: {decrypted}")
            
        elif choix == '3':
            text = input("Texte à hacher: ")
            hashed = tools.hash(text)
            print(f"\n Hash (PBKDF2): {hashed}")
            
        elif choix == '4':
            text = input("Texte original: ")
            hash_to_compare = input("Hash à comparer: ")
            match = tools.compare_hash(text, hash_to_compare)
            if match:
                print("\n Les hash correspondent !")
            else:
                print("\n Les hash ne correspondent pas.")
                
        elif choix == '5':
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
