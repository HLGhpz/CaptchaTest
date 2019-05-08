from PIL import Image

image = Image.open("1.png")
# image.show()
image = image.convert("L")
pixdata =image.load()
threshold = 1
w, h = image.size
# print('w=%s,h=%s' % (w, h))
for y in range(h):
    for x in range(w):
        if pixdata[x,y] < 30:
            pixdata[x,y] = 0
        else:
            pixdata[x,y] = 255
image.show()
