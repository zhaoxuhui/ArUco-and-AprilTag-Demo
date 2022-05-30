import cv2
import numpy as np

if __name__ == '__main__':
    grid_rows = 3  # 行数
    grid_cols = 5  # 列数
    grid_interval = 10  # marker之间的间隔像素
    grid_size = 200  # 单个marker像素大小
    marker_boarder = 1  # 单个marker边界
    grid_background = 1  # 0-black, 1-white

    # step1 加载预定义的字典
    dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

    # step2 新建一张空白影像用于存放marker
    img_height = grid_rows * grid_size + (grid_rows + 1) * grid_interval
    img_width = grid_cols * grid_size + (grid_cols + 1) * grid_interval
    markerImg = np.zeros([img_height, img_width], np.uint8)
    if grid_background == 1:
        markerImg += 255

    for i in range(grid_cols):
        for j in range(grid_rows):
            tmp_index = i * grid_rows + j
            start_x = j * grid_size + (j + 1) * grid_interval
            start_y = i * grid_size + (i + 1) * grid_interval
            # step3 获得marker内容并赋值
            tmp_marker = cv2.aruco.drawMarker(dict, tmp_index, grid_size, marker_boarder)
            markerImg[start_x:start_x + grid_size, start_y:start_y + grid_size] = tmp_marker

    # step4 保存marker
    cv2.imwrite("arucoBoard.png", markerImg)
