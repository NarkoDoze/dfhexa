from PIL import Image, ImageFont, ImageDraw
import requests
import json

class List:
    def __init__(self):
        with open("makefail/API/result.json", 'r', encoding='utf-8') as f:
            self.epic = json.load(f)


class MakeFail:
    def __init__(self, type, name, num):
        # NEED!!
        # result.json
        self.type = type
        self.name = name
        self.num = num
        with open("makefail/API/result.json", 'r', encoding='utf-8') as f:
            self.epic = json.load(f)

    def image(self):
        # NEED!!
        # fail1.jpg
        # moris.ttf
        url = 'http://df.gamebogam.com/item/'
        url += self.epic[self.type][self.name]
        til = Image.open(requests.get(url, stream=True).raw)
        im = Image.open("makefail/API/fail1.jpg")

        im.paste(til, (22, 60))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype('makefail/API/moris.ttf', 11)

        name = self.num + " " + self.name
        len = name.__len__()
        half = name.count(' ') + name.count('-') + name.count('+')
        start = (175 - (len - half) * 10 - half * 5) / 2 + 50

        draw.text((start, 68), name, (255, 180, 0), font=font)
        return im

# Example Code
# if __name__=="__main__":
#     MakeFail('zhua', '구원의 이기 - 클로', '').image().save('here.png')
