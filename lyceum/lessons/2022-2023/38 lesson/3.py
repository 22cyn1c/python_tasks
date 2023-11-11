from PIL import Image, ImageDraw


def wayward(n, x, y, c):
    im = Image.open(n)
    x = x // 2
    a = im.size[0]
    a /= 2
    b = im.size[0]
    b /= 2
    im2 = im.crop((a - x, b - x, a + x, b + x))
    im3 = im2.transpose(Image.FLIP_LEFT_RIGHT)
    # im2.save('r1.png')
    # im3.save('r.png')
    n_i = Image.new("RGB", (x * 4 + 2 * y, x * 2 + 2 * y), (255, 255, 255))
    n_i.paste(im2, (y, y))
    n_i.paste(im3, (y + x * 2, y))
    n_i.save('a.png')
    drawer = ImageDraw.Draw(n_i)
    drawer.polygon(((0, 0), (x * 4 + 2 * y, 0), (x * 4 + 2 * y, y), (0, y)),
                   c)
    drawer.polygon(((0, 0), (y, 0), (y, x * 2 + 2 * y), (0, x * 2 + 2 * y)),
                   c)
    drawer.polygon(((0, x * 2 + 2 * y), (0, x * 2 + 2 * y - y), (x * 4 + 2 * y, x * 2 + 2 * y - y),
                    (x * 4 + 2 * y, x * 2 + 2 * y)),
                   c)
    drawer.polygon(((x * 4 + 2 * y, x * 2 + 2 * y), (x * 4 + 2 * y - y, x * 2 + 2 * y), (x * 4 + 2 * y - y, 0),
                    (x * 4 + 2 * y, 0)),
                   c)
    n_i.save('reflection.png')