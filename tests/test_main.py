from simple_calculator.main import SimpleCalculator

def test_add_two_numbers():
    # setup
    calculator = SimpleCalculator()

    # act
    result = calculator.add(4, 5)

    # assert
    assert result == 9


def test_add_three_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4, 5, 11)

    assert result == 20

def test_add_many_numbers():
    numbers = range(100)
    calculator = SimpleCalculator()

    result = calculator.add(*numbers)

    assert result == 4950

def test_subtract_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.subtract(5, 3)

    assert result == 2