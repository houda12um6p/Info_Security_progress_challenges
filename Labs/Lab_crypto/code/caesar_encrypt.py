text = "CRYPTO IS FUN UNTIL THE PROFESSOR SAYS QUIZ"
key = 4

result = ""
for letter in text:
    if letter == " ":
        result += " "
    else:
        result += chr((ord(letter) - ord("A") + key) % 26 + ord("A"))

print("Plaintext:", text)
print("Encrypted:", result)
