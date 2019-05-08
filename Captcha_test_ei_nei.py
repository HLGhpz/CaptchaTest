from PIL import Image

image = Image.open("test.png")
# image.show()
image = image.convert("L")
pixdata =image.load()
threshold = 1
w, h = image.size
# 八临域
qz = 175
for y in range(h-1):
    for x in range(w-1):
        # print(x)
        count = 0
        # 判断8领域内白色点的个数

        if pixdata[x, y-1] > qz:
            count += 1
        if pixdata[x, y+1] > qz:
            count += 1
        if pixdata[x+1, y] > qz:
            count += 1
        if pixdata[x-1, y] > qz:
            count += 1
        if pixdata[x-1, y-1] > qz:
            count += 1
        if pixdata[x-1, y+1] > qz:
            count += 1
        if pixdata[x+1, y-1] > qz:
            count += 1
        if pixdata[x+1, y+1] > qz:
            count += 1

        print('count=%s' % count)

        if count < 3:
            #如果8邻域内白色点个数小于6
            pixdata[x, y] = 255
            #为黑色
        else:
            pixdata[x, y] = 0
image.show()
