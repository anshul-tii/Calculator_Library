import Calculator

class Test_Calculator:
    def test_addition(self):
        assert Calculator.add(2,2) ==4

    def test_substraction(self):
        assert Calculator.substract(4,3)==1
