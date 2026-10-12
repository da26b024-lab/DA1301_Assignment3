from typing import List


def surviving_ships(ships: List[int]) -> List[int]:
    """
    Problem 2: Spaceship collisions.

    Given a list of ship engine powers (sign = direction: positive is
    right, negative is left), resolve all collisions between ships
    moving toward each other and return the engine powers (with sign)
    of the ships that remain.

    Args:
        ships: list of signed engine powers.

    Returns:
        List of signed engine powers of surviving ships, left to right.
    """
    stack = []
    for ship in ships:
        while stack and ship < 0 < stack[-1]:
            if abs(ship) > abs(stack[-1]):
                stack.pop()
                continue
            elif abs(ship) == abs(stack[-1]):
                stack.pop()
            break
        else:
            stack.append(ship)
    return stack


if __name__ == "__main__":
    # Example sanity checks (see test.py for the real test cases)
    print(surviving_ships([6, 3, -5]))  # expected: [6]
    print(surviving_ships([8, -8]))     # expected: []
