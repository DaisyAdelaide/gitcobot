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

const int SWITCH = 12; 
int SWITCH_VALUE = 1400;

const int REVERSE = 13;
int REVERSE_VALUE = 0;

int TURNING_MAGNITUDE;

int RIGHT_SPEED;
int LEFT_SPEED;

int DRIVING = 0;

int axis = 0;
char c = '0';
int motornum = c-'0';
int requested_state;

SoftwareSerial odrive_serial(8, 9);
ODriveArduino odrive(odrive_serial);

void setup() {
  odrive_serial.begin(115200);

  Serial.begin(115200);
  //while (!Serial) ; // wait for Arduino Serial Monitor to open

 // Serial.println("ODriveArduino");
  
}

void loop() {

  THROTTLE_STICK_VALUE = pulseIn(THROTTLE_STICK, HIGH, 25000);
  THROTTLE_BINARY = map(THROTTLE_STICK_VALUE, 1000, 2000, 0, 10);

  TURNING_STICK_VALUE = pulseIn(TURNING_STICK, HIGH, 25000);
  TURNING_BINARY = map(TURNING_STICK_VALUE, 1150, 1700, 0, 100);

  if ((THROTTLE_BINARY > 1) && (DRIVING == 0))
  {
    Serial.println("Driving");
    DRIVING = 1;
  }
  
  if ((THROTTLE_BINARY < 2) && (DRIVING == 1))
  {
    Serial.println("Stop");
    DRIVING = 0;
  }

  SWITCH_VALUE = pulseIn(SWITCH, HIGH, 25000);
  if (SWITCH_VALUE < 1300)
  {
    axis = 0;
    odrive_serial << "w axis" << axis << ".controller.config.vel_limit " << 10.0f << '\n';
    odrive_serial << "w axis" << axis << ".motor.config.current_lim " << 11.0f << '\n';
    
    delay(2000);
    c = '0';
    motornum = c-'0';
    requested_state;
    delay(2000);
    
    requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE;
    if(!odrive.run_state(motornum, requested_state, true)) return;
    delay(3000);
  
    requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL;
    if(!odrive.run_state(motornum, requested_state, false /*don't wait*/)) return;
    delay(3000);  
  }


  if (SWITCH_VALUE > 1800)
  {
    axis = 1;
    odrive_serial << "w axis" << axis << ".controller.config.vel_limit " << 10.0f << '\n';
    odrive_serial << "w axis" << axis << ".motor.config.current_lim " << 11.0f << '\n';
    
    delay(2000);
    c = '1';
    motornum = c-'0';
    requested_state;
    delay(2000);
    
    requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE;
    if(!odrive.run_state(motornum, requested_state, true)) return;
    delay(3000);
  
    requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL;
    if(!odrive.run_state(motornum, requested_state, false /*don't wait*/)) return;
    delay(3000);
  }
  

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

  REVERSE_VALUE = pulseIn(REVERSE, HIGH, 25000);
  if (REVERSE_VALUE < 1000) 
  {
   RIGHT_SPEED = -RIGHT_SPEED;
   LEFT_SPEED = -LEFT_SPEED;
  }
  
  odrive.SetVelocity(0, LEFT_SPEED);
  odrive.SetVelocity(1, -RIGHT_SPEED);

}
