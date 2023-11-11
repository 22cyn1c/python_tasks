from PIL import Image, ImageDraw


def mirror():
    im = Image.open('image.jpg')
    im = im.transpose(Image.FLIP_LEFT_RIGHT)
    im.save('res.jpg')


mirror()