import cv2
import numpy as np

class mouseParam:
    def __init__(self, input_img_name):
        self.mouseEvent = {"x":None, "y":None, "event":None, "flags":None}
        cv2.setMouseCallback(input_img_name, self.__CallBackFunc, None)
    
    def __CallBackFunc(self, eventType, x, y, flags, userdata):
        
        self.mouseEvent["x"] = x
        self.mouseEvent["y"] = y
        self.mouseEvent["event"] = eventType    
        self.mouseEvent["flags"] = flags    

    def getData(self):
        return self.mouseEvent
    
    def getEvent(self):
        return self.mouseEvent["event"]                

    def getFlags(self):
        return self.mouseEvent["flags"]                

    def getX(self):
        return self.mouseEvent["x"]  

    def getY(self):
        return self.mouseEvent["y"]  

    def getPos(self):
        return (self.mouseEvent["x"], self.mouseEvent["y"])
        

if __name__ == "__main__":
    # 入力画像2枚のパス
    paths = ["img/img1.JPG", "img/img3.JPG"]
    coordinate_point = []

    for i, path in enumerate(paths):
        # 入力画像
        img = cv2.imread(path)
        # 画像表示時に大きくなりすぎることがあったので1/2に縮小
        orgHeight, orgWidth = img.shape[:2]
        size = (int(orgWidth/2), int(orgHeight/2))
        img = cv2.resize(img, size)
        print(size)

        # Window名
        window_name = "input window"

        # 画像の表示
        cv2.imshow(window_name, img)

        mouseData = mouseParam(window_name)

        while 1:
            cv2.waitKey(20)

            # 左クリックをした座標を格納
            if mouseData.getEvent() == cv2.EVENT_LBUTTONDOWN:
                coordinate_point.append(mouseData.getPos())
                coordinate_point=list(dict.fromkeys(coordinate_point))

            # 右クリックがあったら終了
            elif mouseData.getEvent() == cv2.EVENT_RBUTTONDOWN:
                break

        cv2.destroyAllWindows()

        print(coordinate_point)

    # 対応点の数(画像1,2で同じ数であることが条件)
    num = int(len(coordinate_point)/2)
    print(num)

    # [[u1, v1, u2, v2], ...]の形にする
    uvmat=[coordinate_point[idx]+coordinate_point[idx+num] for idx in range(num)]
    uvmat = np.array(uvmat)
    print(uvmat)

    # npy形式にして保存
    np.save("img/uv_mat2", uvmat)
