bme_schema = {
    "temp": None,
    "humidity": None,
    "pressure": None,
    "gas": None
}

gps_schema =  {
    "latitude": None,
    "longitude": None,
    "altitude": None,
    "speed": None,
    "satellites": None,
    "fixQuality": None
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
