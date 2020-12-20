from microbit import *
import time
import random
        
def eteindre ():
    pin0.write_digital(0)
    pin1.write_digital(0)
    pin2.write_digital(0)
    pin3.write_digital(0)
    pin4.write_digital(0)
    pin5.write_digital(0)
    pin6.write_digital(0)
    pin7.write_digital(0)
    pin8.write_digital(0)
    pin9.write_digital(0)
    pin10.write_digital(0)
    pin11.write_digital(0)
    
while True:
    liste = []
    # Side A
    liste.append(random.randint(0,2))
    # Side B
    liste.append(random.randint(3,5))
    # Side C
    liste.append(random.randint(6,8))
    # Side D
    liste.append(random.randint(9,11))
    for i in range(4):
        if liste [i] == 0 :
                pin0.write_digital(1)
        if liste [i] == 1 :
                pin1.write_digital(1)
        if liste [i] == 2 :
                pin2.write_digital(1)
        if liste [i] == 3 :
                pin3.write_digital(1)
        if liste [i] == 4 :
                pin4.write_digital(1)
        if liste [i] == 5 :
                pin5.write_digital(1)
        if liste [i] == 6 :
                pin6.write_digital(1)
        if liste [i] == 7 :
                pin7.write_digital(1)
        if liste [i] == 8 :
                pin8.write_digital(1)
        if liste [i] == 9 :
                pin9.write_digital(1)
        if liste [i] == 10 :
                pin10.write_digital(1)
        if liste [i] == 11 :
                pin11.write_digital(1)
    sleep (1000)
    eteindre ()
    sleep (1000)