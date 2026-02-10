from script import sum ,divide
def test_sum():
    a = 1
    b = 2
    result = 3
    assert sum(a,b) == result

def test_divide():
    a = 2
    b = 4
    result = 0.5
    assert divide(a,b) == result

def test_divide_prohibited():
    try:
        devide([1,2,3],[4,5,6])
	print("Test list-divison passed")
	assert False


def test_divide_zero():
    a = 2
    b = 0
    try:
        divide(a,b)
        assert False
    except ValueError as e:
        print("Good")

if __name__ == "main":
    test_sum()
    test_divide()
    test_divide_zero()
