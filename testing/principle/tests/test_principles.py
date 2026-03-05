
#TODO make it with pip install -e .
# in project root_dir after setup.py defined


# Раннее тестирование позволяет сэкономить время позднее
# Тесты показывают наличие ошибок, а не отсутсвие

# Тесты не должны дублировать логику тестируемого кода
# и делать предположений о внутреннем устройстве кода

# Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты должны покрывать "кластеры" входных параметров
# Тестовые функции должны тестировать логические блоки

# Тесты должны обнаруживать новые ошибки, использование
# одних и тех же типов может препятствовать этому (pescicide paradox)

# Тесты покрывают как успешные, так и ошибочные кейсы

from math_demo import add, add_with_bug, calculate_tax_bug, calculate_tax


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


def test_addition_clusters():
    assert add(7,6) == 13
    assert add(0,6) == 6
    assert add(0,0) == 0
    assert add(-70,60) == -10
    assert add(-60,70) == 10
    assert add(-60,0) == -60
    assert add(0,-1100) == -1100
    print("test clusters passed")


def test_addition_commutativity():
    assert add(7,6) == 13
    assert add(6,7) == 13
    print("Test commutativity passed")


# def test_tax_calculator():
#     assert calculate_tax_bug(1000) == 150
#     assert calculate_tax_bug(100) == 15
#     assert calculate_tax_bug(10) == 1.5
#     assert calculate_tax_bug(1) == 0.15
#     assert calculate_tax_bug(234) == 35.1
#     print("Test tax calculator passed")
#     assert calculate_tax_bug(2.34) == 0.35 # 0.351


def test_tax_calculator():
    assert calculate_tax(1000) == 150
    assert calculate_tax(100) == 15
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(234) == 35.1
    print("Test tax calculator passed")
    assert calculate_tax    (2.34) == 0.35 # 0.351

def test_negative_income():
    try:
        calculate_tax(-100)
    except ValueError as e:
        print("Test negative income error passed")



if __name__ == "__main__":
    test_addition()
    #test_addition_with_bug()
    test_addition_dublicate()
    # test_addition_overkill()
    test_addition_clusters()
    test_addition_commutativity()
    test_tax_calculator()