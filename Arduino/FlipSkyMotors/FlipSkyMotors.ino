#include <HardwareSerial.h>
#include <SoftwareSerial.h>
#include <ODriveArduino.h>

template<class T> inline Print& operator <<(Print &obj,     T arg) { obj.print(arg);    return obj; }
template<>        inline Print& operator <<(Print &obj, float arg) { obj.print(arg, 4); return obj; }

const int THROTTLE_STICK = A1;
int THROTTLE_STICK_VALUE = 900;
int THROTTLE_BINARY = 0;

const int TURNING_STICK = A0;
int TURNING_STICK_VALUE = 1300;
int TURNING_BINARY = 0;

int TURNING_MAGNITUDE;

int RIGHT_SPEED;
int LEFT_SPEED;

const int SWITCH = A2; 
int SWITCH_VALUE = 1400;

SoftwareSerial odrive_serial(8,9);
ODriveArduino odrive(odrive_serial);

void setup() {
  // put your setup code here, to run once:
  odrive_serial.begin(115200);
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:
  THROTTLE_STICK_VALUE = pulseIn(THROTTLE_STICK, HIGH, 25000);
  THROTTLE_BINARY = map(THROTTLE_STICK_VALUE, 900, 1900, 0, 10);

  TURNING_STICK_VALUE = pulseIn(TURNING_STICK, HIGH, 25000);
  TURNING_BINARY = map(TURNING_STICK_VALUE, 1800, 800, 0, 100);

  SWITCH_VALUE = pulseIn(SWITCH, HIGH, 25000);

  if (SWITCH_VALUE > 1800)
  { 
    char c = '0';
    int motornum = c-'0';
    int requested_state;
    delay(500);
    
    requested_state = AXIS_STATE_MOTOR_CALIBRATION;
    //Serial << "Axis" << c << ": Requesting state " << requested_state << '\n';
    if(!odrive.run_state(motornum, requested_state, true)) return;
    delay(2000);

    requested_state = AXIS_STATE_ENCODER_HALL_POLARITY_CALIBRATION;
   // Serial << "Axis" << c << ": Requesting state " << requested_state << '\n';
    if(!odrive.run_state(motornum, requested_state, true, 25.0f)) return;
    delay(2000);
    
    requested_state = AXIS_STATE_ENCODER_OFFSET_CALIBRATION;
   // Serial << "Axis" << c << ": Requesting state " << requested_state << '\n';
    if(!odrive.run_state(motornum, requested_state, true, 25.0f)) return;
    delay(2000);
  
    requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL;
    //Serial << "Axis" << c << ": Requesting state " << requested_state << '\n';
    if(!odrive.run_state(motornum, requested_state, false /*don't wait*/)) return;
    delay(1000);
  
    c = '1';
    motornum = c-'0';
    delay(500);
    requested_state = AXIS_STATE_MOTOR_CALIBRATION;
    //Serial << "Axis" << c << ": Requesting state " << requested_state << '\n';
    if(!odrive.run_state(motornum, requested_state, true)) return;
    delay(2000);

    requested_state = AXIS_STATE_ENCODER_HALL_POLARITY_CALIBRATION;
   // Serial << "Axis" << c << ": Requesting state " << requested_state << '\n';
    if(!odrive.run_state(motornum, requested_state, true, 25.0f)) return;
    delay(2000);
  
    requested_state = AXIS_STATE_ENCODER_OFFSET_CALIBRATION;
    //Serial << "Axis" << c << ": Requesting state " << requested_state << '\n';
    if(!odrive.run_state(motornum, requested_state, true, 25.0f)) return;
    delay(2000);
  
    requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL;
   // Serial << "Axis" << c << ": Requesting state " << requested_state << '\n';
    if(!odrive.run_state(motornum, requested_state, false /*don't wait*/)) return;  
    delay(1000); 
}
if (TURNING_BINARY < 40)
   {
    TURNING_MAGNITUDE = map(TURNING_BINARY, 0, 40, 10, 90);
    RIGHT_SPEED = THROTTLE_BINARY;
    LEFT_SPEED = THROTTLE_BINARY * TURNING_MAGNITUDE/100;    
   }
 else if (TURNING_BINARY > 60)
   {
    TURNING_MAGNITUDE = map(TURNING_BINARY, 60, 100, 90, 10);
    LEFT_SPEED = THROTTLE_BINARY;
    RIGHT_SPEED = THROTTLE_BINARY * TURNING_MAGNITUDE/100;    
   }
 else
  {
   RIGHT_SPEED = THROTTLE_BINARY;
   LEFT_SPEED = THROTTLE_BINARY; 
  }

  if (RIGHT_SPEED < 2){
    RIGHT_SPEED = 0;
  }
  if (LEFT_SPEED < 2){
    LEFT_SPEED = 0;
  }

  odrive.SetVelocity(1, LEFT_SPEED*1);
  odrive.SetVelocity(0, -RIGHT_SPEED*1);
  delay(5);


}
