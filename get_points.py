import cv2
import numpy as np

from glob import glob

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
    # 入力画像
    paths = sorted(glob("movie/**.jpg"))
    print(paths)

    for i, path in enumerate(paths):

        coordinate_point = []

        # 入力画像
        img = cv2.imread(path)
        # 画像表示時に大きくなりすぎることがあったので1/2に縮小
        # orgHeight, orgWidth = img.shape[:2]
        # size = (int(orgWidth/2), int(orgHeight/2))
        # img = cv2.resize(img, size)
        # print(size)

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

                print(coordinate_point)

            # 右クリックがあったら終了
            elif mouseData.getEvent() == cv2.EVENT_RBUTTONDOWN:
                break

        cv2.destroyAllWindows()

        alter_point = []
        for p in coordinate_point:
            alter_point.append(list(p))
        alter_point = np.array(alter_point)

        if i == 0:
            uv_mat = alter_point[:, :]

        else:
            uv_mat = np.concatenate([uv_mat, alter_point], axis=1)

        print(uv_mat)

    # npy形式にして保存
    np.save("movie/uv_mat", uv_mat)
