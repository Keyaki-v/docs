# -*- coding: utf-8 -*-

import sys
import random
import numpy as np
import image_utils as ut
import noise_function as noise
from matplotlib import pyplot as plt


def output_test():
    width = 256
    height = 256
    image = ut.create_image(width, height)
    ut.fill_uv_color(image, width, height)
    image_name = f'images/{sys._getframe().f_code.co_name}'
    ut.save_image(image, f'{image_name}.png')


def noise_2d_function_test(noise_function, width=256, height=256):
    image_name = f'images/{noise_function.__name__}'
    image = np.zeros([height, width])
    # Create a noise image
    for y in range(height):
        ry = y / (height - 1)
        for x in range(width):
            rx = x / (width - 1)
            uv = np.array([rx, ry])
            noise_value = noise_function(uv)
            assert (0.0 <= noise_value and
                    noise_value <= 1.0), f'{noise_value}'
            image[y][x] = np.floor(noise_value * 256)
    # Get its histogram
    hist, bins = np.histogram(image.ravel(), 256, [0, 256])
    plt.cla()
    plt.clf()
    plt.step(bins[:-1], hist, where='post')
    plt.savefig(f'{image_name}_hist.png')
    # Get its FFT image
    image_color = ut.convert_monochrome_to_color(image, width, height)
    image_fft2 = ut.get_fft2_image(image)
    image_fft2 = ut.convert_monochrome_to_color(image_fft2, width, height)
    # Save images
    ut.save_image(image_color, f'{image_name}.png')
    ut.save_image(image_fft2, f'{image_name}_fft.png')


def main():
    print('A survey of noise functions')
    random.seed(42)
    np.random.seed(seed=42)
    output_test()
    noise_2d_function_test(noise.random_random)
    noise_2d_function_test(noise.numpy_random_rand)
    noise_2d_function_test(noise.xorshift)
    noise_2d_function_test(noise.unnamed_hash_0)
    noise_2d_function_test(noise.unnamed_hash_1)
    noise_2d_function_test(noise.unnamed_hash_2)


if __name__ == '__main__':
    main()
