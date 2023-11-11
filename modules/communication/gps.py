def get_location():
    print("Getting location.")
    return "OK"

def test():
    print("TESTS: Getting gps location.")
    try:
        print(get_location())
        print("TESTS: GPS OK.")
    except:
        print("TESTS: GPS ERROR.")