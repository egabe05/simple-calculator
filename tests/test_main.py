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


# is this test enough to verify substract works??
# answer: like I mentioned to only write enough code that the test passes they also recommend in the blog to not be
# dumb and only implment what the assertion asks for (example: here I returend 2 in the method instead of actually
# doing the subtraction)  IMO a good balance to this is to parameterize the test to verify everything works with 2 
# different scenarios
# TODO: parameterize me to also subtract 9, 3
def test_subtract_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.subtract(5, 3)

    assert result == 2

# TODO: requirement: multiply two numbers
def test_mul_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.multiply(6, 4)

    assert result == 24

# TODO: requirement: multiply many numbers
