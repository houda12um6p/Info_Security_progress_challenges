with open("classified.enc", "rb") as file:
    data = file.read()

print(len(data))
image = data[16:]
print(len(image))

result = []
for i in range(0, len(image), 16):
    block = image[i:i+16]
    result.append(block)

from collections import Counter
from PIL import Image

counts = Counter(result)
colors = {}

for i, (block, count) in enumerate(counts.most_common()):
    if i == 0:
        colors[block] = 255
    else:
        colors[block] = (count * 53) % 200

pixels = []
for block in result:
    pixels.extend([colors[block]] * 16)

img = Image.new("L", (432, 475))
img.putdata(pixels)
img.save("test.png")