from PIL import Image, ImageDraw


def spotted_uding(filename, w, *colors):
    width = w * 10
    height = w * 4
    im = Image.new("RGB", (width, height), (255, 255, 255))
    drawer = ImageDraw.Draw(im)
    drawer.ellipse((
        (0, 0),
        (int(width), int(height))),
         colors[0])
    drawer.polygon(((int(0.2 * width), int(height * 0.125)),
                    (int(0.8 * width), int(height * 0.125)),
                    (int(0.8 * width), int(height * 0.875)),
                    (int(0.2 * width), int(height * 0.875))), colors[1])
    im.save(filename, "PNG")