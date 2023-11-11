from PIL import Image


def twist_image(input_file_name, output_file_name):
    im = Image.open(input_file_name)
    x, y = im.size
    pixels = im.load()
    for i in range(x // 2):
        for j in range(y):
            pixels[i, j], pixels[x // 2 + i, j] = pixels[x // 2 + i, j], pixels[i, j]
    im.save(output_file_name)