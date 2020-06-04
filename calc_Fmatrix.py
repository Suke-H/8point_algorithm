import numpy as np
import numpy.linalg as LA

def calc_Fmatrix(uv_mat):

    mat = np.zeros((8, 9))

    for i in range(8):
        mat[i, 0] = uv_mat [i, 0] * uv_mat [i, 2]
        mat[i, 1] = uv_mat [i, 1] * uv_mat [i, 2]
        mat[i, 2] = uv_mat [i, 2]
        mat[i, 3] = uv_mat [i, 0] * uv_mat [i, 3]
        mat[i, 4] = uv_mat [i, 1] * uv_mat [i, 3]
        mat[i, 5] = uv_mat [i, 3]
        mat[i, 6] = uv_mat [i, 0]
        mat[i, 7] = uv_mat [i, 1]
        mat[i, 8] = 1.0

    # matを特異値分解
    U, D, V = LA.svd(mat)
    # Vから固有値最小の固有ベクトルを取り出してFにする
    F = V[8].reshape((3, 3))

    # これでもいけるはずだけどできない
    # value, vec = LA.eig(np.dot(mat.T, mat))
    # F = vec[8].reshape((3, 3))

    print("F=",F)
    print("F_rank=",LA.matrix_rank(F))
    # Fの固有値は[1,0,0]になる
    value, _ = LA.eig(F)
    print("Fの固有値=", value)

    # Fのランクを2にする(うまく動作しない)
    # U, D, V = LA.svd(F)
    # d = np.sqrt(D[0]**2 + D[1]**2)
    # print(np.diag([D[0]/d, D[1]/d, 0]))
    # F = np.dot(U, np.diag([D[0]/d, D[1]/d, 0]))
    # F = np.dot(F, V.T)
    # print("F'=",F)

    # print("F_rank=",LA.matrix_rank(F))

    # # Fの固有値は[1,0,0]になる
    # value, _ = LA.eig(F)
    # print("Fの固有値=", value)

    for i in range(8):
        # x1 = [u1, u2, 1], x2 = [u2, v2, 1]
        x1 = np.array([uv_mat[i, 0], uv_mat[i, 1], 1.0])
        x2 = np.array([uv_mat[i, 2], uv_mat[i, 3], 1.0])

        # x2^T * F * x1 = 0 のチェック
        a = np.dot(x2.T, F)
        print(np.dot(a, x1))

    return F

def calc_epipole(F):
    # F^Tを特異値分解
    U, D, V = LA.svd(F)
    # Vから固有値最小の固有ベクトルを取り出す
    fvec = V[2]

    # こっちだとやっぱりできない
    # value, vec = LA.eig(np.dot(F, F.T))
    # fvec = vec[2]
    # print(fvec / fvec[2])

    return fvec / fvec[2]


