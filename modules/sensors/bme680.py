def get_temp():
    print("Get temp function.")
    return "OK"

def get_humdity():
    print("Get humdity fucntion.")
    return "OK"

def get_pressure():
    print("Get pressure function.")
    return "OK"

def test():
    print("TESTS: Testing humidity, pressure and temp readings.")
    try:
        print(get_temp())
        print("TESTS: Humidity OK.")
    except:
        print("TESTS: Humidity ERROR.")
    try:
        print(get_humdity())
        print("TESTS: Temp OK.")
    except:
        print("TESTS: Temp ERROR.")
    try:
        print(get_pressure())
        print("TESTS: Pressure OK.")
    except:
        print("TESTS: Pressure ERROR.")