import Pi20 #Pi20 kütüphanesini içeri aktardık.
from time import sleep #Time kütüphanesi içerisindeki sleep i içeri aktar.

motorlar = Pi20.MotorKontrol() #Motorkontrol ü motorlar diye tanıttık.
ultra = Pi20.UltrasonikSensor(16, 13) #Sensörlerin Echo ve Trig lerini yazdık.

ultra.mesafeOlcmeyeBasla() #Ultra diye adlandırmış olduğumuz sensörümüzün ölçüme başlamasını sağladık.

motorlar.hizlariAyarla(0, 0) #Motorların hızını 0 a almış olduk.
sayac = 0 #Sayaç ile ultrasonikten gelen hataları eledik.
while sayac<8: #Sayaç 8'den küçük ise:
    sleep(0.01) #0.01 sn uyut.
    print(sayac) #Sayaç değerini yaz
    anlikDeger = ultra.mesafeOku() #Ultra diye adlandırmış olduğumuz sensörümüzün mesafe okuma kodlarını anlikDeger adlı değişkende tanımladık.
    
    if (anlikDeger <=8): #Anlıkdeğer 8'e eşit veya küçük ise:
        print(anlikDeger) #Anlık değeri yaz.
        sayac = sayac+1 #Sayaca +1 ekle

    elif (anlikDeger <=15): #Anlıkdeğer 8'e eşit veya küçük ise:
        sleep(0.2) #0.2 sn uyut.
        motorlar.hizlariAyarla(80, 80) #Motor hızlarını 80 e ayarlayarak ileri gitme hareketini yap.
        print(anlikDeger) #Anlık değeri yaz.
        
    elif (anlikDeger <=30): #Anlıkdeğer 30'a eşit veya küçük ise:
        sleep(0.2) #0.2 sn uyut.
        motorlar.hizlariAyarla(130, 130) #Motor hızlarını 130 e ayarlayarak ileri gitme hareketini yap.
        print(anlikDeger) #Anlık değeri yaz.
        
    else:
        motorlar.hizlariAyarla(130, 130) #Motor hızlarını 130 e ayarlayarak ileri gitme hareketini yap.
        print(anlikDeger) #Anlık değeri yaz.

motorlar.hizlariAyarla(0, 0) #Motorların hızını 0 a almış olduk.
sleep(5) #5 sn uyut.