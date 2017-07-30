# 256 Dyes for Minetest
256 variants of a single item "256_dyes:dye". Not useful for now.
Universal mixing craft recipe: you can mix up to 9 colors at once on the crafting grid.
In game, only the brown dye can be found in creative inventory. You can change the color by clicking:
- Right click changes hue
- Left click changes brightness
The `color.dat` file is used by the mixing algorithm. (compressed list of RGB color codes)
gen_palette.py: Python 3 script to run with Python Image Library to generate the palette and color.dat. Could be easily modified to generate a different palette.

256-colors palette based on 24 hues, with 10 variations of each one, and grey scales.

Screenshot showing the 24 pure hues:
![Screenshot](https://raw.githubusercontent.com/Gael-de-Sailly/256_dyes/master/screenshot.png)

Code: Gael-de-Sailly
Textures:
- palettes: Gael-de-Sailly
- white dye texture: Celeron55, modified by Gael-de-Sailly
