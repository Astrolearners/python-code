def gprmcConverter(nmea_string: str):
    fields = nmea_string.split(",")
    if fields[0] == "$GPRMC" and len(fields) >= 12:
        data = []

        # Get Time
        time = fields[1][:6] # Time in HHMMSS
        data.append(time)

        # Get Latitude
        days = float(fields[3][:2])
        minutes = float(fields[3][2:]) / 60.0
        latitude = days + minutes
        if fields[4] == "S":
            latitude = -latitude  # Southern hemisphere is represented by a negative value
        data.append(latitude)

        # Get Longtitude
        longitude = float(fields[5][:3]) + float(fields[5][3:]) / 60.0
        if fields[6] == "W":
            longitude = -longitude  # Western hemisphere is represented by a negative value
        data.append(longitude)

        # Get Speed in Knots
        speed = float(fields[7])
        data.append(speed)

        # Return the data list
        return data

    else:
        print("ERROR: Invalid or unsupported NMEA sentence")
        return ValueError
    
def gpggaConverter(nmea_string: str):
    fields = nmea_string.split(",")
    if fields[0] == "$GPGGA" and len(fields) >= 12:
        data = []

        # Get Time
        time = fields[1][:6]
        data.append(time)

        # Get Latitude
        days = float(fields[2][:2])
        minutes = float(fields[2][2:]) / 60.0
        latitude = days + minutes
        if fields[3] == "S":
            latitude = -latitude  # Southern hemisphere is represented by a negative value
        data.append(latitude)

        # Get Longtitude
        longitude = float(fields[4][:3]) + float(fields[4][3:]) / 60.0
        if fields[5] == "W":
            longitude = -longitude  # Western hemisphere is represented by a negative value
        data.append(longitude)

        # Get fix quality
        fix = fields[6]
        data.append(fix)

        # Get number of Satellites in view
        satellites = fields[7]
        data.append(satellites)

        # Get altitude
        altitude = fields[9]
        data.append(altitude)

        # Return data
        return data
    
    else:
        print("ERROR: Invalid or unsupported NMEA sentence")
        return ValueError
    
def test():
    print("TESTS: Testing Nmea Parser")
    print("TESTS: Testing GPRMC converter.")
    try:
        sample_response = ["134441", 38.03353833333333, 23.837116666666667, 0.0]
        sample_data = "$GPRMC,134441.000,A,3802.0123,N,02350.2270,E,0.00,243.39,071223,,,D*6C"
        if gprmc_converter(sample_data) == sample_response:
            print("TESTS: GPRMC converter OK.")
        else:
            print("TESTS: GPRMC converter ERROR.")
    except Exception as error:
        print("TESTS: Warning cannot call function! Check logs!")
        print(f"TESTS: GPRMC converter error logs: ${error}")
    print("TESTS: Testing GPGGA converter.")
    try:
        sample_response = ["134442", 38.03353833333333, 23.837116666666667, "2", "08", "233.8"]
        sample_data = "$GPGGA,134442.000,3802.0123,N,02350.2270,E,2,08,1.08,233.8,M,35.5,M,,*69"
        if gpgga_converter(sample_data) == sample_response:
            print("TESTS: GRGGA converter OK.")
        else:
            print("TESTS: GPGGA converter ERROR.")
    except Exception as error:
        print("TESTS: Warning cannot call function! Check logs!")
        print(f"TESTS: GPGGA converter error logs: ${error}")

test()