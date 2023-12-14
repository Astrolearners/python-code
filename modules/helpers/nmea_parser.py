def gprmc_converter(nmea_string: str):
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
        if fields[4] == 'S':
            latitude = -latitude  # Southern hemisphere is represented by a negative value
        data.append(latitude)

        # Get Longtitude
        longitude = float(fields[5][:3]) + float(fields[5][3:]) / 60.0
        if fields[6] == 'W':
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
    
def test():
    print("TESTS: Testing Nmea Parser")
    print("TESTS: Testing GPRMC converter.")
    try:
        sample_response = ['134441', 38.03353833333333, 23.837116666666667, 0.0]
        sample_data = "$GPRMC,134441.000,A,3802.0123,N,02350.2270,E,0.00,243.39,071223,,,D*6C"
        if gprmc_converter(sample_data) == sample_response:
            print("TESTS: GRMC converter OK.")
        else:
            print("TESTS: GRMC converter ERROR.")
    except Exception as error:
        print("TESTS: Warning cannot call function! Check logs!")
        print(f"TESTS: GPRMC converter error logs: ${error}")