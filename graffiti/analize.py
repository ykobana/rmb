# -*- coding: utf-8 -*-
import numpy as np
import cv2
import copy
import sys


def main(args):
    # 元画像の読み込み
    img = cv2.imread(args[1])
    graffiti_analyzer = GraffitiAnalyzer()

    # 体力の算出
    hit_point = graffiti_analyzer.analyze_hit_point(img)
    print('hit_point: ' + str(hit_point))

    # 魔法力の算出
    magic_point = graffiti_analyzer.analyze_magic_point(img)
    print('magic_point: ' + str(magic_point))

    # 攻撃力の算出(直線が多い)
    attack_point = graffiti_analyzer.analyze_attack_point(img)
    print('attack_point: ' + str(attack_point))

    # 防御力の算出（画素が中心に寄っている）
    defence_point = graffiti_analyzer.analyze_defence_point(img)
    print('defence_point:', defence_point)

    # 俊敏力の算出（上半分と下半分の画素の割合がが均一）
    speed_point = graffiti_analyzer.analyze_speed_point(img)
    print('speed_point:', speed_point)

    # 運命力の算出（ランダム）
    luck_point = graffiti_analyzer.analyze_luck()
    print('luck_point:', luck_point)


class GraffitiAnalyzer:
    # 初期化
    def __init__(self):
        pass

    # 2点間の距離を算出する関数
    def calc_dist(self, x1, y1, x2, y2):
        a = np.array([x1, y1])
        b = np.array([x2, y2])
        length = np.linalg.norm(a - b)
        return length


    # 体力を算出する関数
    def analyze_hit_point(self, img):
        return 1000


    # 魔法力を算出する関数
    def analyze_magic_point(self, img):
        return 1000


    # 攻撃力を算出する関数
    def analyze_attack_point(self, img):
        attack_point = 0

        # 直線検出
        img_atk = copy.deepcopy(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.bitwise_not(gray)
        lines = cv2.HoughLinesP(gray2, rho=1, theta=np.pi / 360,
                                threshold=200, minLineLength=80, maxLineGap=10)

        if lines is not None:
            # とりあえず直線数 % 255, 直線が検出されない場合はランダムの値を返却
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

        return attack_point


    # 防御力を算出する関数（画像の画素が中心に寄っている）
    def analyze_defence_point(self, img):
        defence_point = 0
        img_def = copy.deepcopy(img)

        # 中心部分を算出
        height, width = img_def.shape[:2]
        center_coordinate_x = int(width / 2)
        center_coordinate_y = int(height / 2)

        # ドットをすべて走査
        length_array = []
        for x in range(width):
            for y in range(height):
                # ドットの場合は中心からの距離を求める
                if not all(img_def[y, x] == 255):  # 画素が白でない場合（RGBすべてが255でない）
                    l = self.calc_dist(y, x, center_coordinate_y, center_coordinate_x)
                    length_array.append(l)

        if length_array is None:
            print('length_array is None. Maybe all pixel are white...')
            sys.exit()

        # lengthを正規化する（中心から角までの値で割る）
        # 偏差を求める
        mean_length = np.mean(length_array)
        dev_length_array = np.abs(length_array - mean_length)
        l = self.calc_dist(width, height, center_coordinate_x, center_coordinate_y)
        max_length = np.abs(l - mean_length)

        # 正規化する
        norm_length_array = dev_length_array / max_length
        # 正規化後の平均を求める
        mean_norm_length = np.mean(norm_length_array)
        defence_point = 255 - int(mean_norm_length * 255)

        return defence_point


    # 俊敏力を算出する関数（画像の画素の上下の割合が均一）
    def analyze_speed_point(self, img):
        speed_point = 0

        # 全ドット数、上半分のドット数、下半分のドット数計算
        upper_half_dots = 0
        lower_half_dots = 0
        height, width = img.shape[:2]
        center_coordinate_y = int(height / 2)
        length_array = []
        for x in range(width):
            for y in range(height):
                # ドットの場合は中心からの距離を求める
                if not all(img[y, x] == 255):  # 画素が白でない場合（RGBすべてが255でない）
                    if y < center_coordinate_y:  # y座標が中心よりも上にある場合
                        upper_half_dots += 1
                    else:
                        lower_half_dots += 1

        # 上半分のドット数の割合、下半分のドット数の割合を計算
        upper_half_ratio = upper_half_dots / (upper_half_dots + lower_half_dots)
        lower_half_ratio = lower_half_dots / (upper_half_dots + lower_half_dots)

        # 上半分のドット数の割合、下半分のドット数の割合に対して、低い方/高い方*255で俊敏力を計算する
        if upper_half_ratio > lower_half_ratio:
            speed_point = 255 * (lower_half_ratio / upper_half_ratio)
        else:
            speed_point = 255 * (upper_half_ratio / lower_half_ratio)

        return int(speed_point)


    # 運命力を算出する関数（ランダム）
    def analyze_luck(self):
        luck_point = np.random.randint(255)
        return luck_point



# main関数
if __name__ == '__main__':
    main(sys.argv)
