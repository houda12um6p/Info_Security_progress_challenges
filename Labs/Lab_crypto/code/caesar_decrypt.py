text = "GWCL JMBBMZ VWB JM CAQVO BWWTA BW AWTDM BPQA"
key = 8

result = ""
for letter in text:
    if letter == " ":
        result += " "
    else:
        result += chr((ord(letter) - ord("A") - key) % 26 + ord("A"))

print("Ciphertext:", text)
print("Decrypted :", result)
