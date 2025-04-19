uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

def cesar_decrypt(cipherText, step):
    clearText = ""

    for letter in cipherText:
        if letter in uppercase:
            index = uppercase.index(letter)
            letter_decrypted = uppercase[(index - step) % 26]  # Soustraire pour déchiffrer
            clearText += letter_decrypted
        elif letter in lowercase:
            index = lowercase.index(letter)
            letter_decrypted = lowercase[(index - step) % 26]  # Soustraire pour déchiffrer
            clearText += letter_decrypted
        else:
            clearText += letter  # conserve les espaces, ponctuations, etc.

    return clearText

# Exemple d'utilisation
clearText = input("Entrer le texte à déchiffrer : ")
step = int(input("Entrer le pas : "))

# Déchiffrement
decryptedText = cesar_decrypt(clearText, step)
print("Texte déchiffré :", decryptedText)
