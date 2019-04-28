from inky import InkyPHAT

inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw

img = Image.open("resources/fingerprint.png")
inky_display.set_image(img)
inky_display.show()

from font_fredoka_one import FredokaOne

font = ImageFont.truetype(FredokaOne, 12)

from font_fredoka_one import FredokaOne

message = "Agent Confirmed"
w, h = font.getsize(message)
x = (inky_display.WIDTH / 106) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((x, y), message, inky_display.RED, font)
inky_display.set_image(img)
inky_display.show()
