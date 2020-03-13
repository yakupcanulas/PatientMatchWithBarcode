from time import sleep 

from RPi import GPIO

import RPLCD  

GPIO.setmode(GPIO.BOARD) 

lcd = RPLCD.CharLCD(numbering_mode=GPIO.BOARD,cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40,36,38,15,33,31,29,32] )   

lcd.cursor_pos=(1,0)  # cursor_pos fonksiyonu ile yazmaya alt satırdan başlayacaktır

lcd.write_string('ESLESTİ') 

sleep(5)  

lcd.clear()

GPIO.cleanup()




