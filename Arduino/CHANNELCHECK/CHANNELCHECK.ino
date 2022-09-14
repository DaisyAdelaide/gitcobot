const int TURNING_STICK = 7;
int REVERSE_VALUE = 0;


void setup() {
  Serial.begin(9600);

}

void loop() {
  REVERSE_VALUE = pulseIn(TURNING_STICK, HIGH, 25000);
  Serial.println(REVERSE_VALUE);

}
