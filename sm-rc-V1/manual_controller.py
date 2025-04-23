# This script is an interface for a wireless controller (e.g., PS4 controller) using the pyPS4Controller library.
# It defines a class RobotController that handles various button presses and joystick movements.
# The script also includes functions to connect and disconnect from the controller, as well as a global input structure to store the state of various inputs.
from pyPS4Controller.controller import Controller

input_struct = {
    "recording": 0,
    "playback" : 0,
    "jump": 0, #1 for active
    "crouch" : 0, #1 for active
    "freelook" : 0, #1 for active
    "movement" : [0.0,0.0], #x,y
    "rotation" : [0.0,0.0] #x,y
}

def connect():
    # any code you want to run during initial connection with the controller
    pass

def disconnect():
    input_struct = {
        "jump": 0, #1 for active
        "crouch" : 0, #1 for active
        "freelook" : 0, #1 for active
        "movement" : [0.0,0.0], #x,y
        "rotation" : [0.0,0.0] #x,y
    }
    # any code you want to run during loss of connection with the controller or keyboard interrupt
    pass


class RobotController(Controller):
    
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        print("jump start")
        input_struct['jump'] = 1

    def on_x_release(self):
        print("jump end")
        input_struct['jump'] = 0
        
    def on_triangle_press(self):
        pass

    def on_triangle_release(self):
        pass

    def on_circle_press(self):
        input_struct['crouch'] = 1
        pass

    def on_circle_release(self):
        input_struct['crouch'] = 0
        pass

    def on_square_press(self):
        pass

    def on_square_release(self):
        pass

    def on_L1_press(self):
        if (input_struct['recording'] == 1):
            input_struct['recording'] = 0
        else:
            input_struct['recording'] = 1
        pass

    def on_L1_release(self):
        pass

    def on_L2_press(self, value):
        calced = abs((value + 32768)  / (32768+32768))
        input_struct['rotation'][1] = -calced
        #print(calced)

    def on_L2_release(self):
        #input_struct['rotation'][1] = 0
        pass

    def on_R1_press(self):
        if (input_struct['playback'] == 1):
            input_struct['playback'] = 0
        else:
            input_struct['playback'] = 1
        pass

    def on_R1_release(self):
        pass

    def on_R2_press(self, value):
        calced = abs((value + 32768)  / (32768+32768))
        input_struct['rotation'][1] = calced
        #print("on_R2_press: {}".format(value))

    def on_R2_release(self):
        #input_struct['rotation'][1] = 0
        pass

    def on_up_arrow_press(self):
        pass

    def on_up_down_arrow_release(self):
        pass

    def on_down_arrow_press(self):
        pass

    def on_left_arrow_press(self):
        pass

    def on_left_right_arrow_release(self):
        pass

    def on_right_arrow_press(self):
        pass

    def on_L3_up(self, value):
        #print("on_L3_up: {}".format(value/32768))
        input_struct['movement'] = [input_struct['movement'][0],value/32768]

    def on_L3_down(self, value):
        #print("on_L3_down: {}".format(value/32768))
        input_struct['movement'] = [input_struct['movement'][0],value/32768]


    def on_L3_left(self, value):
        #print("on_L3_left: {}".format(value/32768))
        input_struct['movement'] = [value/32768,input_struct['movement'][1]]

    def on_L3_right(self, value):
        #print("on_L3_right: {}".format(value/32768))
        input_struct['movement'] = [value/32768,input_struct['movement'][1]]

    def on_L3_y_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        input_struct['movement'] = [input_struct['movement'][0],0.0]

    def on_L3_x_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        input_struct['movement'] = [0.0,input_struct['movement'][1]]

    def on_L3_press(self):
        """L3 joystick is clicked. This event is only detected when connecting without ds4drv"""
        pass

    def on_L3_release(self):
        """L3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
        pass

    def on_R3_up(self, value):
        print("on_R3_up: {}".format(value/32768))

    def on_R3_down(self, value):
        print("on_R3_down: {}".format(value/32768))

    def on_R3_left(self, value):
        print("on_R3_left: {}".format(value/32768))

    def on_R3_right(self, value):
        print("on_R3_right: {}".format(value/32768))

    def on_R3_y_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        pass

    def on_R3_x_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        pass
    def on_R3_press(self):
        """R3 joystick is clicked. This event is only detected when connecting without ds4drv"""
        pass
    def on_R3_release(self):
        """R3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
        pass
    def on_options_press(self):
        pass
    def on_options_release(self):
        pass
    def on_share_press(self):
        """this event is only detected when connecting without ds4drv"""
        pass
    def on_share_release(self):
        """this event is only detected when connecting without ds4drv"""
        pass
    def on_playstation_button_press(self):
        """this event is only detected when connecting without ds4drv"""
        pass
    def on_playstation_button_release(self):
        """this event is only detected when connecting without ds4drv"""
        pass

controller = RobotController(interface="/dev/input/js0", connecting_using_ds4drv=False)

def start_control():
    # you can start listening before controller is paired, as long as you pair it within the timeout window
    controller.listen(timeout=99999,on_connect=connect, on_disconnect=disconnect)