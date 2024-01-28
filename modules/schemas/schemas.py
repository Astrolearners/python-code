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

main_schema = {
    "time": None,
    "bme": bme_schema,
    "gps": gps_schema,
    "rpi_temp": None
}