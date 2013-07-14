import media

def chromakey(person, background):
    '''Replace blue pixels in the person picture with the corresponding
    pixels in the background picture. The pictures must have the same
    dimensions.'''

    for pixel in person:

        # If the blue dominates the pixel, replace its colour with the colour of
        # the corresponding pixel from the background picture.
        if media.get_blue(pixel) > media.get_green(pixel) and \
                media.get_blue(pixel) > media.get_red(pixel):
            x = media.get_x(pixel)
            y = media.get_y(pixel)
            background_px = media.get_pixel(background, x, y)
            media.set_color(pixel, media.get_color(background_px))

if __name__ == '__main__':
    pic1 = media.load_picture(media.choose_file())
    media.show(pic1)
    pic2 = media.load_picture(media.choose_file())
    media.show(pic2)
    chromakey(pic1, pic2)
    media.show(pic1)
