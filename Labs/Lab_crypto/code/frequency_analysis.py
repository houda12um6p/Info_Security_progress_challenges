text = """EKT YTJRTE BTYYQFT PY KPZZTO PO EKPY NQRQFRQNK.
STEETR GRTCVTOJD ZXTY OXE RTHTQS EKT IKXST LTD,
MVE PE FPHTY Q FXXZ YEQRE.
SXXL GXR JXBBXO IXRZY, RTNTQETZ NQEETROY,
QOZ YKXRE IXRZY.
IKTO DXV RTJXHTR EKT BTYYQFT,
EKT HPFTOTRT LTD KQY GXVR STEETRY."""
counts = {}
for letter in text:
    if letter.isalpha():
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
total=sum(counts.values())
sort_letters = sorted(counts.items(), key=lambda x: x[1], reverse=True)
for letter, count in sort_letters:
    percentage = count/total * 100
    print(letter,count,round(percentage, 2), " %" )
