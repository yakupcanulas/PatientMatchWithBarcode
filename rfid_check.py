from pirc522 import RFID
import signal
import time
import RPi.GPIO as GPIO
import RPLCD

GPIO.setmode(GPIO.BOARD)

ledpinAcik = 7
ledpinKapali = 11

GPIO.setup(ledpinAcik, GPIO.OUT)
GPIO.setup(ledpinKapali, GPIO.OUT)

rdr = RFID()
util = rdr.util()
util.debug = True

 

while True:
    
    lcd = RPLCD.CharLCD(numbering_mode=GPIO.BOARD,cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40,36,38,15,33,31,29,32] )   
    
    rdr.wait_for_tag()
    (error, data) = rdr.request()
    #if not error:
    print("\nKart Algilandi!")
    (error, uid) = rdr.anticoll()
    #if not error:
    #Print UID
    kart_uid = str(uid[0])+" "+str(uid[1])+" "+str(uid[2])+" "+str(uid[3])+" "+str(uid[4])
    print(kart_uid)
    
    
    dosya = open('/home/pi/Desktop/rfid_text.txt')
    x= dosya.read()
    #bu sayıları okurken ve yazarken kripto ile yazıp göz ile okunur halden uzaklaştırmalıyız.
    
    if kart_uid == str(x) :
        #print("ÖRNEKLER EŞLEŞTİ!")
        GPIO.output(ledpinAcik, True)
        lcd.cursor_pos=(1,0)
        lcd.write_string('ORNEK ESLESDI')
        time.sleep(2)
        GPIO.output(ledpinAcik, False)
        
        
#     elif kart_uid == "41 212 221 162 130":
#         print("ÖRNEKLER EŞLEŞTİ!")
#         GPIO.output(ledpinAcik, True)
#         time.sleep(2)
#         GPIO.output(ledpinAcik, False)
        
    else: 
        #print("HATA! ÖRNEKLER EŞLEŞMEDİ!!")
        GPIO.output(ledpinKapali, True)
        lcd.cursor_pos=(1,0)
        lcd.write_string('ORNEK ESLESMEDI')
        time.sleep(2)
        GPIO.output(ledpinKapali, False)
        