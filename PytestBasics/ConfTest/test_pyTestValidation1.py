

def test_validation1(setup_session,setup_module,setup_function):
    print("Executing test validation1")
    assert True

def test_validation2(setup_session,setup_module,setup_function):
    print("Executing test validation2")
    assert True

class TestValidationClass:
    def test_validation3(self, setup_class):
        print("Executing test validation3")
        assert True

    def test_validation4(self, setup_class):
        print("Executing test validation4")
        assert True
