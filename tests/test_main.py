import pytest
from main import sort


@pytest.mark.parametrize(
    ("width", "height", "length", "mass", "expected"),
    [
        pytest.param(
            100, 100, 100, 10, "SPECIAL", id="volume_equals_bulky_threshold_is_special"
        ),
        pytest.param(
            100,
            100,
            101,
            10,
            "SPECIAL",
            id="volume_more_than_bulky_threshold_is_special",
        ),
        pytest.param(
            150, 1, 1, 10, "SPECIAL", id="dimension_equals_bulky_threshold_is_special"
        ),
        pytest.param(
            151,
            151,
            151,
            10,
            "SPECIAL",
            id="dimension_and_volume_more_than_bulky_threshold_is_special",
        ),
        pytest.param(
            151,
            1,
            1,
            10,
            "SPECIAL",
            id="dimension_more_than_bulky_threshold_is_special",
        ),
        pytest.param(
            1, 1, 1, 20, "SPECIAL", id="mass_equals_bulky_threshold_is_special"
        ),
        pytest.param(
            1, 1, 1, 21, "SPECIAL", id="mass_more_than_bulky_threshold_is_special"
        ),
        pytest.param(
            150,
            1,
            1,
            20,
            "REJECTED",
            id="dimension_and_mass_equals_bulky_threshold_is_rejected",
        ),
        pytest.param(
            100,
            100,
            100,
            20,
            "REJECTED",
            id="volume_and_mass_equals_bulky_threshold_is_rejected",
        ),
        pytest.param(
            100,
            100,
            101,
            21,
            "REJECTED",
            id="volume_and_mass_more_than_bulky_threshold_is_rejected",
        ),
        pytest.param(
            100,
            100,
            10,
            19,
            "STANDARD",
            id="dimension_and_volume_mass_less_than_threshold_is_standard",
        ),
        pytest.param(
            0, 0, 0, 0, "STANDARD", id="sort_volume_and_mass_all_zero_is_standard"
        ),
    ],
)
def test_sort(width, height, length, mass, expected):
    package_type = sort(width=width, height=height, length=length, mass=mass)
    assert package_type == expected


def test_sort_negative_values_should_raise_exception():
    with pytest.raises(ValueError):
        sort(-1, 1, 1, 1)

    with pytest.raises(ValueError):
        sort(1, 1, 1, -1)

    with pytest.raises(ValueError):
        sort(-10, -11, -11, -1)
