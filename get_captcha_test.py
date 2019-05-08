import requests
import tesserocr
from bs4 import BeautifulSoup
from PIL import Image


base_url = "http://jw.hzau.edu.cn/"
aspx_url = "http://jw.hzau.edu.cn/CheckCode.aspx"
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"

header = {
    'User-Agent': ua,
    'Host': "localhost",
    'Accept-Language': "zh-CN,zh;q=0.8",
    'Accept-Encoding': "gzip, deflate",
    'Content-Type': "application/x-www-form-urlencoded",
    'Connection': "keep-alive",
}
i = 0
r = requests.session()


def get_post_data(url_base, url_aspx,i):
    img = r.get(url_aspx, stream=True, headers=header)
    with open("D:\python\Captcha_test\png\\"+ str(i) +".png", 'wb') as f:
        f.write(img.content)


while True:
    i += 1
    if i<=500:
        get_post_data(base_url, aspx_url, i)
        print("储存第%d"%i)
    else:
        break
