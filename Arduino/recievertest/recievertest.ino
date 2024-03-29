const int TURNING_STICK = 10;
const int THROTTLE_STICK = 11;

int TURNING_STICK_VALUE = 1150;
int THROTTLE_STICK_VALUE = 1100;

int TURNING_BINARY = 0;
int THROTTLE_BINARY = 0;

int RIGHT_SPEED = 0;
int LEFT_SPEED = 0;

int TURNING_MAG = 0;

int RIGHT_AVERAGE_SPEED = 0;
int LEFT_AVERAGE_SPEED = 0;

int i = 0;

void setup() {
    Serial.begin(9600);
}

void loop() {
  
  TURNING_STICK_VALUE = pulseIn(TURNING_STICK, HIGH, 25000);
  THROTTLE_STICK_VALUE = pulseIn(THROTTLE_STICK, HIGH, 25000);

  //Serial.println(TURNING_STICK_VALUE);
  
  
  TURNING_BINARY = map(TURNING_STICK_VALUE, 1150, 1700, 0, 100);
  THROTTLE_BINARY = map(THROTTLE_STICK_VALUE, 1100, 2000, 0, 100);
  
  if (TURNING_BINARY > 60)
  {
    TURNING_MAG = map(TURNING_BINARY, 60, 100, 90, 10);
    RIGHT_SPEED = THROTTLE_BINARY;
    LEFT_SPEED = THROTTLE_BINARY * TURNING_MAG / 100;
  }
  
  else if (TURNING_BINARY < 40)
  {
    TURNING_MAG = map(TURNING_BINARY, 0, 40, 10, 90);
    LEFT_SPEED = THROTTLE_BINARY;
    RIGHT_SPEED = THROTTLE_BINARY * TURNING_MAG / 100;
  }
  
  else
  {
    LEFT_SPEED = THROTTLE_BINARY;
    RIGHT_SPEED = THROTTLE_BINARY;
  }
  
  RIGHT_SPEED = map(RIGHT_SPEED, 10, 100, 1000, 2000);
  LEFT_SPEED = map(LEFT_SPEED, 10, 100, 1000, 2000);
  
  if (i < 5)
  {
    RIGHT_AVERAGE_SPEED += RIGHT_SPEED;
    LEFT_AVERAGE_SPEED += LEFT_SPEED;
    i += 1;
  }
  
  else if (i == 5)
  {
    RIGHT_SPEED = RIGHT_AVERAGE_SPEED / 5;
    LEFT_SPEED = LEFT_AVERAGE_SPEED / 5;
    if (RIGHT_SPEED < 1000)
    {
      RIGHT_SPEED = 1000;
    }
    if (LEFT_SPEED < 1000)
    {
      LEFT_SPEED = 1000;
    }

    
    
    RIGHT_AVERAGE_SPEED = 0;
    LEFT_AVERAGE_SPEED = 0;
    
    i = 0;
  }
  delay(5); 
  Serial.println(RIGHT_SPEED);
}
