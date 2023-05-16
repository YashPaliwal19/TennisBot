import rotate_move
from end_eff_servo_control import control_two_servo
import time

def post_process_command(command):
    if command=="NoBall":
        # Rotate 45 degree
        rotate_move.rotate_45()
        
    elif command=="Grab":
        # do grab using 2 servo
        control_two_servo()
        time.sleep(6)
        print("I grab the ball")
        rotate_move.backward_comm()
        exit()
        
    elif command=="mForward":
        # move more forward
        rotate_move.more_forward()
        
    elif command=="lForward":
        # Move less forward
        rotate_move.less_forward()
        
    elif command=="Left":
        # Rotate left 10 degree
        rotate_move.rotate_10_left()
        
    elif command=="Right":
        # Rotate right 10 degree
        rotate_move.rotate_10_right()
        
    else:
        print(f"Invalid message: {command}")