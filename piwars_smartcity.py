import numpy as np #napy kütüphanemizi çağırıyoruz
import cv2  #cv2 kütüphanemizi çağırıyoruz
import Pi20 #Pi20 kütüphanemizi çağırıyoruz

from time import sleep # time kütüphanesinden sleep'i çağırıyoruz


cap = cv2.VideoCapture(0) 

MIN_THRESHOLD = 100
MAX_THRESHOLD = 255

CENTER_MIN = 200 # Takip edilecek çizginin merkeze olan min. uzaklığı
CENTER_MAX = 300 # Takip edilecek çizginin merkeze olan max. uzaklığı

VELOCITY = 200 # Motor hız Değişkenimiz

motorlar = Pi20.MotorKontrol() #Motor kontrolü
last_direction = None


while(True):
    # Kare kare yakalama komutu
    ret, frame = cap.read()

    # Çerçeve üzerindeki operasyonlarımız buraya geliyor
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Görüntüyü gri renge çeviriyoruz
    blur = cv2.GaussianBlur(gray,(5,5),0) #Gri tonlamalı görüntüyü blurlaştırıyoruz. Amaç görüntüyü yumuşatmak
    
    _, thresh = cv2.threshold(blur,35,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # thershold'u kullanarak gürültüyü azaltıyoruz.
#    _, thresh = cv2.threshold(thresh,127,255,cv2.THRESH_BINARY_INV) # Görüntünün piksel rengini tersine çevirmiyoruz
    
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:

        c = max(contours, key=cv2.contourArea)  #kontürdeki en büyük pixel grubu
        M = cv2.moments(c)  #görüntü piksellerinin yoğunluklarının ağırlıklı ortalaması

        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        cv2.line(frame,(cx,0),(cx,720), (255,0,0), 2)  #ağırlıklı ortalamadan çıkartılan centroid koordinatları
        cv2.line(frame,(0,cy),(1280,cy), (255,0,0), 2) #ağırlıklı ortalamadan çıkartılan centroid koordinatları


        print("cx -> %s" %cx) #çizgi çek
        print("cy -> %s" %cy) #çizgi çek

        if cx <= CENTER_MIN: # İzleyeceğimiz çizgi ekranın sol tarafında ise robotumuza sola doğru gitme komutunu veriyoruz.
            print("direction -> left")
            motorlar.hizlariAyarla(-int(VELOCITY / 4), VELOCITY)
        
        elif cx > CENTER_MIN and cx < CENTER_MAX: # İzleyeceğimiz çizgi ekranın merkezindeyse robotumuza düz git komutunu veriyoruz.
            print("direction -> center")
            motorlar.hizlariAyarla(VELOCITY, VELOCITY)
        
        elif cx >= CENTER_MAX: # İzleyeceğimiz çizgi ekranın sağ tarafında ise robotumuza sağa doğru gitme komutunu veriyoruz.
            print("direction -> right")
            motorlar.hizlariAyarla(VELOCITY, -int(VELOCITY/4))
                
        else:
            motorlar.hizlariAyarla(0, 0) # Çizgiyi göremediğimizde robotu durduruyoruz.
            print("I don't see the line")
            
    else:
        motorlar.hizlariAyarla(0, 0) # Çizgiyi göremediğimizde robotu durduruyoruz.
        print("I don't see the line")

            
    # Görüntüyü ekranımızda gösteriyoruz
    cv2.imshow('frame', thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'): #q tuşuna bastığımızda motorları durdurup programdan çıkıyoruz
        motorlar.hizlariAyarla(0, 0)
        break



# Her şey bittiğinde, ekran yakalamasını serbest bırakıyoruz
cap.release()
cv2.destroyAllWindows()
