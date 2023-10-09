import cv2
class normal_zumbie:
    def __init__(self, icon, x, y) -> None:
        self.img = cv2.imread(icon) 
        self.img = cv2.resize(self.img, (90,90))# 获取图标
        self.x = x
        self.y = y
        self.step = 2
        pass
    def draw(self,window):
        window[self.y:self.y+90, self.x:self.x+90] = self.img
    def update(self):
        self.step -= 1
        if self.step == 0:
            self.x -= 1
            self.step = 2