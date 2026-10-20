from collections import Counter
from PIL import Image

width = 432
height = 475

with open("classified.enc", "rb") as f:
    data = f.read()

ciphertext = data[16:16 + width * height]

blocks =[
    ciphertext[i:i+16]
    for i in range(0, len(ciphertext), 16)
]

counts = Counter(blocks)
colors ={}

for i, (block, count) in enumerate(counts.most_common()):
    if i == 0:
        colors[block] = 255
    else:
        colors[block] = (i * 120) % 220 #

pixels = []
for block in blocks:
    pixels.extend([colors[block]] * 16) #

img=Image.new("L", (width, height))
img.putdata(pixels)
img.save("pattern_ecb.png")

