text = """EKT YTJRTE BTYYQFT PY KPZZTO PO EKPY NQRQFRQNK.
STEETR GRTCVTOJD ZXTY OXE RTHTQS EKT IKXST LTD,
MVE PE FPHTY Q FXXZ YEQRE.
SXXL GXR JXBBXO IXRZY, RTNTQETZ NQEETROY,
QOZ YKXRE IXRZY.
IKTO DXV RTJXHTR EKT BTYYQFT,
EKT HPFTOTRT LTD KQY GXVR STEETRY."""
mapping = {
    "T": "E",
    "E": "T",
    "R": "R",
    "Y": "S",
    "X": "O",
    "Q": "A",
    "K": "H",
    "O": "N",
    "Z": "D",
    "P": "I",
    "F": "G",
    "S": "L"
}
result =""
for letter in text:
    if letter in mapping:
        result += mapping[letter]
    elif letter.isalpha():
        result += "_"
    else:
        result += letter
print(result)
