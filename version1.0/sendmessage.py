import serial


def stop():
    ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
    ser.flush()  
    ser.write(b"stop\n")
    return

def arm():
    ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
    ser.flush()  
    ser.write(b"arm\n")
    return
    

