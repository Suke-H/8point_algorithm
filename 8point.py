import numpy as np
import numpy.linalg as LA

from draw_image import draw_lines

width = 768
height = 432
 
uvmat = np.array([[207, 193, 312, 256],
                    [251, 279, 432, 330],
                    [330, 279, 508, 290],
                    [451, 208, 548, 167],
                    [438, 145, 522, 104],
                    [386, 109, 404, 85],
                    [273, 135, 332, 155],
                    [288, 185, 451, 206]])

mat = np.zeros((8, 9))

for i in range(8):
    mat[i, 0] = uvmat [i, 0] * uvmat [i, 2]
    mat[i, 1] = uvmat [i, 1] * uvmat [i, 2]
    mat[i, 2] = uvmat [i, 2]
    mat[i, 3] = uvmat [i, 0] * uvmat [i, 3]
    mat[i, 4] = uvmat [i, 1] * uvmat [i, 3]
    mat[i, 5] = uvmat [i, 3]
    mat[i, 6] = uvmat [i, 0]
    mat[i, 7] = uvmat [i, 1]
    mat[i, 8] = 1.0

# mattmat = np.dot(mat.T, mat)
# value, vec = LA.eig(mattmat)

# matを特異値分解
U, D, V = LA.svd(mat)
# Vから固有値最小の固有ベクトルを取り出してFにする
F = V[8].reshape((3, 3)).T

### 以下の処理はコメントにしても大丈夫、あると精度がよくなる
# Fのランクを2にする
U, D, V = LA.svd(F)
F = np.dot(U, np.diag([D[0], D[1], 0]))
F = np.dot(F, V.T)
### おわり

# Nにより正規化
N = np.array([[2/width, 0, -1],
            [0, 2/height, -1],
            [0, 0, 1]])
F = np.dot(N.T, F)
F = np.dot(F, N)

print(F)

# Fの固有値は[1,0,0]になる
value, vec = LA.eig(F)

print(value)

# F = value.reshape((3, 3))
# F = []
# values = []
# for i in range(9):
#     F.append(vec[i].reshape((3, 3)))
#     values.append(value[i])
# print(F)

# F = vec[8].reshape((3, 3))

for i in range(8):
    # x1 = [u1, u2, 1], x2 = [u2, v2, 1]
    x1 = np.array([uvmat[i, 0], uvmat[i, 1], 1.0])
    x2 = np.array([uvmat[i, 2], uvmat[i, 3], 1.0])
    #print(x1, x2)

    # Nにより正規化
    x1 = np.dot(N, x1.T)
    x2 = np.dot(N, x2.T)
    # x3 = np.array([width/2, height/2, 1])
    # x3 = np.dot(N, x3.T)
    # print(x1, x2, x3)

    # x2^T * F * x1 = 0 のチェック
    # a = np.dot(x2.T, F)
    # print(a, np.dot(a, x1))
    b = np.dot(F.T, x2)
    print(b, np.dot(x1.T, b))

print("="*50)
draw_lines(F, uvmat)