import numpy as np
import numpy.linalg as LA
import sympy as sy
from PIL import Image
from calc_Fmatrix import calc_Fmatrix, calc_epipole, calc_Fmatrix_by5points
from draw_images import draw_images
from calc_camera_matrix import calc_inside_param

def division(uv_mat):
    """
    対応点を用途別に分ける際に利用した関数
    points8, points15, plane_points8, plane_points15, points8_else, points15_elseはそれぞれ
    8点, 15点, 同一平面上8点, 同一平面上15点, 選択した8点以外, 選択した15点以外
    """
    points8 = uv_mat[:8, :]
    points15 = uv_mat[:15, :]
    plane_points8 = uv_mat[[0,1,2,3,15,17,19,21], :]
    plane_points15 = uv_mat[[0,1,2,3,8,9,10,15,16,17,18,19,20,21,22], :]
    points8_else = uv_mat[8:, :]
    points15_else = uv_mat[15:, :]

    return points8, points15, plane_points8, plane_points15, points8_else, points15_else

if __name__ == '__main__':
    # getpoint.pyにより取り出した対応点を読み込み
    uv_mat = np.load("img/uv_mat1.npy")

    # 対応点を用途別に仕分け
    points8, points15, plane_points8, plane_points15, points8_else, points15_else = division(uv_mat)

    # 画像の読み込み
    pic_paths = ["img/img1.jpg", "img/img2.jpg"]

    # カメラ行列A1, A2
    f1, f2 = 923.620025369579, 941.677220030127
    c1 = [480, 853]
    c2 = [480, 853]
    A1 = np.array([[f1,  0, c1[0]],
                    [0, f1, c1[1]],
                    [0,  0,    1]])
    A2 = np.array([[f2,  0, c2[0]],
                    [0, f2, c2[1]],
                    [0,  0,    1]])

    # 5pointアルゴリズムによりFを算出
    F = calc_Fmatrix_by5points(points8, A1, A2)

    # エピポーラ線を描画
    draw_images(F, points8, pic_paths)
 