const int TURNING_STICK = A1;
int REVERSE_VALUE = 0;
//A3 reverse
//A2 calibrate switch
//A1 throttle
//A0 turning

void setup() {
  Serial.begin(9600);

}

void loop() {
  REVERSE_VALUE = pulseIn(TURNING_STICK, HIGH, 25000);
  Serial.println(REVERSE_VALUE);

}
