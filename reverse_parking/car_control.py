import time
import serial
import sys,tty,termios

s = serial.Serial(sys.argv[1])

import time
import serial
import sys,tty,termios
class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def get():
    inkey = _Getch()
    while(1):
        k=inkey()
        if k!='':break
    if k=='\x1b':
        k2 = inkey()
        k3 = inkey()
        k4 = inkey()
        k5 = inkey()
        k6 = inkey()
        if (k3=='C'and k6=='A') or (k3=='A'and k6=='C'):
            print ("up right")
            s.write("/turn/run 100 -0.3\n".encode())
            time.sleep(2.2)
        if (k3=='D'and k6=='A') or (k3=='A'and k6=='D'):
            print ("up left")
            s.write("/turn/run 100 0.3\n".encode())
            time.sleep(2.2)
        if (k3=='C'and k6=='B') or (k3=='B'and k6=='C'):
            print ("down right")
            s.write("/turn/run -100 -0.3\n".encode())
            time.sleep(2.2)
        if (k3=='D'and k6=='B') or (k3=='B'and k6=='D'):
            print ("down left")
            s.write("/turn/run -100 0.3\n".encode())
            time.sleep(2.2)
        if k3=='A' and k6=='A':
            print ("up")
            s.write("/goStraight/run 50 0.9 1\n".encode())
            time.sleep(1)
        if k3=='B' and k6=='B':
            print ("down")
            s.write("/goStraight/run -50 0.9 1\n".encode())
            time.sleep(2.8)
        # time.sleep(1)
        s.write("/stop/run \n".encode())
    elif k=='q':
        print ("quit")
        return 0
    else:
        print ("not an arrow key!")
    return 1

if len(sys.argv) < 1:
    print ("No port input")

# while get():
#     i = 0


position = input("poisition:")
d1 = int(input("d1:"))
d2 = int(input("d2:"))


if position == 'left': 
    #goStraight
    if d2 > 0:
        a1 = d2*2.44
        s.write("/goStraight/run 50 1 1\n".encode())
    else: #d2 < 0
        a1 = -d2*2.43
        s.write("/goStraight/run -50 1 1\n".encode())
    time.sleep(a1)
    s.write("/stop/run \n".encode())
    #goStraight
    s.write("/goStraight/run -50 0.9 1\n".encode())
    time.sleep(0.65)
    s.write("/stop/run \n".encode())
    #turn
    s.write("/turn/run -100 -0.3 \n".encode())
    time.sleep(2.7)
    s.write("/stop/run \n".encode())
    #goStraight
    a2 = 2.2+(d1-1)*2.5
    s.write("/goStraight/run -50 0.9 1\n".encode())
    time.sleep(a2)
    s.write("/stop/run \n".encode())

elif position == 'right':
    #goStraight
    if d2 > 0:
        a1 = (d2-1)*2.45
        s.write("/goStraight/run -50 0.9 1\n".encode())
    else: #d2 <= 0
        a1 = -(d2-1)*2.45
        s.write("/goStraight/run 50 1 1\n".encode())
    time.sleep(a1)
    s.write("/stop/run \n".encode())
    #goStraight
    s.write("/goStraight/run -50 0.9 1\n".encode())
    time.sleep(0.45)
    s.write("/stop/run \n".encode())
    #turn
    s.write("/turn/run -100 0.3 \n".encode())
    time.sleep(3.1)
    s.write("/stop/run \n".encode())
    #goStraight
    a2 = 1.9+(d1-1)*2.7
    s.write("/goStraight/run -50 0.9 1\n".encode())
    time.sleep(a2)
    s.write("/stop/run \n".encode())

elif position == 'front':
    if d1 == 2:
        s.write("/goStraight/run -50 0.9 1\n".encode())
        time.sleep(2.7)
        s.write("/stop/run \n".encode())
    #turn
    if d2 > 0:
        s.write("/turn/run 100 0.3\n".encode()) #up right
        time.sleep(2.7)
        s.write("/stop/run \n".encode())
    else: 
        s.write("/turn/run 100 -0.3\n".encode()) #up left
        time.sleep(2.7)
        s.write("/stop/run \n".encode())

    #goStraight
    if d2 > 0:
        a1 = 0.9+(d2-1)*2.9
        s.write("/goStraight/run -50 1 1\n".encode())
    else: 
        a1 = 1.1-d2*2.45
        s.write("/goStraight/run -50 1 1\n".encode())
    time.sleep(a1)
    s.write("/stop/run \n".encode())
    #turn
    if d2 > 0:
        s.write("/turn/run -100 0.3 \n".encode()) 
        time.sleep(3.2)
    else:
        s.write("/turn/run -100 -0.3 \n".encode())
        time.sleep(2.9)
    s.write("/stop/run \n".encode())
    #goStraight
    a2 = 2.4+d1*1.6
    s.write("/goStraight/run -50 0.9 1\n".encode())
    time.sleep(a2)
    s.write("/stop/run \n".encode())