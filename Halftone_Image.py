from sys import argv
import random
import os

from PIL import Image
from PIL import ImageOps
from PIL import ImageDraw


# Loading the image
img = Image.open(argv[1])
# turn image to grayscale
img = ImageOps.grayscale(img)
# create a uniform distribution of grayscale values in the output image
img = ImageOps.equalize(img)

# setting up a logic for each dot size
width, height = img.size
dot_mass = int(width / height * int(argv[2]))
pxls = int(width / dot_mass)

# creating a white canvas
canvas = Image.new('L', (width, height), 'white')
new_img = ImageDraw.Draw(canvas)

# replacing a block of pixles with a dot/circle
for x in range(0, width - pxls, pxls):
    for y in range(0, height - pxls, pxls):
        this_crop = img.crop((x, y, x + pxls, y + pxls))
        # make a list of all colors in selected block
        color_list = list(this_crop.getdata())
        # pick an average color to apply to selected block
        selected_color = int(sum(color_list) / len(color_list))
        # adding a bit of random noise resizing each dot to make it more natural
        noise = random.randrange(1, 3, 1)
        new_img.ellipse([x + noise / 2, y + noise / 2, x + pxls - noise / 2, y + pxls - noise / 2], selected_color)

# saving new file on same directory and displaying it
canvas.save("{}_{}_{}{}".format(os.path.splitext(argv[1])[0], argv[2], pxls, os.path.splitext(argv[1])[1]))
canvas.show()
canvas.close()
