import serial


if __name__ == '__main__':
    ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
    ser.flush()
    
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            
            if line != 'LOW' and line != 'HIGH' and line != 'HALF':

                if float(line) < 250:
                    ser.write(b"below half\n")

                elif float(line) > 250:
                    ser.write(b"above half\n")
                    
                else:
                    ser.write(b"halfway\n")

      