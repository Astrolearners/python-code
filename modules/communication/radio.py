def send():
    print("Sending...")
    return "OK"

def receive():
    print("Receiving...")
    return "OK"

def test():
    print("TESTS: Running radio send and receive functions.")
    example_data = "hello"
    try:
        print(receive())
        print("TESTS: Receive OK.")
    except:
        print("TESTS: Receiver ERROR.")
    try:
        print(send(example_data))
        print("TESTS: Send OK.")
    except:
        print("TESTS: Send ERROR.")