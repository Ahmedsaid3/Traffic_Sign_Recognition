import glob
import numpy as np
import cv2
import darknet
import matplotlib.pyplot as plt
network, class_names, colors = darknet.load_network("/home/oem/Desktop/gat/asaid/yolo/yolov4-obj.cfg","/home/oem/Desktop/gat/asaid/yolo/obj_teamblg.data","/home/oem/Desktop/gat/asaid/yolo/backup/yolov4-obj_last.weights")
width = darknet.network_width(network)
height = darknet.network_height(network)

# egıtımımın ilk sonucu (array olarak)
"""
array = np.load("confusion_matrix.npy")
print(array)
"""

def our_video_capture(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame_rgb, (width, height),
                                interpolation=cv2.INTER_LINEAR)
    img_for_detect = darknet.make_image(width, height, 3)
    darknet.copy_image_from_bytes(img_for_detect, frame_resized.tobytes())
    return img_for_detect

def ahmed_detector(frame):
    img_for_detect = our_video_capture(frame) # öncelikle yukarıdaki fonksiyonumuzu kullanarak darknete uygun bir img elde ediyoruz
    detection = darknet.detect_image(network, class_names,img_for_detect) # thresh=0.65, hier_thresh=0.5, nms=0.45 eklenebilir 
    retlist = []
    for isim, dogruluk,(x, y, w, h) in detection:
      retlist.append((isim, dogruluk,(int((x-w/2)*frame.shape[1]/416), int((y-h/2)*frame.shape[0]/416), int(w*frame.shape[1]/416), int(h*frame.shape[0]/416))))
    return retlist

KIRMIZI = (0, 0, 255)
YESIL = (0, 255, 0)
MAVI = (255, 0 , 0)
CYAN = (64, 64, 0)
MAGENTA = (128, 0, 128)
SIYAH = (0, 0, 0)
CIRTLAK_YESIL = (100,255,100)

def bbox_drawer(retlist, frame):
    for isim, _, (x, y, w, h) in retlist:
      renk = CIRTLAK_YESIL
      frame = cv2.putText(frame,dogruluk,(x+w,y+h),cv2.FONT_HERSHEY_SIMPLEX,1,renk,2)
      frame = cv2.putText(frame,isim,(x+w,y),cv2.FONT_HERSHEY_SIMPLEX,1,renk,2)
      frame = cv2.rectangle(frame, (x, y), (x+w, y+h), renk, 2)
    return frame     

OKUNACAK_VİDEO = '/home/oem/Desktop/gat/asaid/yolo/parkur1.mp4'

cap = cv2.VideoCapture(f"{OKUNACAK_VİDEO}")
while True:
    ret, frame = cap.read()  # Bir kareyi yakala
    if not ret:
        break  # Videonun sonuna geldiyseniz döngüyü kir

    retlist = ahmed_detector(frame)
    cv2.imshow('output', bbox_drawer(retlist, frame))  # İşlenmiş kareyi göster

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        break  # 'q' tuşuna basarak döngüyü sonlandır

cv2.destroyAllWindows()        


