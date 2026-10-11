alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "QMJZTGFKPWLSBOXNCRYEVHIADU"
text = "ERVYE DXVR SXFPJ"
result = ""
for letter in text:
    if letter == " ":
        result += " "
    else:
        position = cipher.index(letter)
        result += alphabet[position]

print("Ciphertext:", text)
print("Decrypted :",result)
