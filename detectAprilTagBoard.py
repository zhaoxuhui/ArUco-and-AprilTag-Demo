import cv2
import pupil_apriltags as apriltag

if __name__ == '__main__':
    # step1 读取影像并转成灰度(OpenCV中的AprilTag只支持灰度影像)
    img_path = "apriltag_test.jpg"  # 待检测影像路径
    img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # step2 构造检测器开始检测
    detector = apriltag.Detector()
    results = detector.detect(img_gray)
    print("Found ", len(results), "apriltag markers")

    # step3 解析结果
    markerCorners = []
    markerIds = []
    for i in range(len(results)):
        tmp_obj = results[i]
        markerCorners.append([tmp_obj.corners])
        markerIds.append(tmp_obj.tag_id)

    # step4 可视化结果
    # 需要注意的是AprilTag检测结果角点的顺序是逆时针的：左下→右下→右上→左上
    # 另外，检测的坐标是浮点型小数，可视化的时候需要转成int类型
    for i in range(len(markerCorners)):
        tmp_marker = markerCorners[i][0]
        print("Marker ID:", markerIds[i])
        print(tmp_marker)
        tmp_marker_tl = (int(tmp_marker[3][0]), int(tmp_marker[3][1]))
        tmp_marker_tr = (int(tmp_marker[2][0]), int(tmp_marker[2][1]))
        tmp_marker_br = (int(tmp_marker[1][0]), int(tmp_marker[1][1]))
        tmp_marker_bl = (int(tmp_marker[0][0]), int(tmp_marker[0][1]))
        cv2.circle(img, tmp_marker_tl, 10, (0, 0, 255), -1)
        cv2.circle(img, tmp_marker_tr, 10, (0, 255, 0), -1)
        cv2.circle(img, tmp_marker_br, 10, (255, 0, 0), -1)
        cv2.circle(img, tmp_marker_bl, 10, (0, 170, 255), -1)
        cv2.putText(img, "ID: " + str(markerIds[i]), (int(tmp_marker_tl[0] + 10), int(tmp_marker_tl[1] + 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1,
                    cv2.LINE_AA)

    # step5 保存图片
    cv2.imwrite("apriltag_detection.jpg", img)
