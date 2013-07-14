import media

if __name__ == '__main__':

    filename = media.choose_file()
    pic = media.load_picture(filename)
    media.show(pic)
  
    # Reduce the blue and green by 30% each to make
    # the red stand out.
    for pixel in pic:
        value = media.get_blue(pixel)
        new_blue = int(value * 0.7)
        media.set_blue(pixel, new_blue)
        
        value = media.get_green(pixel)
        new_green = int(value * 0.7)
        media.set_green(pixel, new_green)
    
    media.show(pic)
