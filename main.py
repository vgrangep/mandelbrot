import numpy as np
from math import log10, cos
import tqdm
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import cm


def color_scale():
    cmap = cm.get_cmap("BrBG")
    scale = [cmap(i) for i in range(255)]
    return scale



def steps(c: complex, threshold: int = 2, itermax: int = 20):
    z = complex(0, 0)
    j = 0
    while abs(z) < threshold and j < itermax:
        z = z ** 2 + c
        j += 1
    return j


def generate_set(threshold, itermax, img_size, x_min=-2, x_max=0.48, y_min=-1.24, y_max=1.24):
    #img_data = np.full((img_size[0], img_size[1], 3), 255,  dtype=np.uint8)
    img_data = np.full((img_size[0], img_size[1]), 255, dtype=np.uint8)
    real = zip(tqdm.trange(img_size[1]), np.linspace(start=x_min, stop=x_max, num=img_size[1]))
    for idr, r in real:
        imaginary = zip(range(img_size[0]), np.linspace(start=y_min, stop=y_max, num=img_size[0]))
        for idi, i in imaginary:
            it = steps(complex(r, i), threshold=threshold, itermax=itermax)
            img_data[idi][idr] = it
    return img_data


def generate_img_pil(data, file_name, itermax, img_size):
    data_hsv = np.full((img_size[0], img_size[1], 3), 0, dtype=np.uint8)
    for idi, i in enumerate(data):
        for idy, y in enumerate(i):
            hue = 180
            saturation = 255
            value = 255 * (1 - log10(y / itermax)) if y < itermax else 0
            data_hsv[idi][idy] = [hue, saturation, value]
    img = Image.fromarray(data_hsv, mode='HSV').convert('RGB')
    img.save(file_name, "JPEG")
    img.show()


def generate_img_mpl(data, file_name, w, h):

    plt.imshow( data, cmap='viridis')


if __name__ == '__main__':
    img_size = (1440, 3440)
    #img_size = (480, 640)
    itermax = 250
    threshold = 4

    img_dir = "img_generated/"
    file_name = img_dir + "mandelbrot_" + str(img_size[0]) + "x" + str(img_size[1]) + ".jpg"


    margin = 0
    x_min = -2.2
    x_max = 0.6
    y_min = - (x_max - x_min) * img_size[0] / img_size[1]
    y_max = 0 - margin


    cmap = color_scale()


    img_data = generate_set(threshold=threshold, itermax=itermax, img_size=img_size,
                            x_max=x_max + margin, x_min=x_min - margin,
                            y_min=y_min -  margin, y_max=y_max + margin)

    generate_img_pil(img_data, file_name, itermax, img_size)
    #generate_img_mpl(img_data, file_name, img_size[0], img_size[1])