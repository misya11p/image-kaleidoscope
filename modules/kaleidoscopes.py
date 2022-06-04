import numpy as np
import matplotlib.pyplot as plt
import cv2
from _tools import *

def kal_1(filepath):
    img = imgfile2xy(filepath)
    rr = []
    result = []
    for _ in range(0, 360, 15):
        rr.append(rotation(_))
    for i in range(0, len(rr)):
        result.append(np.dot(rr[i], img))
    for l in range(0, len(rr)):
        result.append(np.dot(rr[l], img))
    for i in range(len(rr)):
        plt.scatter(result[i][0], result[i][1], s=1, color='black')
    plt.axis('equal')
    plt.grid(which='major')


def kal_2(path):
    im = cv2.imread(path)
    height, width, channels = im.shape[:3]
    if height >= 200 and height >= 200:
        hei1 = height / 2 - 200
        hei2 = height / 2 + 200
        wid1 = width / 2 - 200
        wid2 = width / 2 + 200

        # name = 'henkango'
        # pa = f'/content/drive/MyDrive/Colab Notebooks/{name}.jpg'

        pa = 'static/tmp/henkango.jpg'
        img1 = im[int(hei1): int(hei2), int(wid1): int(wid2)]
        cv2.imwrite(pa, img1)

        part1 = imgfile2xy(pa)

        # 四角の左上　1を鏡映
        img1 = np.insert(part1, 2, 1, axis=0)
        imgnew = np.dot(B, img1)
        part2 = np.delete(imgnew, 2, axis=0)
        # 四角の右下 1をx軸で鏡映
        img1 = np.insert(part1, 2, 1, axis=0)
        imgnew = np.dot(A, img1)
        part3 = np.delete(imgnew, 2, axis=0)
        #四角の左下　2をx軸で鏡映
        img1 = np.insert(part2, 2, 1, axis=0)
        imgnew = np.dot(A, img1)
        part4 = np.delete(imgnew, 2, axis=0)
        #1を右上に２００
        img1 = np.insert(part1, 2, 1, axis=0)
        imgnew = np.dot(C, img1)
        part5 = np.delete(imgnew, 2, axis=0)
        #２を左上に２００
        img1 = np.insert(part2, 2, 1, axis=0)
        imgnew = np.dot(D, img1)
        part6 = np.delete(imgnew, 2, axis=0)
        #３を右下に２００
        img1 = np.insert(part4, 2, 1, axis=0)
        imgnew = np.dot(E, img1)
        part7 = np.delete(imgnew, 2, axis=0)
        #４を左下に２００
        img1 = np.insert(part3, 2, 1, axis=0)
        imgnew = np.dot(F, img1)
        part8 = np.delete(imgnew, 2, axis=0)
        #１を左に９０度＋上に１００
        img1 = np.insert(part1, 2, 1, axis=0)
        img2 = np.dot(G, img1)
        imgnew = np.dot(H, img2)
        part9 = np.delete(imgnew, 2, axis=0)
        #2を左に９０度＋左に１００
        img1 = np.insert(part2, 2, 1, axis=0)
        img2 = np.dot(G, img1)
        imgnew = np.dot(I, img2)
        part10 = np.delete(imgnew, 2, axis=0)
        #3を左に９０度＋右に１００
        img1 = np.insert(part3, 2, 1, axis=0)
        img2 = np.dot(G, img1)
        imgnew = np.dot(K, img2)
        part11 = np.delete(imgnew, 2, axis=0)
        #4を左に９０度＋下に１００
        img1 = np.insert(part4, 2, 1, axis=0)
        img2 = np.dot(G, img1)
        imgnew = np.dot(J, img2)
        part12 = np.delete(imgnew, 2, axis=0)

        plt.scatter(part1[0], part1[1], s=1, color="c")
        plt.scatter(part2[0], part2[1], s=1, color="m")
        plt.scatter(part3[0], part3[1], s=1, color="m")
        plt.scatter(part4[0], part4[1], s=1, color="c")
        plt.scatter(part5[0], part5[1], s=1, color="y")
        plt.scatter(part6[0], part6[1], s=1, color="y")
        plt.scatter(part7[0], part7[1], s=1, color="y")
        plt.scatter(part8[0], part8[1], s=1, color="y")
        plt.scatter(part9[0], part9[1], s=1, color="g")
        plt.scatter(part10[0], part10[1], s=1, color="g")
        plt.scatter(part11[0], part11[1], s=1, color="g")
        plt.scatter(part12[0], part12[1], s=1, color="g")
        # plt.tick_params(labelbottom=False, labelleft=False, labelright=False,
        #                 labeltop=False, bottom=False, left=False, right=False, top=False)
        # plt.gca().spines['right'].set_visible(False)
        # plt.gca().spines['top'].set_visible(False)
        # plt.gca().spines['left'].set_visible(False)
        # plt.gca().spines['bottom'].set_visible(False)
        plt.axis('equal')
        # plt.savefig("/content/drive/MyDrive/Colab Notebooks/mangekyou.png")
        # plt.show()

        # os.remove(pa)
    else:
        print("サイズが小さすぎます200px*200px以上の写真を指定してください")


def kal_3(path):
    img = imgfile2xy(path)
    imgnew = np.dot(a, img)
    imgnew1 = np.dot(b, img)
    imgnew2 = a@b@img
    # 元画像を灰色
    plt.scatter(img[0], img[1], s=1, color="gray")
    # 移動後の画像を黒色
    plt.scatter(imgnew[0], imgnew[1], s=1, color="black")
    plt.scatter(imgnew1[0], imgnew1[1], s=1, color="black")
    plt.scatter(imgnew2[0], imgnew2[1], s=1, color="gray")
    plt.axis('equal')