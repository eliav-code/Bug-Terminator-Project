import RPi.GPIO as GPIO
import time
def move_motor_time(direction,mytime):



    LATCH = 21
    CLK = 20
    dataBit = 16
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LATCH, GPIO.OUT)
    GPIO.setup(CLK, GPIO.OUT)
    GPIO.setup(dataBit, GPIO.OUT)


    if direction == 'turnleft':
        for x in range(0, 8):
	
            if x==3 or x==7 or x==0 or x==5:

                GPIO.output(dataBit, 1) 
            else:
                GPIO.output(dataBit, 0)
            GPIO.output(CLK, 1)
            #time.sleep(0.1)
            GPIO.output(CLK, 0)

        GPIO.output(LATCH, 1)
        #time.sleep(0.1)
        GPIO.output(LATCH, 0)

    elif direction == 'turnright':
        for x in range(0, 8):
	
            if x==6 or x==1 or x==2 or x==4:
                GPIO.output(dataBit, 1) 
            else:
                GPIO.output(dataBit, 0)
            GPIO.output(CLK, 1)
            #time.sleep(0.1)
            GPIO.output(CLK, 0)

        GPIO.output(LATCH, 1)
        #time.sleep(0.1)
        GPIO.output(LATCH, 0)


    elif direction == 'forward':
        for x in range(0, 8):
	
            if x==3 or x==7 or x==2 or x==4:
                GPIO.output(dataBit, 1) 
            else:
                GPIO.output(dataBit, 0)
            GPIO.output(CLK, 1)
            #time.sleep(0.1)
            GPIO.output(CLK, 0)

        GPIO.output(LATCH, 1)
        #time.sleep(0.1)
        GPIO.output(LATCH, 0)
#if x==0 or x==1 or x==3 or x==4:


#x==5 or x==6 or x==7 or x==2 or x==4




    GPIO.setmode(GPIO.BCM)

    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.output(5, True)
    GPIO.output(6, True)
    GPIO.output(13, True)
    GPIO.output(19, True)
 
    time.sleep(mytime)

    GPIO.output(5, False)
    GPIO.output(6, False)
    GPIO.output(13, False)
    GPIO.output(19, False)

    time.sleep(4*mytime)
	
    GPIO.cleanup()