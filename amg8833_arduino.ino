#include <Wire.h>
#include <Adafruit_AMG88xx.h>

Adafruit_AMG88xx amg;
float pixels[AMG88xx_PIXEL_ARRAY_SIZE];

void setup() {
    Serial.begin(9600);
    bool status;
    status = amg.begin();
    if (!status) {
        Serial.println("Could not find a valid AMG88xx sensor, check wiring!");
        while (1);
    }
    delay(100); // let sensor boot up
}


void loop() { 
    //read all the pixels
    amg.readPixels(pixels);
    for(int i=0;i<64;i++)
      Serial.print(String(pixels[i])+",");
    Serial.println();
    delay(10);
}
