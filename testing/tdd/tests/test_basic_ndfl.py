# | **До 2,4 млн руб.** | 13% | 13% от дохода |
# | **2,4 – 5 млн руб.** | 15% | 312 000 + 15% с суммы превышения |
# | **5 – 20 млн руб.** | 18% | 702 000 + 18% с суммы превышения |
# | **20 – 50 млн руб.** | 20% | 3 402 000 + 20% с суммы превышения |
# | **Свыше 50 млн руб.** | 22% | 9 402 000 + 22% с сумм превышения |

# TODO make test to obey principles

#TODO fix pytest undefine

from ndfl import calculate_ndfl
import pytest

def test_ndfl_tier_1_basic():
    assert calculate_ndfl(2_000_000) == 260_000

def test_ndfl_tier_2_basic():
    #4_000_000 -> 2_400_000 * 0.13 + 1_6000_000
    assert calculate_ndfl(4_000_000) == 552_000

def test_ndfl_tier_3_basic():
    assert calculate_ndfl(10_000_000) == 1_602_000

def test_ndfl_tier_4_basic():
    assert calculate_ndfl(30_000_000) == 5_402_000

def test_ndfl_tier_5_basic():
    assert calculate_ndfl(60_000_000) == 11_602_000

@pytest.mark.xfail
def test_ndfl_fails_negative_income():
    calculate_ndfl(-1000)