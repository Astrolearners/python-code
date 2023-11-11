def buzz():
    print("Buzzing buzzer...")
    return "OK"

def test():
    print("TESTS: Bipping buzzer.")
    try:
        print(buzz())
        print("TESTS: Buzzer OK.")
    except:
        print("TESTS: Buzzer ERROR.")