import cv2
import numpy as np
import matplotlib.pyplot as plt

def line2d(a, b):
    """ 線分abの2D点群生成 """

    t = np.arange(0, 1, 0.01)

    x = a[0]*t + b[0]*(1-t)
    y = a[1]*t + b[1]*(1-t)

    return x, y            

def draw_lines(F, width, height, uv_mat):

    n = uv_mat.shape[0]

    # 対応点の座標
    x1_set = np.array([[uv_mat[i, 0], uv_mat[i, 1], 1] for i in range(n)])
    x2_set = np.array([[uv_mat[i, 2], uv_mat[i, 3], 1] for i in range(n)])

    # #figure()でグラフを表示する領域をつくり，figというオブジェクトにする．
    # fig = plt.figure()

    # #add_subplot()でグラフを描画する領域を追加する．引数は行，列，場所
    # ax1 = fig.add_subplot(1, 2, 1)
    # ax2 = fig.add_subplot(1, 2, 2)

    for x1, x2 in zip(x1_set, x2_set):

        # 画像枠
        line1 = line2d([0,0], [0,height])
        line2 = line2d([0,height], [width,height])
        line3 = line2d([width,height], [width,0])
        line4 = line2d([width,0], [0,0]) 
        plt.plot(line1[0],line1[1],marker=".",linestyle="None",color="black")
        plt.plot(line2[0],line2[1],marker=".",linestyle="None",color="black")
        plt.plot(line3[0],line3[1],marker=".",linestyle="None",color="black")
        plt.plot(line4[0],line4[1],marker=".",linestyle="None",color="black")

        print(x1, x2)

        # F x1 = [a, b, c]よりエピポーラ線のパラメータ算出
        pram1 = np.dot(F.T, x2)
        pram2 = np.dot(F, x1)

        a, b, c = pram1

        line = np.empty((0, 2))

        # x=0, w, y=0, hとの4交点のうち、画像枠内にある2点を選択
        u1 = -c/a
        u2 = -(b*height+c)/a
        v1 = -c/b
        v2 = -(a*width+c)/b

        if 0 <= u1 <= width:
            line = np.append(line, np.array([[u1, 0]]), axis=0)
            print(1)

        if 0 <= u2 <= width:
            line = np.append(line, np.array([[u2, height]]), axis=0)
            print(2)

        if 0 <= v1 <= height:
            line = np.append(line, np.array([[0, v1]]), axis=0)
            print(3)

        if 0 <= v2 <= height:
            line = np.append(line, np.array([[width, v2]]), axis=0)
            print(4)

        print(line)

        # x=0, w, y=0, hとの4交点のうち、画像枠内にある2点を選択
        plt.plot(line[:, 0], line[:, 1], marker="o",color="blue")
        plt.show()
        plt.close()

    # 画像枠
    line1 = line2d([0,0], [0,height])
    line2 = line2d([0,height], [width,height])
    line3 = line2d([width,height], [width,0])
    line4 = line2d([width,0], [0,0]) 
    plt.plot(line1[0],line1[1],marker=".",linestyle="None",color="black")
    plt.plot(line2[0],line2[1],marker=".",linestyle="None",color="black")
    plt.plot(line3[0],line3[1],marker=".",linestyle="None",color="black")
    plt.plot(line4[0],line4[1],marker=".",linestyle="None",color="black")

    plt.show()