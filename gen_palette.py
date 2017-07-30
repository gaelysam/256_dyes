from PIL import Image
from array import array
from zlib import compress

#palette = Image.new("RGB", (16, 16))

palette_list = []

modifiers = [
	(0.25, 0.00),
	(0.50, 0.00),
	(0.75, 0.00),
	(1.00, 0.00),
	(0.75, 0.25),
	(0.50, 0.50),
	(0.25, 0.75),
	(0.25, 0.50),
	(0.25, 0.25),
	(0.50, 0.25),
]

def add_color(color):
	global palette_list
	palette_list += list(color)

def variations(color):
	for mod in modifiers:
		sat = mod[0]
		off = mod[1]
		r = int((color[0] * sat + off) * 255 + 0.5)
		g = int((color[1] * sat + off) * 255 + 0.5)
		b = int((color[2] * sat + off) * 255 + 0.5)
		add_color((r, g, b))

hues = [
	(1.00, 0.00, 0.00),
	(1.00, 0.25, 0.00),
	(1.00, 0.50, 0.00),
	(1.00, 0.75, 0.00),
	(1.00, 1.00, 0.00),
	(0.75, 1.00, 0.00),
	(0.50, 1.00, 0.00),
	(0.25, 1.00, 0.00),
	(0.00, 1.00, 0.00),
	(0.00, 1.00, 0.25),
	(0.00, 1.00, 0.50),
	(0.00, 1.00, 0.75),
	(0.00, 1.00, 1.00),
	(0.00, 0.75, 1.00),
	(0.00, 0.50, 1.00),
	(0.00, 0.25, 1.00),
	(0.00, 0.00, 1.00),
	(0.25, 0.00, 1.00),
	(0.50, 0.00, 1.00),
	(0.75, 0.00, 1.00),
	(1.00, 0.00, 1.00),
	(1.00, 0.00, 0.75),
	(1.00, 0.00, 0.50),
	(1.00, 0.00, 0.25),
]

for hue in hues:
	variations(hue)

for i in range(16):
	l = i * 17
	add_color((l, l, l))

palette_buffer = bytes(palette_list)

palette = Image.frombuffer("RGB", (16, 16), palette_buffer)
palette = palette.transpose(Image.FLIP_TOP_BOTTOM)
palette.save("palette.png")

color_list = open("colors.dat", "wb")
color_list.write(compress(palette_buffer))
color_list.close()
