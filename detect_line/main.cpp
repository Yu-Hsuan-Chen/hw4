#include"mbed.h"
#include "bbcar.h"
#include "bbcar_rpc.h"
Ticker servo_ticker;
PwmOut pin5(D5), pin6(D6);

BBCar car(pin5, pin6, servo_ticker);

BufferedSerial pc(USBTX,USBRX); //tx,rx
BufferedSerial uart(D1,D0); //tx,rx

int main(){
   char buf[256], outbuf[256];
   uart.set_baud(9600);
   while(1){
      memset(buf, 0, 256);
      for( int i = 0; ; i++ ) {
         if(uart.readable()){
            char recv[1];
            uart.read(recv, sizeof(recv));
            buf[i] = recv;
         }
         else
            break;   
      }
      RPC::call(buf, outbuf);
   }
}



// int main() {
//    char buf[256], outbuf[256];
//    FILE *devin = fdopen(&xbee, "r");
//    FILE *devout = fdopen(&xbee, "w");
//    while (1) {
//       memset(buf, 0, 256);
//       for( int i = 0; ; i++ ) {
//          char recv = fgetc(devin);
//          if(recv == '\n') {
//             printf("\r\n");
//             break;
//          }
//          buf[i] = fputc(recv, devout);
//       }
//    RPC::call(buf, outbuf);
//    }
// }
