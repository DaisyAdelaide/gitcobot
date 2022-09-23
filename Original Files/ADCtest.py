from gpiozero import PWMLED,MCP3208
from time import sleep


red = PWMLED(4)
pot1 = MCP3208(channel = 2)

values = []
x = []
index = 0

while True:    
    
    red.value = pot1.value



 
    
