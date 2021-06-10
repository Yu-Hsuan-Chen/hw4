import pyb, sensor, image, time, math

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA) # we run out of memory if the resolution is much bigger...
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)  # must turn this off to prevent image washout...
sensor.set_auto_whitebal(False)  # must turn this off to prevent image washout...
sensor.set_vflip(True)
sensor.set_hmirror(True)
clock = time.clock()

f_x = (2.8 / 3.984) * 160 # find_apriltags defaults to this if not set
f_y = (2.8 / 2.952) * 120 # find_apriltags defaults to this if not set
c_x = 160 * 0.5 # find_apriltags defaults to this if not set (the image.w * 0.5)
c_y = 120 * 0.5 # find_apriltags defaults to this if not set (the image.h * 0.5)

def degrees(radians):
   return (180 * radians) / math.pi

uart = pyb.UART(3,9600,timeout_char=1000)
uart.init(9600,bits=8,parity = None, stop=1, timeout_char=1000)

while(True):
    clock.tick()
    img = sensor.snapshot()
    for tag in img.find_apriltags(fx=f_x, fy=f_y, cx=c_x, cy=c_y): # defaults to TAG36H11
        img.draw_rectangle(tag.rect(), color = (255, 0, 0))
        img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))
        if (degrees(tag.y_rotation())<360 and degrees(tag.y_rotation())>=355) or (degrees(tag.y_rotation())<5 and degrees(tag.y_rotation())>=0):
            print("go: %f", degrees(tag.y_rotation()))
            uart.write(("g").encode())
        elif degrees(tag.y_rotation())>=5 and degrees(tag.y_rotation())<=55:
            print("left: %f", degrees(tag.y_rotation()))
            uart.write(("l").encode())
        elif degrees(tag.y_rotation())>=300 and degrees(tag.y_rotation())<=355:
            print("right: %f", degrees(tag.y_rotation()))
            uart.write(("r").encode())
        else:
            print("other: %f", degrees(tag.y_rotation()))






