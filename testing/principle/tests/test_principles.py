
#TODO make it with pip install -e .
# in project root_dir after setup.py defined


# Раннее тестирование позволяет сэкономить время позднее
# Тесты показывают наличие ошибок, а не отсутсвие

# Тесты не должны дублировать логику тестируемого кода
# и делать предположений о внутреннем устройстве кода

# Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты должны покрывать "кластеры" входных параметров
# Тесты должны обнаруживать новые ошибки (pescicide paradox)
# Тесты покрывают как успешные, так и ошибочные кейсы

from math_demo import add, add_with_bug


def test_addition():
    assert add(2,2) == 4
    assert add(0,0) == 0
    assert add(7,6) == 13
    print("Test addition passed")


def test_addition_with_bug():
    assert add_with_bug(2,2) == 4
    assert add_with_bug(0,0) == 0
    assert add_with_bug(7,6) == 13
    print("Test bugged addition passed")


def test_addition_dublicate():
    assert add(6,7) == 6 + 7
    print("Test duplicate addition passed")


def test_addition_overkill():
    for i in range(2**32):
        for j in range(2**32):
            assert add(i,j) == i + j # violation of duplication
            assert add(-i,j) == -i + j
            assert add(i,-j) == i - j
            assert add(-i,-j) == -i - j
    print("Test overkill passed")

if __name__ == "__main__":
    test_addition()
    #test_addition_with_bug()
    test_addition_dublicate()
    test_addition_overkill()