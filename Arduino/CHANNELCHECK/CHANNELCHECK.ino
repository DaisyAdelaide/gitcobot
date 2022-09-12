const int TURNING_STICK = 13;
int TURNING_STICK_VALUE = 0;


void setup() {
  Serial.begin(9600);

}

void loop() {
  TURNING_STICK_VALUE = pulseIn(TURNING_STICK, HIGH, 25000);
  Serial.println(TURNING_STICK_VALUE);

}
