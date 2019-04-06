# Forklift code!
left_motor = "56702378516105538047867"
right_motor = "56702629055943970764316"
lift_motor = "56695734118150397621956"

rmc = -0.5
lmc = 0.5

async def go_forward(time):

    # move left motor forward 

    Robot.set_value(left_motor, 'duty_cycle', .5)

    # move right motor forward

    Robot.set_value(right_motor,'duty_cycle', .5)

    # wait for x (time) number of seconds

    await Actions.sleep(time)

    # tell left motor to stop

    Robot.set_value(left_motor,'duty_cycle', 0)

    # tell right motor to stop 

    Robot.set_value(right_motor,'duty_cycle', 0)

async def go_backward(time):
    
    #move left motor backward
    
    Robot.set_value(left_motor, 'duty_cycle', -.5)
    
    #move right motor backward
    
    Robot.set_value(right_motor, 'duty_cycle', -.5)
    
    #wait for x (time) number of seconds
    
    await Actions.sleep(time)
    
    #tell left motor to stop
    
    Robot.set_value(left_motor, 'duty_cycle', 0)
    
    #tell right motor to stop
    
    Robot.set_value(right_motor, 'duty_cycle', 0)
    #---TURN ANGLE---

async def turn_angle(angle):
    time= angle / 2
    
    #move left motor forward
    
    Robot.set_value(left_motor, 'duty_cycle', .5)
    
    #move right motor reverse
    
    Robot.set_value(right_motor, 'duty_cycle', -.5)
    
    #wait for x (time) number of seconds
    
    await Actions.sleep(time)
    
    #tell left motor to stop
    
    Robot.set_value(left_motor, 'duty_cycle', 0)
    
    #tell right motor to stop
    
    Robot.set_value(right_motor, 'duty_cycle', 0)

async def robot_drive_direct(vleft, vright):
    Robot.set_value(left_motor, 'duty_cycle', lmc * vleft)    
    Robot.set_value(right_motor, 'duty_cycle', rmc * vright)

async def activate_lift(vlift, time):
    Robot.set_value(lift_motor, 'duty_cycle', -vlift)
    await Actions.sleep(time)
    Robot.set_value(lift_motor, 'duty_cycle', 0)

def autonomous_setup():
    Robot.run(activate_lift, -0.4, 4.0)

def autonomous_main():
    pass

def teleop_setup():
    pass

def teleop_main():
    # --- FORKLIFT CONTROLS ---
    
    # If A is being pressed:
    if Gamepad.get_value("button_a"):
        Robot.set_value(lift_motor, "duty_cycle", 1)
        # Move forklift motor with positive pulse value
    # Otherwise:
    else:
        # Stop the forklift
        Robot.set_value(lift_motor, "duty_cycle", 0)
    
    # --- DRIVE CONTROLS --- 
    # If left joystick has moved:
    if Gamepad.get_value("joystick_left_y") != 0.0:
        print("Moving joystick")
        # Drive left motor proportional to left joystick
        Robot.set_value(left_motor, "duty_cycle", Gamepad.get_value("joystick_left_y"))
    # Otherwise
    else:
        # Stop left motor
        Robot.set_value(left_motor, "duty_cycle", 0)
     # If right joystick has moved:
    if Gamepad.get_value("joystick_right_y") != 0.0:

        print("Moving joystick")
        #Drive right motor proportional to right joystick
        Robot.set_value(right_motor, "duty_cycle", Gamepad.get_value("joystick_right_y"))
    #Otherwise
    else:
        #stop right motor
        Robot.set_value(right_motor, "duty_cycle", 0)

    
