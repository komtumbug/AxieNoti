from PIL import Image, ImageDraw, ImageFont, ImageColor
import requests
from io import BytesIO
import os

imgname = "axie.png"
testText = 'WTF'
font = './fonts/Roboto-Regular-ttf'
background = Image.new("RGB", (500, 600), ImageColor.getrgb("#242735"))
bg_w, bg_h = background.size

def GenImg():
    response = requests.get("https://storage.googleapis.com/assets.axieinfinity.com/axies/7479197/axie/axie-full-transparent.png")
    img = Image.open(BytesIO(response.content))
    
    imgresize = img.resize((600, 450))
    rgb_img = imgresize.convert('RGBA')

    rgb_img.save(imgname, 'png')

    img_w, img_h = rgb_img.size

    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(rgb_img, offset, mask=rgb_img)
    background.save('out.png')
    


def DelImg():
    os.remove(imgname)

GenImg()