import Adafruit_PCA9685 # Import the library used to communicate with PCA9685
from adafruit_servokit import ServoKit
import time

def control_two_servo():
    kit = ServoKit(channels=8)
    
    # Make the servo connected to the No. 3 servo port on the Motor HAT drive board reciprocate
    #3 is for left
    # 65 initial angle
    # 170 final angl0
    kit.servo[3].angle = 175
    #time.sleep(2)
    #pwm = Adafruit_PCA9685.PCA9685() # Instantiate the object used to control the PWM
    #pwm.set_pwm_freq(1) # Set the frequency of the PWM signal
    #time.sleep(5)
    #kit.servo[3].angle = 40
    #pwm.set_pwm(3, 300, 500)
    #7 for the right
    #pwm.set_pwm(7, 0, angle)
    #kit.servo[7].angle = 180
    pass

        
if __name__=="__main__":
    control_two_servo()
    