import Pi20 #Pi20 kütüphanesini içeri aktar.

motorlar = Pi20.MotorKontrol() #Motorkontrol ü motorlar diye tanıttık.

joystik = Pi20.Kumanda() #Kumanda yı joystik diye tanıt.
joystik.dinlemeyeBasla() #Joystik i dinlemeye başlat.

while True:
    lx, ly = joystik.solVerileriOku() #joystik sol verileri oku.
    sagHiz, solHiz, = motorlar.kumandaVerisiniMotorVerilerineCevirme(lx, ly) #Kumanda verisini motor verilerine çevir.

    motorlar.hizlariAyarla(sagHiz, solHiz) #Motorların hızlarını ayarladık yaptığımız harekete göre.
