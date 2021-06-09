#include"mbed.h"
#include "bbcar.h"


// BufferedSerial pc(USBTX,USBRX); //tx,rx

Ticker servo_ticker;
DigitalOut led1(LED1);
BufferedSerial uart(D1,D0); //tx,rxss
static BufferedSerial pc(STDIO_UART_TX, STDIO_UART_RX);
DigitalInOut pin10(D10);

PwmOut pin5(D5), pin6(D6);
BBCar car(pin5, pin6, servo_ticker);

int main(){
   uart.set_baud(9600);
   parallax_ping  ping1(pin10);
   while(1){
      printf("Ping = %lf\r\n", (float)ping1);
      if(uart.readable() && (float)ping1>20){
         char recv[1];
         uart.read(recv, sizeof(recv));
         if(recv[0] == 'g') {
            printf("go straight!\n");
            car.goStraight(50, 1, 1);
            ThisThread::sleep_for(1000ms);
            car.stop();
         }
         else if(recv[0] == 'l') {
            printf("turn left!\n");
            car.turn(30,-0.3);
            ThisThread::sleep_for(1000ms);
            car.stop();
            // ThisThread::sleep_for(500ms);
         }
         else if(recv[0] == 'r') {
            printf("Turn right!\n");
            car.turn(30, 0.3);
            ThisThread::sleep_for(1000ms);
            car.stop();
            // ThisThread::sleep_for(500ms);
         }
      }
   }
}
