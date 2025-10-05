"""
sorter.py

A simple package sorting program for Thoughtful’s robotic automation factory.

Each package is dispatched into one of three stacks:
- STANDARD: Not bulky and not heavy
- SPECIAL: Bulky or heavy (but not both)
- REJECTED: Both bulky and heavy
"""

def sort(width, height, length, mass):
    """
    Determines which stack a package should be dispatched to.

    Args:
        width (float or int): Width of the package in centimeters.
        height (float or int): Height of the package in centimeters.
        length (float or int): Length of the package in centimeters.
        mass (float or int): Mass of the package in kilograms.

    Returns:
        str: One of "STANDARD", "SPECIAL", or "REJECTED".
    """

    # Calculate the volume in cubic centimeters
    volume = width * height * length

    # Check bulky criteria
    is_bulky = (
        volume >= 1_000_000
        or width >= 150
        or height >= 150
        or length >= 150
    )

    # Check heavy criteria
    is_heavy = mass >= 20

    # Determine stack
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


if __name__ == "__main__":
    # Example runs
    examples = [
        (100, 100, 100, 10),
        (200, 50, 40, 10),
        (50, 50, 50, 25),
        (200, 200, 200, 25),
    ]

    for w, h, l, m in examples:
        result = sort(w, h, l, m)
        print(f"Package ({w}x{h}x{l} cm, {m} kg): {result}")
