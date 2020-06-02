import cv2
import numpy as np
import matplotlib.pyplot as plt

def line2d(a, b):
    """ 線分abの2D点群生成 """

    t = np.arange(0, 1, 0.01)

    x = a[0]*t + b[0]*(1-t)
    y = a[1]*t + b[1]*(1-t)

    return x, y            

def draw_lines(F, uv_mat):
    width = 768
    height = 432
    N = np.array([[2/width, 0, -1],
                [0, 2/height, -1],
                [0, 0, 1]])

    n = uv_mat.shape[0]

    x1_set = np.array([[uv_mat[i, 0], uv_mat[i, 1], 1] for i in range(n)])
    x2_set = np.array([[uv_mat[i, 2], uv_mat[i, 3], 1] for i in range(n)])

    for i in range(n):
        # Nにより正規化
        x1 = np.dot(N, x1_set[i].T)
        x2 = np.dot(N, x2_set[i].T)
        # x1 = x1_set[i].T
        # x2 = x2_set[i].T
        print(x1, x2)

        pram1 = np.dot(F.T, x2)
        pram2 = np.dot(F, x1)

        a1, b1, c1 = pram1
        print(a1, b1, c1)

        # a2, b2, c2 = pram2

        # start1 = [-c1/a1, -c1/b1]
        # end1 = [-(b1*height+c1)/a1, -(a1*width+c1)/b1]

        # start2 = [-c2/a2, -c2/b2]
        # end2 = [-(b2*height+c2)/a2, -(a2*width+c2)/b2]

        # x_cross = [-c1/a1, 0]
        # y_cross = [0, -c1/b1]
        # line1 = line2d(x_cross, y_cross)
        # print(x_cross, y_cross)

        # print("="*50)

        # plt.plot(line1[0],line1[1],marker=".",color="yellow")
        # plt.plot(x_cross, y_cross,marker="o",color="red")

        p = np.array([[(b1-c1)/a1, -1], 
                        [-(b1+c1)/a1, 1],
                        [-1, (a1-c1)/b1],
                        [1, -(a1+c1)/b1]])

        plt.plot(p[:, 0], p[:, 1],linestyle="None", marker="o",color="blue")

    line1 = line2d([-1,-1], [-1,1])
    line2 = line2d([-1,1], [1,1])
    line3 = line2d([1,1], [1,-1])
    line4 = line2d([1,-1], [-1,-1])

    plt.plot(line1[0],line1[1],marker=".",linestyle="None",color="black")
    plt.plot(line2[0],line2[1],marker=".",linestyle="None",color="black")
    plt.plot(line3[0],line3[1],marker=".",linestyle="None",color="black")
    plt.plot(line4[0],line4[1],marker=".",linestyle="None",color="black")

    plt.show()








    