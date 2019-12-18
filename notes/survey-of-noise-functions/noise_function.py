# -*- coding: utf-8 -*-

import random
import numpy as np


def fract(x):
    return x - np.floor(x)


def random_random(uv):
    return random.random()


def numpy_random_rand(uv):
    return np.random.rand()


xorshift_state = int(2463534242)


def xorshift(uv):
    global xorshift_state
    xorshift_state = xorshift_state ^ ((xorshift_state << 13) & 0xFFFFFFFF)
    xorshift_state = xorshift_state ^ (xorshift_state >> 17)
    xorshift_state = xorshift_state ^ ((xorshift_state << 5) & 0xFFFFFFFF)
    return float(xorshift_state) / float(4294967295.0)


def unnamed_hash_0(uv):
    offset = np.array([12.9898, 78.233])
    return fract(np.sin(np.dot(uv, offset)) * 43758.5453123)


def unnamed_hash_1(uv):
    offset = np.array([12.9898, 4.1414])
    return fract(np.sin(np.dot(uv, offset)) * 43758.5453)


def unnamed_hash_2(uv):
    a = np.sin(17.0 * uv[0] + uv[1] * 0.1)
    b = (0.1 + np.abs(np.sin(uv[1] * 13.0 + uv[0])))
    return fract(1e4 * a * b)
