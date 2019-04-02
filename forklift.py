# Forklift code!
left_motor = ""
right_motor = ""
lift_motor = ""


def autonomous_setup():
    pass

def autonomous_main():
    pass

def teleop_setup():
    pass

def teleop_main():
    # If A is being pressed:
    if Gamepad.get_value("button_a"):
        Robot.set_value(lift_motor, "duty_cycle", 1)
        # Move lift motor with positive pulse value
    else:
        Robot.set_value(lift_motor, "duty_cycle", 0)
