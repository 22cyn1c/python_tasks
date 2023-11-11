from PIL import Image, ImageDraw


def mirror():
    im = Image.open('image.jpg')
    im = im.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270)
    im.save('res.jpg')


mirror()