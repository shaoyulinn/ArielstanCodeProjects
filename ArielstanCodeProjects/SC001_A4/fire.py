"""
File: fire.py
Name: Ariel
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: images/greenland-fire.png
    :return: fires
    """
    fires = SimpleImage(filename)
    for pixel in fires:
        avg = (pixel.red+pixel.green+pixel.blue)//3
        if pixel.red > avg * HURDLE_FACTOR:
            # Fires
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return fires


def main():
    """
    This program detects the fire area in the image.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
