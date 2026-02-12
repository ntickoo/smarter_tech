BULKY_VOL_THRESHOLD = 1000000
BULKY_DIM_THRESHOLD = 150
HEAVY_MASS_THRESHOLD = 20


def sort(width, height, length, mass):
    """
    - A package is bulky if its volume (Width x Height x Length)
    is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
    - A package is heavy when its mass is greater or equal to 20 kg.

    Returns

    STANDARD: standard packages (those that are not bulky or heavy) can be handled normally.
    SPECIAL: packages that are either heavy or bulky can't be handled automatically.
    REJECTED: packages that are both heavy and bulky are rejected.
    """

    less_than_zero = [d for d in [width, height, length, mass] if d < 0]
    if less_than_zero:
        raise ValueError(
            f"The arguments passed cannot be less than zero {less_than_zero}"
        )

    vol = width * length * height
    dimensions = [width, height, length]

    any_dimension_more_than_threshold = any(
        dim >= BULKY_DIM_THRESHOLD for dim in dimensions
    )

    is_bulky = (vol >= BULKY_VOL_THRESHOLD) or any_dimension_more_than_threshold
    is_heavy = mass >= HEAVY_MASS_THRESHOLD

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


def main():
    print(sort(100, 100, 100, 21), "Should Be REJECTED")
    print(sort(100, 100, 100, 10), "Should Be SPECIAL")
    print(sort(200, 1, 1, 10), "Should Be SPECIAL")
    print(sort(20, 1, 1, 20), "Should Be SPECIAL")
    print(sort(20, 1, 1, 2), "Should Be STANDARD")


if __name__ == "__main__":
    main()
