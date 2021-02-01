from cv2 import cv2 
import os
import numpy as np
import time

# from PIL import Image
def getNumberLocation(im, pwd):
    numbers = set(list(pwd))
    templates = {}
    positions = {}
    nimgpath = ''
    # nimgpath = 'D:\workplace\python\getStockData\images\FuTu'
    for i in numbers:
        templates[i]  = os.path.join(nimgpath, "n{}.png".format(i))

    start = time.time()
    img_rgb = cv2.imread(im)
    print(templates.items())
    print('img_rgb')
    print(img_rgb)
    # imTest = Image.open(im)
    # print(imTest)
    for teNum, tepath in templates.items():
        print(tepath)
        template = cv2.imread(tepath)
        h, w = template.shape[:-1]
        template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        threshold = .95    # 匹配度参数，1为完全匹配
        loc = np.where(res >= threshold)
        if len(loc) > 0:
            positions[teNum] = list(zip(*loc[::-1]))[0]
        else:
            print("Can not found number: [{}] in image: [{}].".format(tepath, im))

    end = time.time()
    print(end-start)

    return [positions[n] for n in pwd]

# if __name__ == "__main__":
#     ls = get_pay_keyboard_number_location('D:\test\img\sekeyboard.png', '123456')
#     print(ls)