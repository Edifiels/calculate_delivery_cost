import pytest

from delivery_calculator import calculate_delivery_cost

def test_minimum_cost():
    assert calculate_delivery_cost(1, "small", False, "normal") == 400

def test_fragile_long_distance():
    with pytest.raises(ValueError):
        calculate_delivery_cost(31, "small", True, "normal")

def test_distance_tiers():
    assert calculate_delivery_cost(1, "small", False, "normal") == 400
    assert calculate_delivery_cost(5, "small", False, "normal") == 400
    assert calculate_delivery_cost(15, "small", False, "normal") == 400
    assert calculate_delivery_cost(35, "small", False, "normal") == 400

def test_size_impact():
    small_cost = calculate_delivery_cost(35, "small", False, "normal")
    big_cost = calculate_delivery_cost(35, "big", False, "normal")
    assert big_cost - small_cost == 100

def test_fragile_impact():
    non_fragile = calculate_delivery_cost(15, "small", False, "normal")
    fragile = calculate_delivery_cost(15, "small", True, "normal")
    assert fragile - non_fragile == 200

def test_load_factors():
    base_cost = calculate_delivery_cost(35, "big", False, "normal")
    assert calculate_delivery_cost(35, "big", False, "very_high") == int(base_cost * 1.6)
    assert calculate_delivery_cost(35, "big", False, "high") == int(base_cost * 1.4)
    assert calculate_delivery_cost(35, "big", False, "above_average") == int(base_cost * 1.2)
