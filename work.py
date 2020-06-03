import numpy as np

from calc_Fmatrix import calc_Fmatrix
from draw_images import draw_images

if __name__ == '__main__':
    uv_mat = np.array([[207, 193, 312, 256],
                    [251, 279, 432, 330],
                    [330, 279, 508, 290],
                    [451, 208, 548, 167],
                    [438, 145, 522, 104],
                    [386, 109, 404, 85],
                    [273, 135, 332, 155],
                    [288, 185, 451, 206]])

    pic_paths = ["img/resize1.jpg", "img/resize2.jpg"]

    # Fを算出
    F = calc_Fmatrix(uv_mat)
    # 2枚の画像にエピポーラ線を描画
    draw_images(F, uv_mat, pic_paths)