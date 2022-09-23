while True:
        pi.set_servo_pulsewidth(ESC, speed)
        inp = input()
        
        if inp == "q":
            speed -= 100    # decrementing the speed like hell
            print ("speed = {speed}".format(speed=speed)) 
        elif inp == "e":    
            speed += 100    # incrementing the speed like hell
            print ("speed = {speed}".format(speed=speed)) 
        elif inp == "d":
            speed += 10     # incrementing the speed 
            print ("speed = {speed}".format(speed=speed)) 
        elif inp == "a":
            speed -= 10     # decrementing the speed
            print ("speed = {speed}".format(speed=speed)) 
        elif inp == "stop":
            stop()          #going for the stop function
            break
        elif inp == "manual":
            manual_drive()
            break
        elif inp == "arm":
            arm()
            break
        else:
            print ("WHAT DID I SAID!! Press a,q,d or e")
      