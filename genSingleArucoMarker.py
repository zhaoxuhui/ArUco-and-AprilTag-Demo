import cv2
import numpy as np

if __name__ == '__main__':
    marker_size = 200  # marker影像大小
    marker_id = 50  # marker的ID
    marker_boarder = 1  # marker边界

    # step1 加载预定义的字典
    dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

    # step2 新建一张空白影像用于存放marker
    markerImg = np.zeros([marker_size, marker_size], np.uint8)

    # step3 获得marker内容并赋值
    # 第一个参数：使用的字典
    # 第二个参数：marker的id
    # 第三个参数：marker影像的像素大小
    # 第四个参数：边界宽度参数，表示将多少位(块)作为边界添加到marker中
    markerImg = cv2.aruco.drawMarker(dict, marker_id, marker_size, marker_boarder)

    # step4 保存marker
    cv2.imwrite("aruco_" + str(marker_id).zfill(3) + ".png", markerImg)
