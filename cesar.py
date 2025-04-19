uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

def cesar_encrypt(clearText, step):
    cipherText = ""

    for letter in clearText:
        if letter in uppercase:
            index = uppercase.index(letter)
            letter_encrypted = uppercase[(index + step) % 26]
            cipherText += letter_encrypted
        elif letter in lowercase:
            index = lowercase.index(letter)
            letter_encrypted = lowercase[(index + step) % 26]
            cipherText += letter_encrypted
        else:
            cipherText += letter  # conserve les espaces, ponctuations, etc.

    return cipherText


clearText = input("Entrer le texte à chiffrer : ")
step = int (input("Entrer le pas : "))
cipherText = cesar_encrypt(clearText, step)
print(cipherText)
