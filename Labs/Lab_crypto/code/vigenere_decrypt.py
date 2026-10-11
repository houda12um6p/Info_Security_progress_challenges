ciphertext = """VVHWGQUIVYHIRSUPGTWXJSVIPCWIUPHGCIVIVVHPGHWITSDTRSDVUSYITMZL
GFHIXSUCVSDQOSPFGFVLQIOHEVHGMSDGJQRPWAQWGSNXJSPSUHIVGEXIPHVC
OPRPCBGYUSLXVCUIECYITHKIMSBAJSQXJSPIUGDKGPHGQAHWEZHETSQXGFWL
GOFGGGVAQFGIEZLTUS"""
ciphertext = ciphertext.replace("\n ", "")
key  = "CODE"
result =""

for i in range(len(ciphertext)):
    letter = ciphertext[i]
    key_letter = key[i % 4]
    shift = ord(key_letter) - ord("A")

    decrypted = chr((ord(letter)- ord("A") -shift) % 26 + ord("A"))


    result += decrypted

print("Key:", key)
print("Decrypted message:")
print(result)
