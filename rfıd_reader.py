from pirc522 import RFID
import signal
import time


x=str(input("Ad:"))
y=str(input("Soyad:"))
z=str(input("T.C. :"))

print("Kartinizi Okutunuz!")
    
time.sleep(5)
    
rdr = RFID()
util = rdr.util()
util.debug = True
# print("Kart bekleniyor...")
rdr.wait_for_tag()
(error, data) = rdr.request()
    
    
    
(error, uid) = rdr.anticoll()
#if not error:
kart_uid = str(uid[0])+" "+str(uid[1])+" "+str(uid[2])+" "+str(uid[3])+" "+str(uid[4])
print(kart_uid)
    
dosya = open('/home/pi/Desktop/rfid_text.txt', "w")
# dosya.write(x)
# dosya.write(y)
# dosya.write(z)
dosya.write(kart_uid)
dosya.close()

print("başarılı")