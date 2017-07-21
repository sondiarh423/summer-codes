#include <Servo.h>

int rightWhiskerPin = 7;
int leftWhiskerPin = 5;
int rightWhiskerState = 0;
int leftWhiskerState = 0;

//Declare Right servo
Servo servoRight;
//Declare Left servo
Servo servoLeft;


void setup() {
// put your setup code here, to run once:
delay(1000); 
pinMode(rightWhiskerPin, INPUT);
pinMode(leftWhiskerPin, INPUT);
Serial.begin(9600);
//Attach Left Servo
servoRight.attach(13);
servoLeft.attach(12);
}

void loop() {
// put your main code here, to run repeatedly:
rightWhiskerState = digitalRead(rightWhiskerPin);
leftWhiskerState = digitalRead(leftWhiskerPin);
// whisker state is 1 if unpressed and 0 if pressed.
if(rightWhiskerState == 0 && leftWhiskerState == 0){
//Make it move away from the Obstacle]
backward(1000);
turnRight(200);
}

else if(leftWhiskerState == 0){
//Make it move away from the Obstacle

backward(100);
turnRight(200);

}
else if(rightWhiskerState == 0){
//Make it move away from the Obstacle

backward(1000);
turnLeft(200);

}else{
//Just move
forward(1000);
}
}

void stopnow(){
servoLeft.writeMicroseconds(1500);
servoRight.writeMicroseconds(1500);
}

void forward(int time) // Forward function
{servoLeft.writeMicroseconds(1300);
servoRight.writeMicroseconds(1700);
delay(time);

}

void turnLeft(int time) // Left turn function
{
servoLeft.writeMicroseconds(1300);
servoRight.writeMicroseconds(1700);
delay(time);
}

void turnRight(int time) // Right turn function
{
servoLeft.writeMicroseconds(1500);
servoRight.writeMicroseconds(1000);
delay(time);
}

void backward(int time) // Backward function
{servoLeft.writeMicroseconds(1700);
servoRight.writeMicroseconds(1300);
delay(time);
}






  
             



