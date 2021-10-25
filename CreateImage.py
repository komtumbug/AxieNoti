from PIL import Image, ImageDraw, ImageFont, ImageColor
import requests
from io import BytesIO

class AxieImage:
    def __init__(self, axies) -> None:
        self.axies = axies

    def GenImage(self):
        whiteText = (255, 255, 255)
        nmFont = ImageFont.truetype('./fonts/Roboto-Regular.ttf', 18)
        lgFont = ImageFont.truetype('./fonts/Roboto-Regular.ttf', 24)
        
        partsIcon = {
            "eyes": {
                "icon": Image.open("./icons/part_eyes.png").convert('RGBA'),
                },
            "ears": {
                "icon": Image.open("./icons/part_ears.png").convert('RGBA'),
                },
            "back": { 
                "icon": Image.open("./icons/part_back.png").convert('RGBA'),
                },
            "mouth": { 
                "icon": Image.open("./icons/part_mouth.png").convert('RGBA'),
            },
            "horn": {
                "icon": Image.open("./icons/part_horn.png").convert('RGBA'),
            },
            "tail": { 
                "icon": Image.open("./icons/part_tail.png").convert(),
            }
        }

        for axie, value in self.axies.items():
            background = Image.new("RGB", (500, 600), ImageColor.getrgb("#242735"))
            cls = value["class"]

            print(value["id"])
            classIcon = Image.open(f"./icons/class_{cls}.png").convert('RGBA')

            response = requests.get(value["image"])

            axieImg = Image.open(BytesIO(response.content))

            axieImg = axieImg.resize((600, 450))

            axiePosition = (-45, 230)

            background.paste(axieImg, axiePosition, mask=axieImg)

            background.paste(classIcon, (40, 80), mask=classIcon)

            partX = 100
            partY = 180

            for part, item in partsIcon.items():
                background.paste(item["icon"], (partX, partY), mask=item["icon"])
                partX += 150

                if (part == "ears" or part == "mouth"):
                    partX = 100
                    partY += 50

            draw = ImageDraw.Draw(background)

            draw.text((340,40), value["priceeth"] + " ETH", whiteText, font=lgFont)

            draw.text((340, 75), value["price"] + " USD", whiteText, font=lgFont)

            draw.text((40, 40), "#" + value["id"], whiteText, font=lgFont)

            draw.text((60, 78), value["name"], whiteText, font=nmFont)

            draw.text((40, 105), "Breed count: " + str(value["breedcount"]), whiteText, font=nmFont)

            draw.text((40, 135), "HP: " + str(value["stats"]["hp"]), whiteText, font=nmFont)

            draw.text((100, 135), "SPD: " + str(value["stats"]["speed"]), whiteText, font=nmFont)

            draw.text((170, 135), "SKILL: " + str(value["stats"]["skill"]), whiteText, font=nmFont)

            draw.text((250, 135), "MORALE: " + str(value["stats"]["morale"]), whiteText, font=nmFont)

            partTextX = 140
            partY = 185

            for part, name in value["parts"].items():
                draw.text((partTextX, partY), name, whiteText, font=nmFont)
                partTextX += 150

                if (part == "ears" or part == "mouth"):
                    partTextX = 140
                    partY += 50

            background.save(f'{axie}.png')