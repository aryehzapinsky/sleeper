import numpy as np
import cv2

cap = cv2.VideoCapture('in3.mp4')
cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap_fps = int(cap.get(cv2.CAP_PROP_FPS))
cap_fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))

wrt = cv2.VideoWriter('out3.mp4', cap_fourcc, cap_fps, (cap_width, cap_height))

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    fgmask = np.expand_dims(fgmask, axis=2)
    sub_frame = np.array(frame-fgmask)

    sum_mask = np.sum(fgmask)
    cv2.putText(sub_frame, "Sum: {}".format(sum_mask), (10, 500),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
    threshold_value = 100000
    if sum_mask > threshold_value:
        cv2.putText(sub_frame, "RECORDING", (10, 600),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
    wrt.write(sub_frame)
    #wrt.write(fgmask)
    # cv2.imshow('frame',fgmask)
    # k = cv2.waitKey(30) & 0xff
    # if k == 27:
    #     break

cap.release()
wrt.release()
#cv2.destroyAllWindows()
