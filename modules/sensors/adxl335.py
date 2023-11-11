def read_data():
    print("Reading accelerometer status.")
    return "OK"

def test():
    print("TESTS: Reading accelerometer data.")
    try:
        print(read_data())
        print("TESTS: Accelerometer OK.")
    except:
        print("TESTS: Accelerometer ERROR.")