import random
import RPi.GPIO as GPIO
import time
from motors_new import *


#-----------------------------------------------------------------------------------------------------------------------
#def move_motor_time(x,y,time): # gets gpio pins of two motors and turns them on for time seconds
                               # motor pins front right-19 front left-13 back left-5 back right-6
                               #front motors move forward. back motors move back.
   # GPIO.setmode(GPIO.BCM)

    #GPIO.setup(x, GPIO.OUT)
    #GPIO.setup(y, GPIO.OUT)

    #GPIO.output(x, True)
    #GPIO.output(y, True)

    #time.sleep(time)

    #GPIO.output(x, False)
    #GPIO.output(y, False)

    #GPIO.cleanup()
#------------------------------------------------------------------------------------------------------------------------------
def distance():

    #GPIO Mode (BOARD / BCM)
    GPIO.setmode(GPIO.BCM)

    #set GPIO Pins
    GPIO_TRIGGER = 26
    GPIO_ECHO = 23

    #set GPIO direction (IN / OUT)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    GPIO.cleanup()
    return distance
#---------------------------------------------------------------------------------------------------------------------
class Drive:
    def __init__(self):
        self.cmd="STOP"
        #self.frontright19 = 0 #neria
        #self.frontleft13 = 0 #neria
        #self.backleft5 = 0 #neria
        #self.backright6 = 0 #neria
#-----------------------------------------------------------------------------------------------------------------------
    def move_forward(self,mytime):
        print("I'm in regular move")
        temp=0
        while temp<mytime/2:
  
            move_motor_time('forward',0.004)
            temp+=0.004

    
        #pulse turn on for 0.5 second
        

            #print( "forward") 		#for debugging
    def set_turnleft(self, mytime):
        self.cmd="RO_L"
    def set_turnright(self, mytime):
        self.cmd="RO_R"
    def set_move_forward(self, mytime):
        self.cmd="M_F"
    def set_squirt(self):
        self.cmd="Trigger"
    def set_movement(self):
        self.cmd="R_M"


    def turnleft(self,mytime):
 #        print('helloleft')
   	 #pulse turn on for 0.5 second
         temp=0.0
         while temp<mytime/2:
  
             move_motor_time('turnleft',0.004)
             temp+=0.004
         #self.frontleft13 = 1 #neria
         #self.backright6 = -1 #neria

          #print( "left") #for debugging
 


    def turnright(self,mytime):

        print(self.cmd)#pulse turn on for 0.5 second
        temp=0.0
        while temp<mytime/2:
  
            move_motor_time('turnright',0.004)
            temp+=0.004

        #self.backleft5 = -1 #neria
        #self.frontright19 = 1 #neria
        #print( "left") #for debugging

    def squirt(self):
        print("h")
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(17, GPIO.OUT)# shoot
        GPIO.setup(12, GPIO.OUT) #beep

        GPIO.output(17, True)
        GPIO.output(12, True)

        time.sleep(0.5)

        GPIO.output(17, False)
        GPIO.output(12, False)
 
        
        time.sleep(1)
        
        GPIO.cleanup()
        self.set_movement()




    def movement(self):
       



        mytime = 0.009
        self.move_forward(mytime)   #move forward for 0.04 sec
        distance1=distance()	#check distance with ultrosonnic
        print(distance1)
        stuck_condition= distance1< 20.0
        if stuck_condition:
                 #print("I'm stuck")
            temp = random.randint(10, 20)
            mytime = 20.0/temp



            if(random.randint(1, 2)) == 1:

                self.turnright(mytime)

            else:

                self.turnleft(mytime)

               # if(condition): #optinal condition for stoping while

               #    break
        




    def handle_motors(self):
        rt=0.02
        while(True):  
            ccmd = self.cmd
            #print(ccmd)
            if ccmd == "RO_L":
                print("left")
                self.turnleft(rt)
            elif ccmd == "RO_R":
                print("right")
                self.turnright(rt)
            elif ccmd == "M_F":
                self.move_forward(rt)
            elif ccmd=="Trigger":
                self.squirt()  
            elif ccmd == "R_M":	
                self.movement()	
            elif ccmd=="STOP":
                time.sleep(0.2)
            else:
                exit(0)


