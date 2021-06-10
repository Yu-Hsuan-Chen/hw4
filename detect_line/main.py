THRESHOLD = (0, 100) # Grayscale threshold for dark things...

FRAME_REGION = 0.5 # Percentage of the image from the bottom (0 - 1.0).
FRAME_WIDE = 0.6 # Percentage of the frame width.
FRAME_REGION = max(min(FRAME_REGION, 1.0), 0.0)
FRAME_WIDE = max(min(FRAME_WIDE, 1.0), 0.0)
SPEED = 50
import sensor, image, time, pyb

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQQVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
sensor.set_vflip(True)
sensor.set_hmirror(True)
sensor.set_windowing((int((sensor.width() / 2) - (int(sensor.width() / 2) * FRAME_WIDE)-5), int(sensor.height() * (1.0 - FRAME_REGION)), \
                     int((sensor.width() / 2) + (int(sensor.width() / 2) * FRAME_WIDE)-5), int(sensor.height() * FRAME_REGION)))

clock = time.clock()
uart = pyb.UART(3,9600,timeout_char=1000)
uart.init(9600,bits=8,parity = None, stop=1, timeout_char=1000)

while(True):
    clock.tick()
    img = sensor.snapshot().binary([THRESHOLD])
    line = img.get_regression([(255,255)])
    turn = 70
    factor = 0.2

    if (line):
        img.draw_line(line.line(), color = 127)
        if line.theta() < 15 or line.theta() >165:
            print("go straight: %d", line.theta())
            uart.write(("/goStraight/run %d 1 1 \n" % SPEED).encode())
        elif line.theta()>=90 and line.theta()<=165: #turn left
            print("turn left: %d", line.theta())
            turn = 1.2*(180-line.theta())
            factor = 1-(180-line.theta())/8
            uart.write(("/turn/run %d %f \n" % (turn, factor)).encode())
        else:                                        #turn right
            print("turn right: %d", line.theta())
            turn = 1.2*line.theta()
            factor = 1-(line.theta())/8
            uart.write(("/turn/run %d %f \n" % (turn, -factor)).encode())
    else:
        print("stop")
        uart.write(("/stop/run \n").encode())




    #print("FPS %f, mag = %s" % (clock.fps(), str(line.magnitude()) if (line) else "N/A"))


