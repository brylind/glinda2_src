# Mic Recording Script
#HEY BRYCE!

def GPS():
    from time import sleep, time
    import adafruit_gps
    import datetime
    import board
    import busio

    import serial
    uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)

    gps = adafruit_gps.GPS(uart, debug=False) # Use UART/pyserial

    # Turn on the basic GGA and RMC info (what you typically want)
    gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

    # Set update rate to once a second (1hz) which is what you typically want.
    gps.send_command(b"PMTK220,1000")

    launch_time = datetime.datetime.now()
    timestr = launch_time.strftime("%Y_%m_%d_%H_%M_%S")
    gpsPath = "/home/pi/infrasound/dataFiles/gpsData" + timestr + ".csv"
    f = open(gpsPath,'a+')
    dat = []
    looptime = time()
    #try:
    print('Reading GPS...\n')

    try:
        while 1:
            for j in range(9):
                for i in range(60):
                    gps.update()
                    if gps.has_fix:
                        dat.append([time(), gps.latitude, gps.longitude, gps.speed_knots, gps.fix_quality, gps.satellites])
                    else:
                        dat.append([time(), 0, 0, -1, -1, 0])
                    sleep(1)
                #print('Writing... \n')
                for d in dat:
                    f.write(str(d[0]) + ',' + str(d[1]) + ',' + str(d[2]) + ',' + str(d[3]) + ',' + str(d[4]) + ',' + str(d[5]) + '\n')
                #print('Closed.. \n')
                dat = []
            f.close()
            launch_time = datetime.datetime.now()
            timestr = launch_time.strftime("%Y_%m_%d_%H_%M_%S")
            gpsPath = "/home/pi/infrasound/dataFiles/gpsData" + timestr + ".csv"
            f = open(gpsPath,'a+')
            print('NEW GPS FILE')
    except KeyboardInterrupt:
        f.close()
        print('\n Done Writing \n')
    except:
        print('ERROR')
        pass


if __name__ == '__main__':
    GPS()
