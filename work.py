import numpy as np
import numpy.linalg as LA
import sympy as sy

from calc_Fmatrix import calc_Fmatrix, calc_epipole
from draw_images import draw_images
from calc_camera_matrix import calc_inside_param

if __name__ == '__main__':
    # uv_mat = np.array([[207, 193, 312, 256],
    #                 [251, 279, 432, 330],
    #                 [330, 279, 508, 290],
    #                 [451, 208, 548, 167],
    #                 [438, 145, 522, 104],
    #                 [386, 109, 404, 85],
    #                 [273, 135, 332, 155],
    #                 [288, 185, 451, 206]])

    # pic_paths = ["img/resize1.jpg", "img/resize2.jpg"]

    # # Fを算出
    # F = calc_Fmatrix(uv_mat)

    # # # 2枚の画像にエピポーラ線を描画
    # # draw_images(F, uv_mat, pic_paths)

    # # エピポールe1, e2を算出
    # e1 = calc_epipole(F)
    # e2 = calc_epipole(F.T)
    # print(e1, e2)

    c_u1 = c_v1 = c_u2 = c_v2 = 0

    A1 = np.array([[2.3, 0, 0], [0, 2.3, 0], [0, 0, 1]])
    A2 = np.array([[3.4, 0, 0], [0, 3.4, 0], [0, 0, 1]])
    r1, r2, r3 = 0.1, 0.2, 0.1
    rot_x = np.array([[1, 0, 0], [0, np.cos(r1), -np.sin(r1)], [0, np.sin(r1), np.cos(r1)]])
    rot_y = np.array([[np.cos(r2), 0, np.sin(r2)], [0, 1, 0], [-np.sin(r2), 0, np.cos(r2)]])
    rot_z = np.array([[np.cos(r3), -np.sin(r3), 0], [np.sin(r3), np.cos(r3), 0], [0, 0, 1]])
    R = np.dot(np.dot(rot_x, rot_y), rot_z)
    T = np.array([0.5, 0.05, 0.03])
    r1, r2, r3 = R.T

    E = np.array([np.cross(T, r1), np.cross(T, r2), np.cross(T, r3)]).T
    print(E)

    F = np.dot(np.dot(LA.inv(A1.T), E), LA.inv(A2))
    print(F)

    # エピポールe1を算出
    e1 = calc_epipole(F)

    # 内部パラメータを算出
    calc_inside_param(F, e1, c_u1, c_v1, c_u2, c_v2, calc_phase="f")

