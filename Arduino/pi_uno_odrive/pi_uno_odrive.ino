#include <HardwareSerial.h>
#include <SoftwareSerial.h>
#include <ODriveArduino.h>

template<class T> inline Print& operator <<(Print &obj,     T arg) { obj.print(arg);    return obj; }
template<>        inline Print& operator <<(Print &obj, float arg) { obj.print(arg, 4); return obj; }


const int THROTTLE_STICK = 10;
int THROTTLE_STICK_VALUE = 1100;
int THROTTLE_BINARY = 0;

const int TURNING_STICK = 11;
int TURNING_STICK_VALUE = 1450;
int TURNING_BINARY = 0;

int TURNING_MAGNITUDE;

int RIGHT_SPEED;
int LEFT_SPEED;

SoftwareSerial odrive_serial(8, 9);
ODriveArduino odrive(odrive_serial);

void setup() {
  odrive_serial.begin(115200);

  Serial.begin(115200);
  //while (!Serial) ; // wait for Arduino Serial Monitor to open

  //Serial.println("ODriveArduino");

  for (int axis = 0; axis < 2; ++axis) {
    odrive_serial << "w axis" << axis << ".controller.config.vel_limit " << 10.0f << '\n';
    odrive_serial << "w axis" << axis << ".motor.config.current_lim " << 11.0f << '\n';
    // This ends up writing something like "w axis0.motor.config.current_lim 10.0\n"
  }

  char c = '0';
  int motornum = c-'0';
  int requested_state;

  requested_state = AXIS_STATE_MOTOR_CALIBRATION;
  //Serial << "Axis" << c << ": Requesting state " << requested_state << '\n';
  if(!odrive.run_state(motornum, requested_state, true)) return;

  //delay(2000);

  requested_state = AXIS_STATE_ENCODER_OFFSET_CALIBRATION;
  //Serial << "Axis" << c << ": Requesting state " << requested_state << '\n';
  if(!odrive.run_state(motornum, requested_state, true, 25.0f)) return;
  //delay(2000);

  requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL;
  //Serial << "Axis" << c << ": Requesting state " << requested_state << '\n';
  if(!odrive.run_state(motornum, requested_state, false /*don't wait*/)) return;
 // delay(2000);

  c = '1';
  motornum = c-'0';
  requested_state = AXIS_STATE_MOTOR_CALIBRATION;
 // Serial << "Axis" << c << ": Requesting state " << requested_state << '\n';
  if(!odrive.run_state(motornum, requested_state, true)) return;
  //delay(2000);

  requested_state = AXIS_STATE_ENCODER_OFFSET_CALIBRATION;
  //Serial << "Axis" << c << ": Requesting state " << requested_state << '\n';
  if(!odrive.run_state(motornum, requested_state, true, 25.0f)) return;
  //delay(2000);

  requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL;
  //Serial << "Axis" << c << ": Requesting state " << requested_state << '\n';
  if(!odrive.run_state(motornum, requested_state, false /*don't wait*/)) return;  
  //delay(2000);
  
}

void loop() {

  THROTTLE_STICK_VALUE = pulseIn(THROTTLE_STICK, HIGH, 25000);
  THROTTLE_BINARY = map(THROTTLE_STICK_VALUE, 1000, 2000, 0, 10);

  TURNING_STICK_VALUE = pulseIn(TURNING_STICK, HIGH, 25000);
  TURNING_BINARY = map(TURNING_STICK_VALUE, 1150, 1700, 0, 100);

  //Serial.println(TURNING_BINARY);

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
  Serial.println(String(RIGHT_SPEED));
  Serial.println(String(LEFT_SPEED));
  
  odrive.SetVelocity(0, LEFT_SPEED);
  odrive.SetVelocity(1, -RIGHT_SPEED);
  delay(5);
}
