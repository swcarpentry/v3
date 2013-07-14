import media

def get_intensity(pixel):
    '''Return the average of the RGB components of Pixel pixel.'''
    
    return (media.get_blue(pixel) + media.get_blue(pixel) + \
            media.get_blue(pixel)) / 3

def turn_stars_blue(pic, intensity):
    '''Find stars in Picture pic brighter than int intensity and turn them blue.'''
    
    for pixel in pic:
        if get_intensity(pixel) > intensity:
            media.set_color(pixel, media.blue)

def flood_fill(pic, x, y, intensity, c):
    '''Set all pixels in Picture pic brighter than int intensity and connected 
    to x, y to Color c.  Preconsition: c's intensity < intensity.'''
    
    pixel = media.get_pixel(pic, x, y)
    
    # Only process the pixel if it's bright.
    if get_intensity(pixel) > intensity:
        media.set_color(pixel, c)
    
        if 0 < x:
            flood_fill(pic, x - 1, y, intensity, c)
            
        if x < media.get_width(pic) - 1:
            flood_fill(pic, x + 1, y, intensity, c)

        if 0 < y:
            flood_fill(pic, x, y - 1, intensity, c)

        if x < media.get_height(pic) - 1:
            flood_fill(pic, x, y + 1, intensity, c)
    
    
def count_stars(pic, intensity):
    '''Count stars in Picture pic brighter than int intensity.'''
    
    count = 0
    
    for pixel in pic:
        if get_intensity(pixel) > intensity:
            count += 1
            x = media.get_x(pixel)
            y = media.get_y(pixel)
            flood_fill(pic, x, y, intensity, media.darkblue)
            
    return count

if __name__ == '__main__':
    pic = media.load_picture(media.choose_file())
    #turn_stars_blue(pic, 100)
    print count_stars(pic, 150)
    media.show(pic)