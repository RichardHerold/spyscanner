from inky import InkyPHAT

inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
font = ImageFont.truetype(FredokaOne, 11)

img = Image.open("resources/fingerprint.png")
draw = ImageDraw.Draw(img)

draw.text((90, 20), "AGENT CONFIRMED", inky_display.WHITE, font=font)
inky_display.set_image(img)
inky_display.show()
