import numpy as np
import numpy.linalg as LA
import cv2

def calc_Fmatrix(uv_mat):
    """ 対応点から8点アルゴリズムによりFを算出 """

    n = uv_mat.shape[0]
    print("points: {}".format(n))

    mat = np.zeros((n, 9))

    for i in range(n):
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

    # Fの固有値
    value, _ = LA.eig(F)
    print("Fの固有値=", value)
    # Fの特異値
    U, D, V = LA.svd(F)
    print("Fの特異値: {}".format(D))
    # Fのランク
    print("F_rank=",LA.matrix_rank(F))

    for i in range(n):
        # x1 = [u1, u2, 1], x2 = [u2, v2, 1]
        x1 = np.array([uv_mat[i, 0], uv_mat[i, 1], 1.0])
        x2 = np.array([uv_mat[i, 2], uv_mat[i, 3], 1.0])
        # x2^T * F * x1 = 0 のチェック
        a = np.dot(x2.T, F)
        print(np.dot(a, x1))

    return F

def calc_epipole(F):
    """ F行列からエピポールeを算出 """

    # Fを特異値分解
    U, D, V = LA.svd(F)
    # Vから固有値最小の固有ベクトルを取り出す
    fvec = V[2]

    return fvec / fvec[2]

def calc_Fmatrix_by5points(uv_mat, A1, A2):
    x1 = uv_mat[:, :2].astype('float32')
    x2 = uv_mat[:, 2:4].astype('float32')
    print(A1.shape)
    x1_norm = cv2.undistortPoints(np.expand_dims(x1, axis=1), cameraMatrix=A1, distCoeffs=None)
    x2_norm = cv2.undistortPoints(np.expand_dims(x2, axis=1), cameraMatrix=A2, distCoeffs=None)
    # print(x1_norm.shape)
    # x1_norm = x1.reshape(5, 2)
    # x2_norm = x2.reshape(5, 2)
    E, mask = cv2.findEssentialMat(x1_norm, x2_norm, focal=1, pp=(480, 853), method=cv2.RANSAC, prob=0.999, threshold=3.0)
    # E, mask = cv2.findEssentialMat(x1, x2, cameraMatrix=A1, #focal=1.0, pp=(0., 0.),
    #                                 method=cv2.RANSAC, prob=0.999, threshold=3.0
    #                                 )
    print(E.shape, mask)
    print(E)
    A1_inv = LA.inv(A1)
    A2_inv = LA.inv(A2)
    F = np.multiply(A1_inv.T, E, A2_inv)
    return F
