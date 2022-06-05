import math
import numpy as np
from PIL import Image

def imgfile2xy(filename):
    threshold = 100
    img = np.array(Image.open(filename).convert('L').resize((200, 200)))
    img_bool = img > threshold
    x = np.array([])
    y = np.array([])
    for i in range(img_bool.shape[0]):
        for j in range(img_bool.shape[1]):
            if img_bool[i, j] == False:
                x = np.append(x, j)
                y = np.append(y, (img_bool.shape[0]-1)-i)
    return np.concatenate([[x], [y]])

def rotation(o):
    A = np.array([
        [math.cos(math.radians(o)), -math.sin(math.radians(o))],
        [math.sin(math.radians(o)), math.cos(math.radians(o))]
    ])
    return A


#鏡映x軸
A = np.array([
    [1, 0, 0],
    [0, -1, 0],
    [0, 0, 1],
])
#鏡映y軸
B = np.array([
    [-1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
])
#右上
C = np.array([
    [1, 0, 200],
    [0, 1, 200],
    [0, 0, 1],
])
#左上
D = np.array([
    [1, 0, -200],
    [0, 1, 200],
    [0, 0, 1],
])
#左下
E = np.array([
    [1, 0, -200],
    [0, 1, -200],
    [0, 0, 1],
])
#右下
F = np.array([
    [1, 0, 200],
    [0, 1, -200],
    [0, 0, 1],
])
#左に回転
G = np.array([
    [math.cos(math.radians(45)), -math.sin(math.radians(45)), 0],
    [math.sin(math.radians(45)), math.cos(math.radians(45)), 0],
    [0, 0, 1]
])
#1
H = np.array([
    [1, 0, 0],
    [0, 1, 100],
    [0, 0, 1],
])
#2
I = np.array([
    [1, 0, -100],
    [0, 1, 0],
    [0, 0, 1],
])
#3
J = np.array([
    [1, 0, 0],
    [0, 1, -100],
    [0, 0, 1],
])
#4
K = np.array([
    [1, 0, 100],
    [0, 1, 0],
    [0, 0, 1],
])

a = np.array([
    [1, 0],
    [0, -1],
])

b = np.array([
    [-1, 0],
    [0, 1]
])

a2 = np.array([
    [1, 0, 0],
    [0, -1, 0],
    [0, 0, 1]
])
