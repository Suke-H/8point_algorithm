import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from glob import glob

""" 対応点描画用 """

# getpoint.pyにより取り出した対応点を読み込み
uv_mat = np.load("movie/uv_mat.npy")

# 入力画像のパス
paths = sorted(glob("movie/**.jpg"))
print(paths)

for i, path in enumerate(paths):
    # 各画像の対応点を取り出す
    u = uv_mat[:, 2*i]
    v = uv_mat[:, 2*i+1]

    # 対応点のプロット
    plt.plot(u, v, marker="o",linestyle="None", color="red")  

    # 画像の読み込み
    img = np.array(Image.open(path))

    # 画像の表示
    plt.imshow(img)

    plt.show()
    plt.close()
