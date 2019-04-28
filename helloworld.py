from inky import InkyPHAT

inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
font = ImageFont.truetype(FredokaOne, 12)

img = Image.open("resources/fingerprint.png")
draw = ImageDraw.Draw(img)

draw.text((106, 2), "agent confirmed", inky_display.WHITE, font=font)
inky_display.set_image(img)
inky_display.show()
