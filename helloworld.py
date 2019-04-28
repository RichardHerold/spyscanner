from inky import InkyPHAT

inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw

img = Image.open("resources/fingerprint.png")
inky_display.set_image(img)
inky_display.show()
