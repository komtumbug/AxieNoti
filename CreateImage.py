from PIL import Image
import requests
from io import BytesIO
import os

imgname = "axie.jpg"

def GenImg():
    response = requests.get("https://storage.googleapis.com/assets.axieinfinity.com/axies/7479197/axie/axie-full-transparent.png")
    img = Image.open(BytesIO(response.content))
    imgresize = img.resize((200,150))
    rgb_img = imgresize.convert('RGB')
    rgb_img.save(imgname)


def DelImg():
    os.remove(imgname)