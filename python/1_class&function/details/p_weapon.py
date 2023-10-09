import numpy as np
import cv2


class pea_double:
    def __init__(self, x, y) -> None:
        self.cycle0 = 10
        self.cycle1 = 5
        self.shot_num = 0
        self.x = x
        self.y = y
        pass
    def shot(self, warheadlist:list):
        self.cycle0 -= 1
        # print(self.cycle0,self.cycle1)
        if self.cycle0 == 0:
            warheadlist.append(pea(self.x, self.y))
        elif self.cycle0 == -1:
            self.cycle0+=1
            self.cycle1 -= 1
            if self.cycle1 == 0:
                warheadlist.append(pea(self.x, self.y))
                self.cycle0 = 40
                self.cycle1 = 5








# 子弹

class pea:
    def __init__(self, x, y) -> None:
        self.damage = 25
        self.x = x
        self.y = y
        self.speed = 20
        pass
    def show(self, window):
        cv2.circle(window, (self.x, self.y), 5, (0, 256, 0), -1) # 在x，y处画个绿圈作为子弹
        pass
    def update(self):
        self.x += self.speed
    def __del__(self):
        pass

if __name__ == "__main__":
    p = pea_double(1,1)