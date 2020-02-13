import cv2

es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 4))

cap = cv2.VideoCapture(0)
while True:
    # Capture a frame
    flag, frame = cap.read()

    current = cv2.blur(frame, (5, 5))
    previous = cv2.blur(frame, (5, 5))
    difference = cv2.absdiff(current, previous)

    frame2 = frame.copy()
    frame2[(frame[..., 1] < 180) | (frame[..., 2] < 150)] = 0

    cv2.imshow('window_a', frame2)
    cv2.imshow('window_b', frame)

    previous = current

    key = cv2.waitKey(10)  # 20
    if key == 27:  # exit on ESC
        cv2.destroyAllWindows()
        break
