import media

def chromakey(person, background):
    '''Replace blue pixels in the person picture with the corresponding
    pixels in the background picture.  The pictures must have the same dimensions.'''
    
    colour = media.get_color(media.get_pixel(person, 60, 60))
    for p in person:
		# 42 is a guess. Other values might work much better.
        if media.distance(media.get_color(p), colour) < 42:
            x = media.get_x(p)
            y = media.get_y(p)
            background_px = media.get_pixel(background, x, y)
            media.set_color(p, media.get_color(background_px))

if __name__ == '__main__':
    pic1 = media.load_picture(media.choose_file())
    #media.show(pic1)
    pic2 = media.load_picture(media.choose_file())
    #media.show(pic2)
    chromakey(pic1, pic2)
    media.show(pic1)
