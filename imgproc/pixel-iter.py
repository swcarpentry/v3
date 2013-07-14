import media
import color

pic = media.create_picture(100, 200, media.black)

for i in range(media.get_width(pic)):
  for j in range(media.get_height(pic)):
  pixel = media.get_pixel(pic, i, j)
  media.set_color(pixel,
    media.create_color(i % 255, j % 255, 0))

pic.show()
