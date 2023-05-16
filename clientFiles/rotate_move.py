#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

# motor_EN_A: Pin7  |  motor_EN_B: Pin11
# motor_A:  Pin8,Pin10    |  motor_B: Pin13,Pin12

Motor_A_EN    = 4
Motor_B_EN    = 17

Motor_A_Pin1  = 26
Motor_A_Pin2  = 21
Motor_B_Pin1  = 27
Motor_B_Pin2  = 18

def setup():#Motor initialization
	global pwm_A, pwm_B
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Motor_A_EN, GPIO.OUT)
	GPIO.setup(Motor_B_EN, GPIO.OUT)
	GPIO.setup(Motor_A_Pin1, GPIO.OUT)
	GPIO.setup(Motor_A_Pin2, GPIO.OUT)
	GPIO.setup(Motor_B_Pin1, GPIO.OUT)
	GPIO.setup(Motor_B_Pin2, GPIO.OUT)

	motorStop()
	try:
		pwm_A = GPIO.PWM(Motor_A_EN, 1000)
		pwm_B = GPIO.PWM(Motor_B_EN, 1000)
	except:
		pass

def motorStop():#Motor stops
	GPIO.output(Motor_A_Pin1, GPIO.LOW)
	GPIO.output(Motor_A_Pin2, GPIO.LOW)
	GPIO.output(Motor_B_Pin1, GPIO.LOW)
	GPIO.output(Motor_B_Pin2, GPIO.LOW)
	GPIO.output(Motor_A_EN, GPIO.LOW)
	GPIO.output(Motor_B_EN, GPIO.LOW)
	
def destroy():
	motorStop()
	GPIO.cleanup()
	
def rotate_45():
    # rotate right
    timer = 0.15
    speed = 100
    rotate_right(speed, timer)
    

def rotate_10_left():
    timer = 0.08
    speed = 100
    rotate_left(speed, timer)

def rotate_10_right():
    timer = 0.08
    speed = 100
    rotate_right(speed, timer)

def more_forward():
    timer = 0.12
    speed = 100
    forward(speed, timer)
    
def less_forward():
    timer = 0.07
    speed = 100
    forward(speed, timer)
    
def backward_comm():
    timer = 1.15
    speed = 100
    backward(speed, timer)

def forward(speed, timer):
    # Move forward
    setup()
    GPIO.output(Motor_B_Pin1, GPIO.LOW)
    GPIO.output(Motor_B_Pin2, GPIO.HIGH)
    GPIO.output(Motor_A_Pin1, GPIO.LOW)
    GPIO.output(Motor_A_Pin2, GPIO.HIGH)
    pwm_A.start(speed)
    pwm_A.ChangeDutyCycle(speed)
    pwm_B.start(speed)
    pwm_B.ChangeDutyCycle(speed)
    
    time.sleep(timer)
    destroy()

def backward(speed, timer):
    # Move backward
    setup()
    GPIO.output(Motor_B_Pin1, GPIO.HIGH)
    GPIO.output(Motor_B_Pin2, GPIO.LOW)
    GPIO.output(Motor_A_Pin1, GPIO.HIGH)
    GPIO.output(Motor_A_Pin2, GPIO.LOW)
    pwm_A.start(speed)
    pwm_A.ChangeDutyCycle(speed)
    pwm_B.start(speed)
    pwm_B.ChangeDutyCycle(speed)
    
    time.sleep(timer)
    destroy()

def rotate_left(speed, timer):
    setup()
    GPIO.output(Motor_B_Pin1, GPIO.LOW)
    GPIO.output(Motor_B_Pin2, GPIO.HIGH)
    GPIO.output(Motor_A_Pin1, GPIO.HIGH)
    GPIO.output(Motor_A_Pin2, GPIO.LOW)
    pwm_A.start(speed)
    pwm_A.ChangeDutyCycle(speed)
    pwm_B.start(speed)
    pwm_B.ChangeDutyCycle(speed)
    time.sleep(timer)
    destroy()
    
def rotate_right(speed, timer):
    setup()
    GPIO.output(Motor_B_Pin1, GPIO.HIGH)
    GPIO.output(Motor_B_Pin2, GPIO.LOW)
    GPIO.output(Motor_A_Pin1, GPIO.LOW)
    GPIO.output(Motor_A_Pin2, GPIO.HIGH)
    pwm_A.start(speed)
    pwm_A.ChangeDutyCycle(speed)
    pwm_B.start(speed)
    pwm_B.ChangeDutyCycle(speed)
    time.sleep(timer)
    destroy()

if __name__=="__main__":
    setup()
    speed = 100
    timer = 1.0
    #time.sleep(timer)
    #forward(speed, timer)
    #backward(speed, timer)
    #rotate_left(speed, timer)
    #rotate_right(speed, timer)
    #more_forward()
    #ess_forward()
    #rotate_10_right()
    backward_comm()
    time.sleep(3)
    #rotate_10_left()
    #destroy()
    