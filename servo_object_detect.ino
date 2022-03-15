
#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

//int pos = 0;    // variable to store the servo position

void setup() {
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
 if(Serial.available()>0){
   int pos = Serial.parseInt();
   switch(pos)
   {
    case 1:
      myservo.write(85);
      delay(5);
      break;
    case 2:
      myservo.write(100);
      delay(5);
      break;
    case 3:
      myservo.write(90);
      delay(5);
      break;
   }
 }
}
