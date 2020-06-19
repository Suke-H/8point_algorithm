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
    img1 = np.array(Image.open(pic_paths[0]))
    img2 = np.array(Image.open(pic_paths[1]))
    # 正解の中心座標ans_cを出しておく
    ans_c_v1, ans_c_u1, _ = np.array(img1.shape) / 2
    ans_c_v2, ans_c_u2, _ = np.array(img2.shape) / 2
    f1, f2 = 923.620025369579, 941.677220030127
    c1 = [480, 853]
    c2 = [480, 853]
    A1 = np.array([[f1,  0, c1[0]],
                    [0, f1, c1[1]],
                    [0,  0,    1]])
    A2 = np.array([[f2,  0, c2[0]],
                    [0, f2, c2[1]],
                    [0,  0,    1]])
    F_test = calc_Fmatrix_by5points(points8, A1, A2)
    # 15点のエピポーラ線を描画
    draw_images(F_test, points8, pic_paths)
    # # 選択した8点からFを算出
    # F8 = calc_Fmatrix(points8)
    # print("F8:\n{}".format(F8))
    # # 同一平面上の8点からFを導出
    # plane_F8 = calc_Fmatrix(plane_points8)
    # print("plane_F8:\n{}".format(plane_F8))
    # # 8点のエピポーラ線を描画
    # draw_images(F8, points8, pic_paths)
    # # 8点以外のエピポーラ線を描画
    # draw_images(F8, points8_else, pic_paths)
    # # # 同一平面8点のエピポーラ線を描画
    # # draw_images(plane_F8, plane_points8, pic_paths)
    # # 選択した15点からFを算出
    # F15 = calc_Fmatrix(points15)
    # print("F15:\n{}".format(F15))
    # # 同一平面上の15点からFを導出
    # plane_F15 = calc_Fmatrix(plane_points15)
    # print("plane_F15:\n{}".format(plane_F15))
    # # # 15点のエピポーラ線を描画
    # # draw_images(F15, points15, pic_paths)
    # # # 15点以外のエピポーラ線を描画
    # # draw_images(F15, points15_else, pic_paths)
    # # # 同一平面15点のエピポーラ線を描画
    # # draw_images(plane_F15, plane_points15, pic_paths)
    # # エピポールe1を算出
    # e1 = calc_epipole(F8.T)
    # print("e1: {}".format(e1))
    # # fu=fvとして焦点距離f1, f2を算出
    # ans = calc_inside_param(F8, e1, ans_c_u1, ans_c_v1, ans_c_u2, ans_c_v2, calc_phase="f")
    # # 解が複数出ることがあるので、ユーザーに欲しい解か何番目がを入力してもらう
    # val = input('解が何番目(0, 1, 2, 3)かを入力: ')
    # f1, f2 = ans[int(val)][0], ans[int(val)][1]
    # print("(f1, f2) = ({}, {})".format(f1, f2))
    # # 画像1の中心座標(cu1, cv1)を算出
    # calc_inside_param(F8, e1, f1, f2, ans_c_u2, ans_c_v2, calc_phase="c1")
    # # 画像2の中心座標(cu2, cv2)を算出
    # calc_inside_param(F8, e1, f1, f2, ans_c_u1, ans_c_v1, calc_phase="c2")

    #####################################################
    
    #### カメラ行列A1, A2から作ってFを算出し、f1=2.3, f2=3.4が一致するかテスト ####
    # A1 = np.array([[2.3, 0, 0], [0, 2.3, 0], [0, 0, 1]])
    # A2 = np.array([[3.4, 0, 0], [0, 3.4, 0], [0, 0, 1]])
    # r1, r2, r3 = 0.1, 0.2, 0.1
    # rot_x = np.array([[1, 0, 0], [0, np.cos(r1), -np.sin(r1)], [0, np.sin(r1), np.cos(r1)]])
    # rot_y = np.array([[np.cos(r2), 0, np.sin(r2)], [0, 1, 0], [-np.sin(r2), 0, np.cos(r2)]])
    # rot_z = np.array([[np.cos(r3), -np.sin(r3), 0], [np.sin(r3), np.cos(r3), 0], [0, 0, 1]])
    # R = np.dot(np.dot(rot_x, rot_y), rot_z)
    # T = np.array([0.5, 0.05, 0.03])
    # r1, r2, r3 = R.T
    # E = np.array([np.cross(T, r1), np.cross(T, r2), np.cross(T, r3)]).T
    # print(E)
    # F = np.dot(np.dot(LA.inv(A1.T), E), LA.inv(A2))
    # print(F)
    # # エピポールe1を算出
    # e1 = calc_epipole(F.T)
    # print("e1: {}".format(e1))
    # c_u1 = c_v1 = c_u2 = c_v2 = 0
    # # 内部パラメータを算出
    # calc_inside_param(F, e1, c_u1, c_v1, c_u2, c_v2, calc_phase="f")
    