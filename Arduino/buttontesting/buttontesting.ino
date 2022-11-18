const int FORWARD_BUTTON = 2;  
const int LEFT_BUTTON = 3;
const int RIGHT_BUTTON = 4;  
//const int BACK_BUTTON = 5;

int FORWARD_BUTTON_STATE;            
int LAST_FORWARD_BUTTON_STATE = LOW; 

int LEFT_BUTTON_STATE;            
int LAST_LEFT_BUTTON_STATE = LOW; 

int RIGHT_BUTTON_STATE;            
int LAST_RIGHT_BUTTON_STATE = LOW; 

int BACK_BUTTON_STATE;            
int LAST_BACK_BUTTON_STATE = LOW; 

unsigned long foward_lastDebounceTime = 0;  
unsigned long left_lastDebounceTime = 0;  
unsigned long right_lastDebounceTime = 0;  
unsigned long back_lastDebounceTime = 0;  

unsigned long debounceDelay = 50;    

void setup() {
  Serial.begin(9600);
  pinMode(FORWARD_BUTTON, INPUT);
  pinMode(LEFT_BUTTON, INPUT);
  pinMode(RIGHT_BUTTON, INPUT);
//  pinMode(BACK_BUTTON, INPUT);

  delay(1000);
}

void loop() {
  int forward_reading = digitalRead(FORWARD_BUTTON);
  int left_reading = digitalRead(LEFT_BUTTON);
  int right_reading = digitalRead(RIGHT_BUTTON);
 // int back_reading = digitalRead(BACK_BUTTON);

  if (forward_reading != LAST_FORWARD_BUTTON_STATE) {
    foward_lastDebounceTime = millis();
  }

  else if (left_reading != LAST_LEFT_BUTTON_STATE) {
    left_lastDebounceTime = millis();
  }

  else if (right_reading != LAST_RIGHT_BUTTON_STATE) {
    right_lastDebounceTime = millis();
  }

/*  else if (back_reading != LAST_BACK_BUTTON_STATE) {
    back_lastDebounceTime = millis();
  }*/

  if ((millis() - foward_lastDebounceTime) > debounceDelay) {
    
    if (forward_reading != FORWARD_BUTTON_STATE) {
      FORWARD_BUTTON_STATE = forward_reading;

      if (FORWARD_BUTTON_STATE == HIGH) {
        Serial.println("forward");
      }
    }
  }

   if ((millis() - left_lastDebounceTime) > debounceDelay) {
    
    if (left_reading != LEFT_BUTTON_STATE) {
      LEFT_BUTTON_STATE = left_reading;

      if (LEFT_BUTTON_STATE == HIGH) {
        Serial.println("left");
      }
    }
  }

  if ((millis() - right_lastDebounceTime) > debounceDelay) {
    
    if (right_reading != RIGHT_BUTTON_STATE) {
      RIGHT_BUTTON_STATE = right_reading;

      if (RIGHT_BUTTON_STATE == HIGH) {
        Serial.println("RIGHT");
      }
    }
  }
/*
  if ((millis() - back_lastDebounceTime) > debounceDelay) {
    
    if (back_reading != BACK_BUTTON_STATE) {
      BACK_BUTTON_STATE = back_reading;

      if (BACK_BUTTON_STATE == HIGH) {
        Serial.println("BACK");
      }
    }
  }
  */
  LAST_FORWARD_BUTTON_STATE = forward_reading;
  LAST_LEFT_BUTTON_STATE = left_reading;
  LAST_RIGHT_BUTTON_STATE = right_reading;
//  LAST_BACK_BUTTON_STATE = back_reading;
}
