import cv2

if __name__ == '__main__':
    # step1 读取待检测影像
    img_path = "aruco_test.jpg"  # 影像路径
    img = cv2.imread(img_path)

    # step2 指定待检测Marker的字典并开始检测
    used_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
    markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(img, used_dict)

    # step3 解析结果并可视化
    # 需要注意的是ArUco检测结果角点的顺序是顺时针的：左上→右上→右下→左下
    # 另外，检测的坐标是整型数
    for i in range(len(markerCorners)):
        tmp_marker = markerCorners[i][0]
        print("Marker ID:", markerIds[i])
        print(tmp_marker)
        tmp_marker_tl = (tmp_marker[0][0], tmp_marker[0][1])
        tmp_marker_tr = (tmp_marker[1][0], tmp_marker[1][1])
        tmp_marker_br = (tmp_marker[2][0], tmp_marker[2][1])
        tmp_marker_bl = (tmp_marker[3][0], tmp_marker[3][1])
        cv2.circle(img, tmp_marker_tl, 10, (0, 0, 255), -1)
        cv2.circle(img, tmp_marker_tr, 10, (0, 255, 0), -1)
        cv2.circle(img, tmp_marker_br, 10, (255, 0, 0), -1)
        cv2.circle(img, tmp_marker_bl, 10, (0, 170, 255), -1)
        cv2.putText(img, "ID: " + str(markerIds[i]), (int(tmp_marker_tl[0] + 10), int(tmp_marker_tl[1] + 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1,
                    cv2.LINE_AA)

    # step4 保存图片
    cv2.imwrite("aruco_detection.jpg", img)
