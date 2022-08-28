"""
File: mirror_lake.py
Name: Ariel
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: 'images/mt-rainier.jpg'
    :return: b_img
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height*2)

    for x in range(img.width):
        for y in range(img.height):
            colored_pixel = img.get_pixel(x, y)
            blank_pixel_up = b_img.get_pixel(x, y)
            blank_pixel_down = b_img.get_pixel(x, b_img.height-1-y)

            blank_pixel_up.red = colored_pixel.red
            blank_pixel_up.green = colored_pixel.green
            blank_pixel_up.blue = colored_pixel.blue

            blank_pixel_down.red = colored_pixel.red
            blank_pixel_down.green = colored_pixel.green
            blank_pixel_down.blue = colored_pixel.blue
    return b_img


def main():
    """
    This program flips the picture vertically.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
