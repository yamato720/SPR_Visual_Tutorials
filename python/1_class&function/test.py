import details.p_weapon as pw
import details.p_icon as pi
import details.z_armor as za
import details.z_icon as zi
import details.z_weapon as zw
import numpy as np
import cv2
class Plant:
    def __init__(self, p_life, p_weapon, p_icon, p_dead_voice = None) -> None:   # 构造函数，当该类构造成一个对象后自动运行，其中dead_voice默认为无
        self.p_life = p_life
        self.p_weapon = p_weapon
        self.p_icon = p_icon
        self.p_dead_voice = p_dead_voice
        pass
    def __del__(self): # 析构函数
        
        pass

class zumbie:
    def __init__(self, z_life, z_armor, z_weapon, z_icon, z_dead_voice = None) -> None:
        self.z_life = z_life
        self.z_armor = z_armor
        self.z_weapon = z_weapon
        self.z_icon = z_icon
        self.z_dead_voice = z_dead_voice
        self.total = self.z_life
        self.current = self.total
        pass
    def get_damage(self, damage): # 公有函数
        self.current -= damage
        if self.current < 0:
            del()

    def __del__(self):
        print("僵尸死了！")
        pass

class double_pea(Plant) : 
    def __init__(self, p_life, p_weapon:pw.pea_double, p_icon=None, p_dead_voice=None) -> None:
        super().__init__(p_life, p_weapon, p_icon, p_dead_voice)
    def __del__(self):
        return super().__del__()

class Plant_zumbie(Plant, zumbie):
    def __init__(self, p_life, p_weapon, p_icon, p_dead_voice=None) -> None:
        Plant.__init__(self, p_life, p_weapon, p_icon, p_dead_voice)
        zumbie.__init__(self, 1,1,1,zi.normal_zumbie(r'python\1_class&function\pic\zumbie.jpg',810,210))



# a = Plant_zumbie(0,pw.pea_double(50,250),1) # 植物僵尸的废案
warheadlist = [] # 子弹列表

b_channel = np.ones((510, 910), dtype=np.uint8) * 127
g_channel = np.ones((510, 910), dtype=np.uint8) * 196
r_channel = np.ones((510, 910), dtype=np.uint8) * 119
background = cv2.merge((b_channel, g_channel, r_channel))# 创建三个颜色通道并合并起来
for i in range(0,510,100):
    background[i:i+10,0:910] = (171,236,250)
for i in range(0,910,100):
    background[0:510,i:i+10] = (171,236,250)
# 画草坪
# 可放置的点位：从(10,10)开始，每一格加100(中心为50,50)
double0 = double_pea(1,pw.pea_double(50,250),pi.double_pea_icon(r'python\1_class&function\pic\double_pea.jpg',10,210))
zumbie0 = zumbie(200,1,1,zi.normal_zumbie(r'python\1_class&function\pic\zumbie.jpg',810,210))
time = 30 # 每帧30ms刚好大概是30帧
while True:
    img = background.copy() # 深拷贝
    if double0 != None and zumbie0 != None:
        double0.p_icon.draw(img)
        double0.p_weapon.shot(warheadlist)
        zumbie0.z_icon.update()
        zumbie0.z_icon.draw(img)
        over = -1
        for i in range(len(warheadlist)):
            warheadlist[i].update()
            # print(len(warheadlist))
            if warheadlist[i].x >= zumbie0.z_icon.x :
                # print("删除后：",len(warheadlist))
                over = i
                zumbie0.get_damage(warheadlist[i].damage)
                print("僵尸剩余血量：",zumbie0.current)
                
            else:
                warheadlist[i].show(img)
        if over != -1: del warheadlist[over]
        if zumbie0.current <= 0:
            del zumbie0
            zumbie0 = None
        cv2.imshow("PvZ",img)
        # del zumbie0
    else: time = 0
    if cv2.waitKey(time) & 0xFF == 27: # 按“esc”退出
        break
