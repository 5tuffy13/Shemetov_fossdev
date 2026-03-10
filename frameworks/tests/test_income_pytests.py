import pytest 

from src_tax import calculate_tax

def test_income(self):
    assert calculate_tax(100) == 13.0
    
def test_integers_cents(self):
    assert calculate_tax(10.5) == 1.36


@pytest.mark.parametrize("income", "expected", [
      
    (100,13.0),
    (10.5, 1.36),
      
])

def test_calculate_tax_parametrized(
      income, expected
):
        assert calculate_tax(income) == expected