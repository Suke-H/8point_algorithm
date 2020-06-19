import numpy as np
import numpy.linalg as LA
import cv2

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