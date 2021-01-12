import cmath
import numpy as np
import matplotlib.pyplot as plt

def steps(c, itermax):
    z = complex(0,0)
    j = 0
    result = False
    while abs(z) < 2 and j < itermax:
        z = z ** 2 + c
        j += 1
    if j == itermax:
        result = True
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mesh = 10000
    m = []

    mandelbrot_x = []
    mandelbrot_y = []
    itermax = 20

    real = np.linspace(start = -2, stop = 2, num = mesh)
    for r in real:
        img = np.linspace(start = -2, stop = 2, num = mesh)
        for i in img:
            c = complex(r,i)
            if steps(c, itermax):
                mandelbrot_x.append(r)
                mandelbrot_y.append(i)




    plt.scatter(mandelbrot_x, mandelbrot_y, marker=".")
    plt.show()