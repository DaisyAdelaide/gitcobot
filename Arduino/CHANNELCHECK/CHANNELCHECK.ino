const int TURNING_STICK = 12;
int REVERSE_VALUE = 0;


void setup() {
  Serial.begin(9600);

}

void loop() {
  REVERSE_VALUE = pulseIn(TURNING_STICK, HIGH, 25000);
  Serial.println(REVERSE_VALUE);

}
