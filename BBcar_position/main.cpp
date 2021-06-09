#include"mbed.h"
#include "bbcar.h"
//BufferedSerial pc(USBTX,USBRX); //tx,rx
BufferedSerial uart(D1,D0); //tx,rx
static BufferedSerial pc(STDIO_UART_TX, STDIO_UART_RX);
// DigitalInOut ping(D10);
DigitalInOut pin10(D10);
parallax_ping  ping1(pin10);
PwmOut pin5(D5), pin6(D6);
BBCar car(pin5, pin6, servo_ticker);

Timer t;
Ticker servo_ticker;

int main(){
   uart.set_baud(9600);
   double distance = 0;

   while(1){

      distance = (float)ping1*17700.4f;
      printf("Ping = %lf\r\n", distance);

      if(uart.readable() && distance > 20){
         char recv[1];
         uart.read(recv, sizeof(recv));
         if(recv[0] == 'f') {
            car.goStraight(100, 0.9, 1);
            ThisThread::sleep_for(1000ms);
            car.stop();
            
         }
         else if(recv[0] == 'l' ) {
            car.turn(50,0.3);
            ThisThread::sleep_for(1000ms);
            car.stop();
         }
         else if(recv[0] == 'r' ) {
            car.turn(50,-0.3);
            ThisThread::sleep_for(1000ms);
            car.stop();
         }
      }
   }
}

//   ping.output();
//   ping = 0; wait_us(200);
//   ping = 1; wait_us(5);
//   ping = 0; wait_us(5);
//   ping.input();
//   while(ping.read() == 0);
//   t.start();
//   while(ping.read() == 1);
//   val = t.read();
//   printf("Ping = %lf\r\n", val*17700.4f);
//   distance = val*17700.4f;
//   t.stop();
//   t.reset();


