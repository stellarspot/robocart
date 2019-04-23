# Run DC Motors with L293D

import RPi.GPIO as GPIO
from time import sleep

enable_a = 7
motor_a1 = 3
motor_a2 = 5

enable_b = 11
motor_b1 = 13
motor_b2 = 15


def setup():
    GPIO.setmode(GPIO.BOARD)
    setup_pins(enable_a, motor_a1, motor_a2)
    setup_pins(enable_b, motor_b1, motor_b2)


def setup_pins(enable, in1, in2):
    GPIO.setup(enable, GPIO.OUT)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)


setup()

pwm_a = GPIO.PWM(enable_a, 100)
pwm_b = GPIO.PWM(enable_b, 100)
pwm_a.start(0)
pwm_b.start(0)


def run_forward(enable, in1, in2, pwm):
    GPIO.output(in1, True)
    GPIO.output(in2, False)
    pwm.ChangeDutyCycle(95)
    GPIO.output(enable, True)


def run_backward(enable, in1, in2, pwm):
    GPIO.output(in1, False)
    GPIO.output(in2, True)
    pwm.ChangeDutyCycle(95)
    GPIO.output(enable, True)


def stop(enable, in1, in2):
    GPIO.output(in1, False)
    GPIO.output(in2, False)
    GPIO.output(enable, False)


def run_forward_motors():
    run_forward(enable_a, motor_a1, motor_a2, pwm_a)
    run_forward(enable_b, motor_b1, motor_b2, pwm_b)


def run_backward_motors():
    run_backward(enable_a, motor_a1, motor_a2, pwm_a)
    run_backward(enable_b, motor_b1, motor_b2, pwm_b)


def rotate_motors_left():
    run_forward(enable_a, motor_a1, motor_a2, pwm_a)
    run_backward(enable_b, motor_b1, motor_b2, pwm_b)


def rotate_motors_right():
    run_backward(enable_a, motor_a1, motor_a2, pwm_a)
    run_forward(enable_b, motor_b1, motor_b2, pwm_b)


def stop_motors():
    stop(enable_a, motor_a1, motor_a2)
    stop(enable_b, motor_b1, motor_b2)


def motors_cleanup():
    GPIO.cleanup()


# run_forward_motors()
# sleep(2)
# stop_motors()
# sleep(2)
#
# rotate_motors_left()
# sleep(1)
# stop_motors()
# sleep(2)
#
# run_backward_motors()
# sleep(2)
# stop_motors()
# sleep(2)
#
# rotate_motors_right()
# sleep(1)
# stop_motors()
# sleep(2)
#
# pwm_a.stop()
# pwm_b.stop()
# GPIO.cleanup()
