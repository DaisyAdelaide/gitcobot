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
    FORWARD_BUTTON_STATE = digitalRead(FORWARD_BUTTON);
    LEFT_BUTTON_STATE = digitalRead(LEFT_BUTTON);
    RIGHT_BUTTON_STATE = digitalRead(RIGHT_BUTTON);
    BACK_BUTTON_STATE = digitalRead(BACK_BUTTON);
    
    if (FORWARD_BUTTON_STATE == HIGH && FORWARD_PRESSED == 0)
    {
      FORWARD_PRESSED += 1;
      Serial.println("forward");
      delay(200);
      return;
    }
    else if ((FORWARD_BUTTON_STATE == LOW)&& (FORWARD_PRESSED == 1))
    {
      FORWARD_PRESSED = 0;
    }

    if (LEFT_BUTTON_STATE == HIGH && LEFT_PRESSED == 0)
    {
      LEFT_PRESSED += 1;
      Serial.println("LEFT");
      delay(200);
      return;
    }
    else if ((LEFT_BUTTON_STATE == LOW)&& (LEFT_PRESSED == 1))
    {
      LEFT_PRESSED = 0;
    }

    
    delay(5);

 }
