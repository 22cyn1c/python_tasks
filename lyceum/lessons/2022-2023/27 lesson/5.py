from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color='#87CEEB',
            ocean_color='#017B92', boat_color='#874535',
            sail_color='#FFFFFF', sun_color='#FFCF40'):
    im = Image.new("RGB", (width, height))
    drawer = ImageDraw.Draw(im)

    drawer.rectangle(((0, 0),
                      (width, int(height * 0.8))), sky_color)
    drawer.rectangle(((0, int(height * 0.8)), (width, height)),
                     ocean_color)
    drawer.ellipse(((int(0.8 * width), -int(0.2 * height)),
                    (int(1.2 * width), int(0.2 * height))),
                   sun_color)

    drawer.polygon(((int(0.3 * width), int(height * 0.85)),
                    (int(0.25 * width), int(height * 0.65)),
                    (int(0.49 * width), int(height * 0.65)),
                    (int(0.49 * width), int(height * 0.3)),
                    (int(0.51 * width), int(height * 0.3)),
                    (int(0.51 * width), int(height * 0.65)),
                    (int(0.75 * width), int(height * 0.65)),
                    (int(0.7 * width), int(height * 0.85))),
                   boat_color)
    drawer.polygon(((int(0.51 * width), int(height * 0.3)),
                    (int(0.66 * width), int(height * 0.45)),
                    (int(0.51 * width), int(height * 0.6))),
                   sail_color)
    im.save(file_name)
