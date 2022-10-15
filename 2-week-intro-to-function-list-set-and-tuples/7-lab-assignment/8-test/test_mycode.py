from my_code import make_upper,make_lower,make_capital

nam = "my nAme is mosTafizur"

def test_script():
    test_upper = make_upper(nam)
    test_lower = make_lower(nam)
    test_capital = make_capital(nam)
    # print(test_upper, test_lower, test_capital)


    assert "MY NAME IS MOSTAFIZUR" == test_upper and  "my name is mostafizur" == test_lower and  "My name is mostafizur" == test_capital

    assert test_upper == nam.upper() and test_lower == nam.lower() and test_capital == nam.capitalize()





