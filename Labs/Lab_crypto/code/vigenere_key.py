from collections import Counter
ciphertext = """VVHWGQUIVYHIRSUPGTWXJSVIPCWIUPHGCIVIVVHPGHWITSDTRSDVUSYITMZL
GFHIXSUCVSDQOSPFGFVLQIOHEVHGMSDGJQRPWAQWGSNXJSPSUHIVGEXIPHVC
OPRPCBGYUSLXVCUIECYITHKIMSBAJSQXJSPIUGDKGPHGQAHWEZHETSQXGFWL
GOFGGGVAQFGIEZLTUS"""
ciphertext = ciphertext.replace("\n", "")
key = ""
for i in range(4):
    group = ciphertext[i::4]
    most_frequent = Counter(group).most_common(1)[0][0]
    shift = (ord(most_frequent) - ord("E")) % 26
    key_letter = chr(ord("A") + shift)
    key += key_letter
    print("Group", i + 1)
    print("Most frequent letter:", most_frequent)
    print("Key letter:", key_letter)
    print()
print("Recovered key:", key)
