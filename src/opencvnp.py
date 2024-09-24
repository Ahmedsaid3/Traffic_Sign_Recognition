import glob
import numpy as np
import cv2
import darknet
import matplotlib.pyplot as plt
network, class_names, colors = darknet.load_network("/mydrive/yolo/yolov4-obj.cfg","/mydrive/yolo/obj_copy.data","/mydrive/yolo/backup/yolov4-obj_last.weights")
width = darknet.network_width(network)
height = darknet.network_height(network)

def opencv_demo(frame):
  image = cv2.imread(frame) # Görüntüyü OpenCV ile okuyoruz
  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # opencv bgr formatinda aliyor goruntuyu, biz bunu rgb formatina ceviriyoruz, bunu yapmadan once dogruluk 70'lerdeydi
  resized_image = cv2.resize(image_rgb, (width, height),interpolation=cv2.INTER_LINEAR) # Görüntüyü Darknet için belirtilen boyutlara yeniden boyutlandırıyoruz
  darknet_image = darknet.make_image(width, height, 3) # Darknet için uygun bir görüntü formatına dönüştüruyoruz
  darknet.copy_image_from_bytes(darknet_image, resized_image.tobytes())
  return darknet_image

def main(general_path="/mydrive/yolo/"): # main fonksiyonu main() ya da main(path) seklinde kullanilir
    aranan_tabelalar = ["sagadonulmez",
                        "soladonulmez",
                        "sagmecburi",
                        "solmecburi",
                        "ilerisag",
                        "ilerisol"
                        ]
    array = np.zeros((7, 6))
    for test_edilen_tabela in aranan_tabelalar:
        jpg_dosyalari = glob.glob(general_path + test_edilen_tabela + "/*.jpg")
        for jpg_path in jpg_dosyalari:
            darknet_image = opencv_demo(jpg_path)
            detection = darknet.detect_image(network, class_names, darknet_image, thresh=0.65, hier_thresh=0.5, nms=0.45)
            counter = 0
            for isim, _, _ in detection:
                if isim in aranan_tabelalar:
                    counter += 1
                    if isim == test_edilen_tabela:
                        array[aranan_tabelalar.index(test_edilen_tabela), aranan_tabelalar.index(test_edilen_tabela)] += 1
                    else:
                        array[aranan_tabelalar.index(isim), aranan_tabelalar.index(test_edilen_tabela), ] += 1
                else:
                    pass
            if counter == 0:
              array[6,aranan_tabelalar.index(test_edilen_tabela)] += 1
    return array


cap = cv2.VideoCapture('/Users/ahmedsaidgulsen/Desktop/Robotaxi/videos/parkur1.mp4')
while True:
    ret, frame = cap.read()  # Bir kareyi yakala
    if not ret:
        break  # Videonun sonuna geldiyseniz döngüyü kir

    # İşleme adimlarini burada yapabilirsiniz

    cv2.imshow('Video', frame)  # İşlenmiş kareyi göster

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # 'q' tuşuna basarak döngüyü sonlandir

