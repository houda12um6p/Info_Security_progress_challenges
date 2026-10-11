alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "QMJZTGFKPWLSBOXNCRYEVHIADU"
text = "KEEP THE SECRET SAFE"
result = ""

for letter in text:
    if letter == " ":
        result += " "
    else:
        position = alphabet.index(letter)
        result += cipher[position]



print("Plaintext:", text)
print("Encrypted :",result)
