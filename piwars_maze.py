import Pi20 #Pi20 kütüphanesini içeri aktardık.
from time import sleep #Time kütüphanesi içerisindeki sleep i içeri aktar.

motorlar = Pi20.MotorKontrol() #Motorkontrol ü motorlar diye tanıttık.
ultra = Pi20.UltrasonikSensor(16, 13) #Sensörlerin Echo ve Trig lerini yazdık.
ultra2 = Pi20.UltrasonikSensor(18, 15) #Sensörlerin Echo ve Trig lerini yazdık.
ultra3 = Pi20.UltrasonikSensor(12, 11) #Sensörlerin Echo ve Trig lerini yazdık.

ultra.mesafeOlcmeyeBasla() #Ultra diye adlandırmış olduğumuz sensörümüzün ölçüme başlamasını sağladık.
ultra2.mesafeOlcmeyeBasla() #Ultra2 diye adlandırmış olduğumuz sensörümüzün ölçüme başlamasını sağladık.
ultra3.mesafeOlcmeyeBasla() #Ultra3 diye adlandırmış olduğumuz sensörümüzün ölçüme başlamasını sağladık.
motorlar.hizlariAyarla(0, 0) #Motorların hızını 0 a almış olduk.

speed1 = 175 #Her satır kodda motor hızını değiştirmek yerine buraya kısaltma eklemiş olduk.
speed2 = -235 #Her satır kodda motor hızını değiştirmek yerine buraya kısaltma eklemiş olduk.
while True:
    anlikDeger = ultra.mesafeOku() #Ultra diye adlandırmış olduğumuz sensörümüzün mesafe okuma kodlarını anlikDeger adlı değişkende tanımladık.
    anlikDeger2 = ultra2.mesafeOku() #Ultra diye adlandırmış olduğumuz sensörümüzün mesafe okuma kodlarını anlikDeger2 adlı değişkende tanımladık.
    anlikDeger3 = ultra3.mesafeOku() #Ultra diye adlandırmış olduğumuz sensörümüzün mesafe okuma kodlarını anlikDeger3 adlı değişkende tanımladık.
    
    if (anlikDeger >= 5): #Anlık Değer 5'e eşit yada küçük ise:
        sleep(0.2) #0.2 sn uyut
        motorlar.hizlariAyarla(speed1, speed1) #Motorların hızlarını speed1 (175) yap.
        sleep(0.2) #0.2 sn uyut
        print("orta-sensor =", anlikDeger) #Orta sensörümüzün okuduğu anlık değeri yaz.
        sleep(0.1) #0.1 sn uyut
        
    elif (anlikDeger < 5) and (anlikDeger2 < anlikDeger3): #Anlık değer 5'ten küçük ve anlıkdeğer2 anlıkdeğer3 ten küçük ise:
        print("sol-sensor =", anlikDeger2) #Sol sensörümüzün okuduğu anlık değeri yaz.
        print("orta-sensor =", anlikDeger) #Orta sensörümüzün okuduğu anlık değeri yaz.
        print("sag-sensor =", anlikDeger3) #Sağ sensörümüzün okuduğu anlık değeri yaz.
        print("____________________________") #Ölçümleri ayırmak için alt çizgi yazdırdık.
        sleep(0.2) #0.2 sn uyut
        motorlar.hizlariAyarla(-80, -80) #Motor hızlarını -80 e ayarlayarak geri gitme hareketini yap.
        sleep(0.6) #0.6 sn uyut
        motorlar.hizlariAyarla(speed1, -speed1) #Motorların hızlarını speed1 (175) ve -speed1 (-175) yap.
        sleep(0.65) #0.65 sn uyut
        
    elif (anlikDeger < 5) and (anlikDeger2 > anlikDeger3): #Anlıkdeğer 5'ten küçük ve anlıkdeğer2 anlıkdeğer3 ten büyük ise:
        print("sol-sensor =", anlikDeger2) #Sol sensörümüzün okuduğu anlık değeri yaz.
        print("orta-sensor =", anlikDeger) #Orta sensörümüzün okuduğu anlık değeri yaz.
        print("sag-sensor =", anlikDeger3) #Sağ sensörümüzün okuduğu anlık değeri yaz.
        print("____________________________") #Ölçümleri ayırmak için alt çizgi yazdırdık.
        sleep(0.2) #0.2 sn uyut
        motorlar.hizlariAyarla(-80, -80) #Motor hızlarını -80 e ayarlayarak geri gitme hareketini yap.
        sleep(0.6) #0.6 sn uyut
        motorlar.hizlariAyarla(-speed1, speed1) #Motorların hızlarını -speed1 (-175) ve speed1 (175) yap.
        sleep(0.65) #0.65 sn uyut
        
    
        
        
    else:
        motorlar.hizlariAyarla(speed1, speed1) #Motorların hızlarını speed1 (175) yap.
        print(anlikDeger) #Orta sensörümüzün okuduğu anlık değeri yaz.
    

