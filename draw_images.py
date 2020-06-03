import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def draw_images(F, uv_mat, pic_paths):
    """
    2つの画像にエピポーラ線描画

    F: F行列
    uv_mat: 画像1の対応点[u1, v1]と画像2の対応点[u2, v2]を
            [[u1, v1, u2, v2], ...]のように格納している
    width: 画像1, 2の幅
    height: 画像1, 2の高さ
    pic_paths: 画像1, 2のパスのリスト

    """
    n = uv_mat.shape[0]

    # 対応点の座標
    x1_set = np.array([[uv_mat[i, 0], uv_mat[i, 1], 1] for i in range(n)])
    x2_set = np.array([[uv_mat[i, 2], uv_mat[i, 3], 1] for i in range(n)])

    # エピポーラ線のパラメータ
    prams1 = np.dot(F.T, x2_set.T).T
    prams2 = np.dot(F, x1_set.T).T

    # 対応点の座標をu, vに分解
    u1_set, v1_set, u2_set, v2_set = uv_mat.T

    # 画像1でのエピポーラ線描画
    draw_lines(F, prams1, u1_set, v1_set, pic_paths[0])
    # 画像2でのエピポーラ線描画
    draw_lines(F, prams2, u2_set, v2_set, pic_paths[1])

def draw_lines(F, prams, u_set, v_set, pic_path):

    # 画像の読み込み
    img = np.array(Image.open(pic_path))

    # 画像のサイズ
    height, width, _ = img.shape

    # エピポーラ線を1本ずつ描画
    for (a, b, c) in prams:

        line = np.empty((0, 2))

        # x=0, w, y=0, hとの4交点のうち、画像枠内にある2点を選択
        u1 = -c/a
        u2 = -(b*height+c)/a
        v1 = -c/b
        v2 = -(a*width+c)/b

        if 0 <= u1 <= width:
            line = np.append(line, np.array([[u1, 0]]), axis=0)

        if 0 <= u2 <= width:
            line = np.append(line, np.array([[u2, height]]), axis=0)

        if 0 <= v1 <= height:
            line = np.append(line, np.array([[0, v1]]), axis=0)

        if 0 <= v2 <= height:
            line = np.append(line, np.array([[width, v2]]), axis=0)

        # 2点を結ぶ線分を描画
        plt.plot(line[:, 0], line[:, 1], marker="None",color="blue")
    
    # 対応点のプロット
    plt.plot(u_set, v_set, marker="o",linestyle="None", color="red")   

    # 画像の読み込み
    img = np.array(Image.open(pic_path))

    # 画像の表示
    plt.imshow(img)

    plt.show()
    plt.close()