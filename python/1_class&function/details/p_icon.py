import cv2
class double_pea_icon:
    def __init__(self, icon, x, y) -> None:
        self.img = cv2.imread(icon)
        self.img = cv2.resize(self.img, (90,90)) # 获取图标
        self.x = x
        self.y = y
        pass
    def draw(self,window):
        window[self.y:self.y+90, self.x:self.x+90] = self.img
