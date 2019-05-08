from PIL import Image
import tesserocr


for i in range(1, 501):
    image = Image.open("jpg\\" + str(i) + ".jpg")
    # image.show()
    # # image.show()
    pixdata =image.load()
    w, h = image.size

    for x in range(w):
        for y in range(h):
            # print(pixdata[x,y])
            if(0<pixdata[x,y][0]<100):
                pixdata[x,y] = (0,0,0)
            else:
                pixdata[x,y] = (255,255,255)
    image = image.convert("L")
    image.show()

    flie_name = tesserocr.image_to_text(image)
    print(flie_name)
