from machine import Pin
from gpio_lcd import GpioLcd 

lcd=GpioLcd(rs_pin=Pin (16),
            enable_pin=Pin (17),
            d4_pin=Pin (18),
            d5_pin=Pin (19),
            d6_pin=Pin (20),
            d7_pin=Pin (21),
            num_lines=2,
            num_columns=16)
            

lcd.putstr('Sahil')


