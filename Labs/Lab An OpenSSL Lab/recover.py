from PIL import Image

width = 432
height =475
with open("recovered.raw", "rb") as file:
    data = file.read()

img= Image.frombytes("L", (width, height), data)
img.save("img.png")