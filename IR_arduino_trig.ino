
const byte interruptPin = 2;
bool state = false;

void setup() {
 
  pinMode(interruptPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(interruptPin), blink, FALLING);
  Serial.begin(9600);
}

void loop() {
 
    if (state == true)
    {Serial.println(1);
    state=false;}
  

}

void blink() {
  state = true;
}
