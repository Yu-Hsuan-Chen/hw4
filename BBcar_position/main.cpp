#include"mbed.h"
#include "bbcar.h"
#include "bbcar_rpc.h"

BufferedSerial pc(USBTX,USBRX); //tx,rx

Ticker servo_ticker;
DigitalOut led1(LED1);
BufferedSerial uart(D1,D0); //tx,rxss
// static BufferedSerial pc(STDIO_UART_TX, STDIO_UART_RX);
// DigitalInOut ping(D10);
DigitalInOut pin10(D10);
parallax_ping  ping1(pin10);
PwmOut pin5(D5), pin6(D6);
BBCar car(pin5, pin6, servo_ticker);

int main(){
   uart.set_baud(9600);
   printf("Start!\n");
   while(1){
      if(uart.readable()){
            char recv[1];
            uart.read(recv, sizeof(recv));
            pc.write(recv, sizeof(recv));
            // printf("%s\n", recv);
      }else{printf("bad\n");}
   }
}
