import qrcode
import os

url = 'www.naver.com'
img = qrcode.make(url)

save_path = url + '.png'

img.save(save_path)
