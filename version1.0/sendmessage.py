import serial


def stop():
    ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
    ser.flush()  
    ser.write(b"stop\n")
    return

