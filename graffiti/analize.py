# -*- coding: utf-8 -*-
import numpy as np
import cv2
import copy
import sys

# 2点間の距離を算出する関数


def calc_dist(x1, y1, x2, y2):
    a = np.array([x1, y1])
    b = np.array([x2, y2])
    length = np.linalg.norm(a - b)
    return length

# 元画像の読み込み
img = cv2.imread('img/images.jpg')


# 攻撃力の算出(直線が多い)
attack_point = 0

# 直線検出
img_atk = copy.deepcopy(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.bitwise_not(gray)
lines = cv2.HoughLinesP(gray2, rho=1, theta=np.pi / 360,
                        threshold=200, minLineLength=80, maxLineGap=10)

if lines is not None:
    # とりあえず直線数 % 255, 直線が検出されない場合はランダム
    attack_point = lines.shape[0] % 255

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img_atk, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # cv2.imshow('sample image', img_atk)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
else:
    print('lines have not been detected...')
    attack_point = np.random.randint(255)

print('attack_point: ' + str(attack_point))


# 防御力の算出（画素が中心に寄っている）
img_def = copy.deepcopy(img)
defence_point = 0

# 中心部分を算出
height, width = img_def.shape[:2]
center_coordinate_x = int(width / 2)
center_coordinate_y = int(height / 2)

# ドットをすべて走査
length_array = []
for x in range(height):
    for y in range(width):
        # ドットの場合は中心からの距離を求める
        if not all(img_def[x, y] == 255):  # 画素が白の場合（RGBすべてが255でない）
            l = calc_dist(x, y, center_coordinate_x, center_coordinate_y)
            length_array.append(l)

if length_array is None:
    print('length_array is None. Maybe all pixel are white...')
    sys.exit()

# lengthを正規化する（中心から角までの値で割る）
# 偏差を求める
mean_length = np.mean(length_array)
dev_length_array = np.abs(length_array - mean_length)
l = calc_dist(width, height, center_coordinate_x, center_coordinate_y)
max_length = np.abs(l - mean_length)

# 正規化する
norm_length_array = dev_length_array / max_length
# 正規化後の平均を求める
mean_norm_length = np.mean(norm_length_array)
defence_point = int(mean_norm_length * 255)

print('defence_point:', defence_point)
