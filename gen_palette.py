#!/usr/bin/env python3

import numpy as np
import imageio
from zlib import compress

#palette = Image.new("RGB", (16, 16))

palette_raw = np.zeros((256,3))

modifiers = np.array([
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
])

hues = np.array([
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
])

i = 0
for hue in hues:
	for sat, off in modifiers:
		palette_raw[i] = hue * sat + off
		i += 1

for g in range(16):
	palette_raw[i] = g / 15
	i += 1

palette = (palette_raw * 255 + 0.5).astype(np.uint8)
print(palette)

imageio.imwrite("palette.png", palette.reshape(16,16,3))

color_list = open("colors.dat", "wb")
color_list.write(compress(bytes(palette)))
color_list.close()
