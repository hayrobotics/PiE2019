left_motor = "56692776393860847950432"
right_motor = "56701913640562953935644"
center_motor = ""

# Motor constants - all velocity values multiplied by these numbers.
# Changing these variables changes speed everywhere in the code. 
lmc = -1 # Left motor constant
rmc = 1 # Right motor constant
cmc = 1 # Center motor constant

async def go_backward(time):
    #move left motor backward
    Robot.set_value(left_motor, 'duty_cycle', -lmc)
    #move right motor backward
    Robot.set_value(right_motor, 'duty_cycle', -rmc)
    #wait for x (time) number of seconds
    await Actions.sleep(time)
    #tell left motor to stop
    Robot.set_value(left_motor, 'duty_cycle', 0)
    #tell right motor to stop
    Robot.set_value(right_motor, 'duty_cycle', 0)

async def go_forward(time):
    # move left motor forward 
    Robot.set_value(left_motor, 'duty_cycle', lmc)
    # move right motor forward
    Robot.set_value(right_motor,'duty_cycle', rmc)
    # wait for x (time) number of seconds
    await Actions.sleep(time)
    # tell left motor to stop
    Robot.set_value(left_motor,'duty_cycle', 0)
    # tell right motor to stop 
    Robot.set_value(right_motor,'duty_cycle', 0)

async def translate_left(time):
    Robot.set_value(center_motor, 'duty_cycle', cmc)
    await Actions.sleep(time)
    Robot.set_value(center_motor, 'duty_cycle', 0)
    
async def translate_right(time):
    Robot.set_value(center_motor, 'duty_cycle', -cmc)
    await Actions.sleep(time)
    Robot.set_value(center_motor, 'duty_cycle', 0)

async def turn_angle(time):
    #move left motor forward
    Robot.set_value(left_motor, 'duty_cycle', lmc)
    #move right motor reverse
    Robot.set_value(right_motor, 'duty_cycle', -rmc)
    #wait for x (time) number of seconds
    await Actions.sleep(time)
    #tell left motor to stop
    Robot.set_value(left_motor, 'duty_cycle', 0)
    #tell right motor to stop
    Robot.set_value(right_motor, 'duty_cycle', 0)

def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(go_forward, 7)

def autonomous_main():
    pass

def teleop_setup():
    print("Tele-operated mode has started!")

'''
# Experimentation with Controller Function. Revert if not functional.
async def controller_function():
    if Gamepad.get_value("joystick_left_y") != 0.0:
        print("Moving joystick")
        Robot.set_value(left_motor, "duty_cycle", Gamepad.get_value("joystick_left_y"))
    else:
        Robot.set_value(left_motor, "duty_cycle", 0)

    if Gamepad.get_value("joystick_right_y") != 0.0:
        print("Moving joystick")
        Robot.set_value(right_motor, "duty_cycle", Gamepad.get_value("joystick_right_y"))
    else:
        Robot.set_value(right_motor, "duty_cycle", 0)

'''

def teleop_main():
    if Gamepad.get_value("joystick_left_y") != 0.0:
        Robot.set_value(left_motor, "duty_cycle", lmc * Gamepad.get_value("joystick_left_y"))
        Robot.set_value(right_motor, "duty_cycle", rmc * Gamepad.get_value("joystick_left_y"))
    else:
        Robot.set_value(left_motor, "duty_cycle", 0)
        Robot.set_value(right_motor, "duty_cycle", 0)
    
    if Gamepad.get_value("joystick_left_x") != 0.0:
        Robot.set_value(center_motor, "duty_cycle", cmc * Gamepad.get_value("joystick_left_x"))
    else:
        Robot.set_value(center_motor, "duty_cycle", 0)
    
    if Gamepad.get_value("joystick_right_x") > 0:
        Robot.set_value(left_motor, "duty_cycle", lmc * Gamepad.get_value("joystick_right_x"))
        Robot.set_value(right_motor, "duty_cycle", -rmc * Gamepad.get_value("joystick_right_x"))
    elif Gamepad.get_value("joystick_right_x") < 0:
        Robot.set_value(left_motor, "duty_cycle", -lmc * Gamepad.get_value("joystick_right_x"))
        Robot.set_value(right_motor, "duty_cycle", rmc * Gamepad.get_value("joystick_right_x"))
    else:
        Robot.set_value(left_motor, "duty_cycle", 0)
        Robot.set_value(right_motor, "duty_cycle", 0)
