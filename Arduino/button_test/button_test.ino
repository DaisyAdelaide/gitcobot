const int FORWARD_BUTTON = 2;
int FORWARD_BUTTON_STATE = 0;
int FORWARD_PRESSED = 0;

const int LEFT_BUTTON = 3;
int LEFT_BUTTON_STATE = 0;
int LEFT_PRESSED = 0;

const int RIGHT_BUTTON = 4;
int RIGHT_BUTTON_STATE = 0;
int RIGHT_PRESSED = 0;

const int BACK_BUTTON = 5;
int BACK_BUTTON_STATE = 0;
int BACK_PRESSED = 0;


//int FORWARD_BUTTON_STATE;            
int LAST_FORWARD_BUTTON_STATE = LOW; 

unsigned long foward_lastDebounceTime = 0;  
unsigned long debounceDelay = 50;   

void setup()
{
  Serial.begin(9600);
  
  pinMode(FORWARD_BUTTON, INPUT);
  pinMode(LEFT_BUTTON, INPUT);
  pinMode(RIGHT_BUTTON, INPUT);
  pinMode(BACK_BUTTON, INPUT);
}

void loop()
{
    int forward_reading = digitalRead(FORWARD_BUTTON);
    LEFT_BUTTON_STATE = digitalRead(LEFT_BUTTON);
    RIGHT_BUTTON_STATE = digitalRead(RIGHT_BUTTON);
    BACK_BUTTON_STATE = digitalRead(BACK_BUTTON);

    if (forward_reading != LAST_FORWARD_BUTTON_STATE) 
    {
      foward_lastDebounceTime = millis();
    }
    
    if ((millis() - foward_lastDebounceTime) > debounceDelay) 
    {    
      if (forward_reading != FORWARD_BUTTON_STATE) 
      {
        FORWARD_BUTTON_STATE = forward_reading;

        if (FORWARD_BUTTON_STATE == HIGH) 
        {
          Serial.println("forward");
        }
      }
    }
    
    else if ((FORWARD_BUTTON_STATE == LOW)&& (FORWARD_PRESSED == 1))
    {
      FORWARD_PRESSED = 0;
      Serial.println("stop");
    }
    
    LAST_FORWARD_BUTTON_STATE = forward_reading;
    delay(5);

 }
