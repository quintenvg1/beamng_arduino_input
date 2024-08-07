#include <Arduino.h>

//define variables
int handbrakepin = 4; //active low so 1 is handbrake pulled
int blinkerpinl = 5; //active high so 1 = not pressed
int blinkerpinr = 6; //active high
int starterpin = 7; //active high

int led = 13;
bool blinkerl = 0;
bool blinkerr = 0;
bool handbrake = 0;
bool starter = 0;


// put function declarations here:



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  pinMode(blinkerpinl, INPUT_PULLUP);
  pinMode(blinkerpinr, INPUT_PULLUP);
  pinMode(handbrakepin, INPUT);
  pinMode(starterpin, INPUT_PULLUP);
  pinMode(led, OUTPUT);
}


void loop() {
  // put your main code here, to run repeatedly:
  //read inputs
  delay(0.016); //refresh at roughly 60 Hz
  blinkerl = digitalRead(blinkerpinl);
  blinkerr = digitalRead(blinkerpinr);
  handbrake = digitalRead(handbrakepin);
  starter = digitalRead(starterpin);
  //write outputs
  Serial.print(blinkerl);
  Serial.print(',');
  Serial.print(blinkerr);
  Serial.print(',');
  Serial.print(handbrake);
  Serial.print(',');
  Serial.println(starter);
}

