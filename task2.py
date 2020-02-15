def square_number(number):
    number **= 2
    return number
square_number(2)

def test_square_number():
    assert square_number(2) == 4
    assert square_number(8) == 64
    assert square_number(10) == 100
    print("YOUR CODE IS CORRECT!")

test_square_number()