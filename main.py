import cv2

# 카메라 영상을 받아올 객체 선언 및 설정 (영상소스, 해상도 설정)
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,720)

# 무한루프
while True:
    ret, frame = capture.read() # 카메라로부터 현재 영상을 받아 frame에 저장, 잘 받았다면 ret가 참
    cv2.imshow("original", frame) #frame(카메라 영상)을 original 이라는 창을 띄워줌
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindoes()



