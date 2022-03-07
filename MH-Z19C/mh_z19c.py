from m5stack import *
from m5ui import *
from uiflow import *
from machine import UART
#import time

class MH_Z19C:

    def __init__(self,tx_pin,rx_pin):
        
        self.uart = None
        self.uart = UART(1, tx=tx_pin, rx=rx_pin)
        self.uart.init(9600, bits=8, parity=None, stop=1)
        
    def read_data(self):
        self.uart.write(b"\xff\x01\x86\x00\x00\x00\x00\x00\x79")
        wait_ms(1000)
        self.s=self.uart.read()
        return self.s

    def read_co2_conc(self):
        if self.s != None:
            return self.s[2]*256 + self.s[3]
    
        else:
            return None

    def read_temp(self):
        if self.s != None:
            return self.s[4] - 40
        else:
            return None