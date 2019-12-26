import os
import requests
import json

import pygame
from PIL import Image, ImageDraw, ImageFont


def make(text):
    pygame.init()
    img = Image.open("./static/head.jpg")  # 250*250
    jgz = Image.open("./static/face.jpg")  # 101*113
    img.paste(jgz, (73, 47))  # 左右，上下

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('simhei.ttf', 24)
    draw.text((32, 190), text,
              fill=(0, 0, 0),
              font=font)
    img.save("./static/biaoqingbao.jpg")


def play(url):
    os.system('mplayer "%s"' % url)


def get_musicurl(title, artist):
    url_search = 'http://s.music.163.com/search/get/?src=lofter&type=1&filterDj=true&s=' + title + '&limit=900&offset=0&callback=loft.w.g.cbFuncSearchMusic'
    res = requests.get(url_search)
    j = json.loads(res.text[27:-1])
    id = j['result']['songs'][0]['id']
    for item in j['result']['songs']:
        if item['artists'][0]['name'] == artist:
            id = item['id']
            break
    url = 'https://music.163.com/#/song?id=' + str(id)
    return url
