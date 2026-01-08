from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


# -------------------------
# Part A — Functions
# -------------------------

def is_even(n: int) -> bool:
    """Return True if n is even."""
    return n % 2 == 0


def sum_list(nums: list[int]) -> int:
    """Return the sum of a list of integers."""
    return sum(nums)


def safe_div(a: float, b: float) -> Optional[float]:
    """
    Return a/b.
    If b == 0, return None (do not raise).
    """
    if b == 0:
        return None
    return a / b

def fizzbuzz(n: int) -> list[object]:
    """
    Return a list from 1..n where:
    - 'FizzBuzz' for multiples of 15
    - 'Fizz' for multiples of 3
    - 'Buzz' for multiples of 5
    - the number otherwise
    """
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result


def count_words(text: str) -> dict[str, int]:
    """
    Count words in text (case-insensitive).
    Treat punctuation as separators (simple approach is fine).
    Example: "Hi, hi!" -> {"hi": 2}
    """
    text = text.lower()
    results = {}
    for ch in '.,!?;:"()[]{}<>\\/|`~@#$%^&*-_=+':
        text = text.replace(ch, " ")
    words = text.split()
    for word in words:
        results[word] = results.get(word, 0) + 1
    return results

def top_n_words(counts: dict[str, int], n: int = 3) -> list[tuple[str, int]]:
    """
    Return top n words sorted by:
    - highest count first
    - then alphabetical for ties
    """
    result = counts.items()
    result = sorted(result, key=lambda item: (-item[1], item[0]))
    return result[:n]


# -------------------------
# Part B — Error handling
# -------------------------

def parse_int_list(csv: str) -> list[int]:
    """
    Convert a comma-separated string into list[int].
    Example: "1,2, 3" -> [1,2,3]
    If any item is not a valid int, raise ValueError with a helpful message.
    """
    # TODO
    raise NotImplementedError


# -------------------------
# Part C — Class
# -------------------------

@dataclass
class BankAccount:
    owner: str
    balance: int = 0

    def deposit(self, amount: int) -> None:
        """Deposit amount. amount must be > 0."""
        # TODO
        raise NotImplementedError

    def withdraw(self, amount: int) -> None:
        """
        Withdraw amount.
        - amount must be > 0
        - cannot withdraw more than balance
        """
        # TODO
        raise NotImplementedError


# -------------------------
# Part D — Quick tests (no pytest)
# -------------------------

def run_tests() -> None:
    # Functions
    assert is_even(2) is True
    assert is_even(3) is False

    assert sum_list([1, 2, 3]) == 6
    assert sum_list([]) == 0

    assert safe_div(10, 2) == 5
    assert safe_div(10, 0) is None

    assert fizzbuzz(5) == [1, 2, "Fizz", 4, "Buzz"]
    assert fizzbuzz(15)[-1] == "FizzBuzz"

    counts = count_words("Hi, hi! This is a test. A TEST.")
    assert counts["hi"] == 2
    assert counts["test"] == 2
    assert counts["a"] == 2

    top3 = top_n_words(counts, 3)
    assert top3[0][1] >= top3[1][1] >= top3[2][1]

    # Error handling
    assert parse_int_list("1,2, 3") == [1, 2, 3]
    try:
        parse_int_list("1, x, 3")
        raise AssertionError("Expected ValueError for invalid int")
    except ValueError:
        pass

    # Class
    acc = BankAccount("Kevin", 100)
    acc.deposit(50)
    assert acc.balance == 150

    acc.withdraw(25)
    assert acc.balance == 125

    try:
        acc.withdraw(1000)
        raise AssertionError("Expected ValueError for insufficient funds")
    except ValueError:
        pass

    print("✅ All tests passed!")


if __name__ == "__main__":
    run_tests()
