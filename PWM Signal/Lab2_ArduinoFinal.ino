//const int input = A0; // This is where the input is fed.
int pulse = 0; // Variable for saving pulses count.
int var = 0;
int digitalPin = 20;
char IncomingByte;

int val=0;
const int pin_in=A0; 
int pin_out=10;
void setup() { 
  // put your setup code here, to run once: 
  TCCR2B = (TCCR2B & 0xF8) | 0x03;  //pg. 57
  //TCCR1B = (TCCR1B & 0xF8) | 0x02;  //pg. 57
  pinMode(pin_in, INPUT);
  attachInterrupt (digitalPinToInterrupt(digitalPin),pulse_counter,HIGH);
  Serial.begin(9600);
  //Serial.println(F("No pulses yet...")); // Message to send initially (no pulses detected yet).
} 

void loop() { 
  // put your main code here, to run repeatedly: 

  val=analogRead(pin_in); 
  val << 2;
  analogWrite(pin_out,val/4);

  //TCCR2B = TCCR2B & ~B00110000; //switch off output B
  //TCCR2B |= B00110000;  //switch on the B output with inverted output
  //analogWrite(pin_out,1023);
  if (Serial.available() > 0){
      IncomingByte=Serial.read();
      Serial.println(pulse);
  }
     
} 

void pulse_counter() 
  {

    pulse++;
   // while(Serial.available()) {
    //Serial.println(float(pulse),0);
    
    }
   
