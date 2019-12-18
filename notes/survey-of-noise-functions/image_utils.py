# -*- coding: utf-8 -*-

import numpy as np
import cv2


def create_image(width, height):
    # No alpha-channel
    return np.zeros([height, width, 3])


def convert_monochrome_to_color(image, width, height):
    new_image = create_image(width, height)
    for y in range(height):
        for x in range(width):
            value = image[y][x]
            new_image[y][x][0] = value
            new_image[y][x][1] = value
            new_image[y][x][2] = value
    return new_image


def fill_uv_color(image, width, height):
    for y in range(height):
        ry = y / (height - 1)
        for x in range(width):
            rx = x / (width - 1)
            image[y][x][0] = 255 * rx
            image[y][x][1] = 255 * ry
            image[y][x][2] = 0


def get_fft2_image(image):
    # Calculate 2D-FFT and shift to visualize
    fft = np.fft.fft2(image)
    fft = np.fft.fftshift(fft)

    # Level adjustment
    p = np.log10(np.absolute(fft))

    # Normalize to [0, 255]
    min = np.amax(p)
    if min > 0:
        p = p / min
    p = np.uint8(np.around(p * 255))
    return p


def save_image(image, output_path):
    cv2.imwrite(output_path, image[:, :, [2, 1, 0]])
