#!/usr/bin/env python3
# mie nov 27 19:01:16 CET 2013
# im2ws: Convierte los colores de una imagen al rango colores seguros para la web.

import sys
from PIL import Image

if len(sys.argv) == 3:
    imagein = sys.argv[1]
    imageout = sys.argv[2]
else:
    sys.exit('Se necesitan dos argumentos' + str(len(sys.argv)))

palette = (0x00, 0x33, 0x66, 0x99, 0xcc, 0xff)

im = Image.open(imagein)
pix = im.load()


def nextcolor(c, p):
    i = 0
    dif = range(0, len(p))
    for shape in p:
        dif[i] = abs(c-shape)
        i = i + 1

    min = 0xfff
    for j in range(0, len(dif)):
        if min > dif[j]:
            min = dif[j]
            nextc = p[j]
    return nextc


def colorfilter(px):
    r = nextcolor(px[0], palette)
    g = nextcolor(px[1], palette)
    b = nextcolor(px[2], palette)
    return (r, g, b)


for x in range(0, im.size[0]):
    for y in range(0, im.size[1]):
        pix[x,y] = colorfilter(pix[x,y])

im.save(imageout)
