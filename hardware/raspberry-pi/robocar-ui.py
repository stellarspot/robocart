from guizero import App, Text, TextBox, PushButton
from robocar import run_forward_motors, run_backward_motors, \
    rotate_motors_left, rotate_motors_right, \
    stop_motors, motors_cleanup
from time import sleep

app = App(title="Robocart Control panel", layout="grid")

ACTION_TIME = 2


def press_forward():
    run_forward_motors()
    sleep(ACTION_TIME)
    stop_motors()


def press_backward():
    run_backward_motors()
    sleep(ACTION_TIME)
    stop_motors()


def press_left():
    rotate_motors_left()
    sleep(ACTION_TIME)
    stop_motors()


def press_right():
    rotate_motors_right()
    sleep(ACTION_TIME)
    stop_motors()


button_left = PushButton(app, command=press_left, text="Left", grid=[0, 0])
button_forward = PushButton(app, command=press_forward, text="Forward", grid=[1, 0])
button_backward = PushButton(app, command=press_backward, text="Backward", grid=[2, 0])
button_right = PushButton(app, command=press_right, text="Right", grid=[3, 0])

app.display()
motors_cleanup()
