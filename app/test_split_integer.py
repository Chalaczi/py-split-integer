import pytest
from app import split_integer

@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (10, 3),
        (100, 10),
        (7, 5),
        (0, 1),
        (5, 5),
        (15, 4),
    ],
)
def test_sum_of_parts_equals_value(value, number_of_parts):
    parts = split_integer.split_integer(value, number_of_parts)
    assert sum(parts) == value, "Suma elementów powinna równać się wartości wejściowej"

@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (10, 3),
        (100, 10),
        (7, 5),
        (15, 4),
    ],
)
def test_parts_are_sorted(value, number_of_parts):
    parts = split_integer.split_integer(value, number_of_parts)
    assert parts == sorted(parts), "Lista powinna być posortowana rosnąco"

@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (10, 3),
        (100, 10),
        (7, 5),
        (15, 4),
    ],
)
def test_difference_max_min_is_at_most_one(value, number_of_parts):
    parts = split_integer.split_integer(value, number_of_parts)
    assert max(parts) - min(parts) <= 1, "Różnica między max a min nie powinna przekraczać 1"
