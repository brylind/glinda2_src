# script to just test the clock on the gps and how to update it properly

def GPS_clock_update():
    from time import sleep, time
    import adafruit_gps                             
    import datetime
    import board
    import busio
    import socket
    import serial
    from threading import Event
    import urllib.request
    # uart = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=10)
    uart = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1000)
    
    gps = adafruit_gps.GPS(uart, debug=False) # Use UART/pyserial
    # Turn on the basic GGA and RMC info (what you typically want)
    # gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

    # get only GGA data
    gps.send_command(b'PMTK314,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')d

    # get all data
    # gps.send_command(b"PMTK314,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0")

    # Set update rate to once a second (1hz) which is what you typically want.
    gps.send_command(b'PMTK220, 2000')
    # launch_time = datetime.datetime.now()
    # f = open(gpsPath,'a+')
    dat = []
  



    try:
        urllib.request.urlopen('http://google.com', None, timeout=5)
        internet = ''
    except:
        internet = 'NOINT_'    

    k=2
    try:
        while k>1:
            for i in range(30):
                gps.update()
                if gps.has_fix:     #gps fix: 0=no, 1=yes, 2=differential fix
                    if internet == '':

                        ## this does something
                        # gps_currenttime = str(gps.datetime)
                        # print(f'Type: {type(gps_currenttime)} \n Value: {gps_currenttime}')
                        # a = 'imastring'
                        # print(f'###### \n Normal string type is: {type(a)} \n ######### \n')

                        #print(f'gps.Datetime type is {type(gps_currenttime)} and the \n'
                        #f'value is : {gps_currenttime}')        


                        #sentence = gps.readline()    ## this also shows a changing epoch times
                        # raw = gps.nmea_sentence
                        # print(f'Raw sentence type: {type(raw)} \n' 
                        # f'Value: {raw}'
                        # )
                        #     gps.timestamp_utc.tm_hour,\

                        # print('starting gps timestamp block')
                        # print(f'GPS timstamp year: {gps.timestamp_utc.tm_year}')
                        # print(f'GPS timstamp month: {gps.timestamp_utc.tm_mon}')
                        # print(f'GPS timstamp day: {gps.timestamp_utc.tm_mday}')
                        gps.update()
                        gps_time = (f'{gps.timestamp_utc.tm_hour}_{gps.timestamp_utc.tm_min}_{gps.timestamp_utc.tm_sec}')
                        print(gps_time)

                        # gps_time = datetime.datetime(gps.timestamp_utc.tm_year,
                        #     gps.timestamp_utc.tm_mon,
                        #     gps.timestamp_utc.tm_mday,
                        #     gps.timestamp_utc.tm_hour,
                        #     gps.timestamp_utc.tm_min,
                        #     gps.timestamp_utc.tm_sec)  
                        #print(f'GPS datetime: {gps_time}')       # turns out this gets the time at the moment the gps fixed
                        # delta_t = (datetime.datetime.utcnow()-gps_time).total_seconds()
                        # print(f'System time: {datetime.datetime.utcnow()}')
                        # print(f'GPS timestamp: {gps_time}')
                        # print(f'The time difference between GPS/System: {delta_t}')
                    
                        #dat.append([time(), gps.latitude, gps.longitude, gps.speed_knots, gps.fix_quality, gps.satellites, 'good_int'])
                    else:
                        #dat.append([time(), gps.latitude, gps.longitude, gps.speed_knots, gps.fix_quality, gps.satellites, [gps_currenttime]])
                        print('No internet')
                else:
                    print('Waiting for GPS fix...')
                sleep(1)
                # sleep(5)    # this has to be the same as the update rate above (in the send command line)
                #print('Writing... \n')
                # gps.update()
                # if gps.has_fix:

                #     # print(gps.hour) # this doesn't work but something simular to this is needed. Its gotta be in there somewhere.
                # else:
                #     delta_t = 'N/A'
                # print('Delta_t_sys_minus_gps_at_write' + ',' + str(delta_t) + '\n')
                # print('Time_s' + ',' + 'Latitude' + ',' + 'Longitude' + ',' + 'Speed_kts' + ',' + 'GPS_fix' + ',' + 'Satellites' + '\n')
                # print(dat)

                # # f.write('Delta_t_sys_minus_gps_at_write' + ',' + str(delta_t) + '\n')
                # # f.write('Time_s' + ',' + 'Latitude' + ',' + 'Longitude' + ',' + 'Speed_kts' + ',' + 'GPS_fix' + ',' + 'Satellites' + '\n')
            k=0              
        # for d in dat:
        #     print(str(d[0]) + ',' + str(d[1]) + ',' + str(d[2]) + ',' + str(d[3]) + ',' + str(d[4]) + ',' + str(d[5]) + ',' + str(d[6]) + '\n')
        # print('Closed.. \n')
                # dat = []
                # # f.close()
                # launch_time = datetime.datetime.now()
                # timestr = launch_time.strftime("%Y_%m_%d_%H_%M_%S")
                # gpsPath = f'/home/pi/glinda_main/dataFiles/gps/{device_hostname}_gpsData_{timestr}.csv'
                # print('NEW GPS FILE')
    except KeyboardInterrupt:
        # f.close()
        print('\n Done Writing \n')
        quit()
    
    except:
        print('ERROR')
        pass


if __name__ == '__main__':
    GPS_clock_update()
