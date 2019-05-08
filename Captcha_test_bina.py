from PIL import Image
import tesserocr
import time


for i in range(1,501):
    image = Image.open("test.png")
    if(image==None):
        print('none')
    image = image.convert("L")
    threshold = 80
    table = []
    print('第%d张'%i)

    for j in range(256):
        if j<threshold:
            table.append(0)
        else:
            table.append(1)

    image = image.point(table,'1')
    file_name = tesserocr.image_to_text(image).replace("\n",'').replace("/",'').replace("?",'').replace("|",'').replace("<",'').replace(">",'').replace("\\",'').replace(":",'').replace('"','').replace('*','').replace(' ','').replace('.','')
    # print(file_name)
    # image.show()

    image.save('png_ocr\\' + str(i) + file_name+'.jpg')


