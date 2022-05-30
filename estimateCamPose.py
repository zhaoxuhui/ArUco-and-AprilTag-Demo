import cv2
import numpy as np

if __name__ == '__main__':
    src_pts = []  # 某个Marker角点理论坐标值
    tar_pts = []  # 某个Marker角点实际坐标值

    # 构造第一个Marker的角点理论坐标值
    src_tl_pt = (0, 0)
    src_tr_pt = (200, 0)
    src_br_pt = (200, 200)
    src_bl_pt = (0, 200)
    src_pts.append(src_tl_pt)
    src_pts.append(src_tr_pt)
    src_pts.append(src_br_pt)
    src_pts.append(src_bl_pt)
    print("Src pts:\n", src_pts)

    # 读取影像
    img_path = "aruco_test.jpg"
    img = cv2.imread(img_path)

    # 检测Marker
    used_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
    markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(img, used_dict)

    # 获取第一个Marker的角点坐标
    # 需要注意的是，返回的列表并不是按照marker ID排序的，所以要获取ID为0的索引
    marker0_index = list(markerIds).index([0])
    tmp_block = markerCorners[marker0_index][0]
    tar_tl_pt = (tmp_block[0][0], tmp_block[0][1])
    tar_tr_pt = (tmp_block[1][0], tmp_block[1][1])
    tar_br_pt = (tmp_block[2][0], tmp_block[2][1])
    tar_bl_pt = (tmp_block[3][0], tmp_block[3][1])
    tar_pts.append(tar_tl_pt)
    tar_pts.append(tar_tr_pt)
    tar_pts.append(tar_br_pt)
    tar_pts.append(tar_bl_pt)
    print("Target pts:\n", tar_pts)

    # 利用得到的对应关系计算单应变换
    homo_mat, mask = cv2.findHomography(np.array(src_pts), np.array(tar_pts))
    print("Homography matrix:\n", homo_mat)
