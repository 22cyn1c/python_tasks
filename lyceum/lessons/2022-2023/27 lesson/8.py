from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color='#75BBFD',
            snow_color='#FFFAFA', trunk_color='#A45A52',
            needls_color='#01796F', sun_color='#FFDB00'):
    im = Image.new("RGB", (width, height))
    drawer = ImageDraw.Draw(im)

    drawer.rectangle(((0, 0),
                      (width, int(height * 0.8))), sky_color)
    drawer.rectangle(((0, int(height * 0.8)), (width, height)),
                     snow_color)
    drawer.ellipse(((int(0.8 * width), -int(0.2 * height)),
                    (int(1.2 * width), int(0.2 * height))),
                   sun_color)
    drawer.polygon(((int(0.3 * width), int(height * 0.7)),
                    (int(0.4 * width), int(height * 0.5)),
                    (int(0.35 * width), int(height * 0.5)),
                    (int(0.45 * width), int(height * 0.3)),
                    (int(0.4 * width), int(height * 0.3)),
                    (int(0.5 * width), int(height * 0.1)),
                    (int(0.6 * width), int(height * 0.3)),
                    (int(0.55 * width), int(height * 0.3)),
                    (int(0.65 * width), int(height * 0.5)),
                    (int(0.6 * width), int(height * 0.5)),
                    (int(0.7 * width), int(height * 0.7)),
                    (int(0.3 * width), int(height * 0.7))
                    ),
                   needls_color)
    drawer.polygon(((int(0.45 * width), int(height * 0.9)),
                    (int(0.45 * width), int(height * 0.7)),
                    (int(0.55 * width), int(height * 0.7)),
                    (int(0.55 * width), int(height * 0.9))),
                   trunk_color)
    im.save(file_name)
