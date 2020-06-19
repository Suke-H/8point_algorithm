import cv2
import numpy as np
from PIL import Image

def cut_movie(path):
    # ビデオ読み込み
    cap = cv2.VideoCapture(path)
    pictures = []
    print(path)

    while True:
        # 1フレーム分読み込み
        ret, frame = cap.read()

        if ret:
            print(frame.shape)
            # BGR -> RGB
            frame = frame[:, :, [2, 1, 0]]
            # 1フレームずつappend
            pictures.append(frame)

        else:
            break

    pictures = np.array(pictures)
    print(pictures.shape)
    return pictures

if __name__ == '__main__':
    # 動画を画像に分解
    pictures = cut_movie("movie/target.mp4")
    # 欲しいフレームを選択して保存
    pictures = pictures[[26, 40, 53, 67, 80]]
    for i, pic in enumerate(pictures):
        im = Image.fromarray(pic)
        im.save('movie/'+str(i)+'.jpg')
