bme_schema = {
    "temp": None,
    "humidity": None,
    "pressure": None,
    "gas": None
}

gps_schema = {
    "latitude": None,
    "longitude": None,
    "altitude": None
}

accelerometer_schema = {
    "accelerometer": {
        "X": None,
        "Y": None,
        "Z": None,
    },
    "magnetometer": {
        "X": None,
        "Y": None,
        "Z": None,
    }
}

main_schema = {
    "time": None,
    "bme": bme_schema,
    "gps": gps_schema,
    "accelerometer": accelerometer_schema,
    "rpi_temp": None
}

dataframe_schema = {
    "time": None,
    "temp": None,
    "humidity": None,
    "pressure": None,
    "gas": None,
    "latitude": None,
    "longitude": None,
    "altitude": None,
    "accelerometer-X": None,
    "accelerometer-Y": None,
    "accelerometer-Z": None,
    "magnetometer-X": None,
    "magnetometer-Y": None,
    "magnetometer-Z": None,
    "rpi_temp": None
}