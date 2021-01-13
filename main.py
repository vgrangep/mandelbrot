import cmath
from math import floor
import numpy as np
import matplotlib.pyplot as plt
import tqdm


def steps(c:complex, threshold:int = 2, itermax:int = 20):
    z = complex(0,0)
    j = 0
    result = False
    while abs(z) < threshold and j < itermax:
        z = z ** 2 + c
        j += 1
    return j


def generate_set(threshold, itermax, meshsize:int, x_min = -2, x_max = 0.48, y_min = -1.24, y_max = 1.24):
    img = np.full((meshsize, meshsize), 255)

    real = np.linspace(start = x_min, stop = x_max, num = meshsize)

    for idr, r in zip(tqdm.trange(meshsize), real):
        imaginary = zip(range(meshsize), np.linspace(start = y_min, stop = y_max, num = meshsize))
        for idi, i in imaginary:
            it = steps(complex(r, i), threshold = 2, itermax = itermax)
            img[idi][idr] = 255 - floor(it * 2.5)
    return img


if __name__ == '__main__':
    meshsize = 10_000
    itermax = 100
    threshold = 2

    x_min = -2.5
    y_min = -2.5
    x_max = 2.5
    y_max = 2.5

    img = generate_set(threshold = 2, itermax = 25, meshsize = meshsize, x_max = x_max, x_min = x_min, y_min = y_min,
                       y_max = y_max )


    plt.figure(figsize=(10, 10))
    plt.imshow(img, cmap="twilight_shifted")

    plt.axis("off")
    plt.show()