text = "ESP VPJ TD FYVYZHY ECJ MCFEP QZCNP"

for key in range(26):
    result = ""

    for letter in text:
        if letter == " ":
            result += " "
        else:
            result += chr((ord(letter) - ord("A") - key) % 26 + ord("A"))

    print("Key ", key , ":", result)
