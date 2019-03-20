// Run DC Motors with L293D

//Define Pins
//Motor A
int enableA = 10;
int MotorA1 = 9;
int MotorA2 = 8;

//Motor B
int enableB = 5;
int MotorB1 = 6;
int MotorB2 = 7;

const int PWM_MAX = 255;
const int PWM_MOTION = PWM_MAX;
const int PWM_ROTATE = PWM_MAX;

const int TIME_MOVE = 1500;
const int TIME_ROTATE = 600;
const int TIME_STOP = 2000;


void setup() {

  //Serial.begin (9600);
  //configure pin modes
  motorSetup(enableA, MotorA1, MotorA2);
  motorSetup(enableB, MotorB1, MotorB2);
}

void loop() {
  run();
}


void run() {

  //Serial.println ("Enabling Motors");

  motorForward(PWM_MOTION);
  delay(TIME_MOVE);
  motorStop();
  delay(TIME_STOP);

  motorRotateRight(PWM_ROTATE);
  delay(TIME_ROTATE);
  motorStop();
  delay(TIME_STOP);

  motorBackward(PWM_MOTION);
  delay(TIME_MOVE);
  motorStop();
  delay(TIME_STOP);

  motorRotateLeft(PWM_ROTATE);
  delay(TIME_ROTATE);
  motorStop();
  delay(TIME_STOP);
}

void motorSetup(int enable, int in1, int in2) {
  pinMode (enable, OUTPUT);
  pinMode (in1, OUTPUT);
  pinMode (in2, OUTPUT);
}


void motorForward(int pwm) {
  motorForward(enableA, pwm, MotorA1, MotorA2);
  motorForward(enableB, pwm, MotorB1, MotorB2);
}

void motorBackward(int pwm) {
  motorBackward(enableA, pwm, MotorA1, MotorA2);
  motorBackward(enableB, pwm, MotorB1, MotorB2);
}

void motorRotateRight(int pwm) {
  motorForward(enableA, pwm, MotorA1, MotorA2);
  motorBackward(enableB, pwm, MotorB1, MotorB2);
}

void motorRotateLeft(int pwm) {
  motorBackward(enableA, pwm, MotorA1, MotorA2);
  motorForward(enableB, pwm, MotorB1, MotorB2);
}


void motorForward(int enable, int pwm, int in1, int in2) {
  analogWrite(enable, pwm);
  digitalWrite (in1, LOW);
  digitalWrite (in2, HIGH);
}

void motorBackward(int enable, int pwm, int in1, int in2) {
  analogWrite(enable, pwm);
  digitalWrite (in1, HIGH);
  digitalWrite (in2, LOW);
}

void motorStop() {
  motorStop(enableA, MotorA1, MotorA2);
  motorStop(enableB, MotorB1, MotorB2);
}

void motorStop(int enable, int in1, int in2) {
  analogWrite(enable, LOW);
  digitalWrite (in1, LOW);
  digitalWrite (in2, LOW);
}
