# Day 6 : Error handling & defensive coding
# Purpose : prevent crashes from bad data

from typing import Dict, Any


def get_user_age(user: Dict[str, Any]) -> int:
    try:
        age = user["age"]

        if not isinstance(age, int):
            raise ValueError("Age must be an integer")
        if age < 0:
            raise ValueError("Age cannot be negative")
        return age
    except KeyError:
        raise KeyError("User data must contain 'age' field")

def is_adult(user: Dict[str, Any]) -> bool:
    age = get_user_age(user)
    return age >= 18

# Simple Test
if __name__ == "__main__":
    test_users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": -5},
        {"name": "Charlie", "age": "twenty"},
        {"name": "David"}  # Missing age
    ]

    for user in test_users:
        try:
            print(user["name"], "is adult:", is_adult(user))
        except Exception as e:
            print(f"Error processing user {user.get('name', 'Unknown')}: {e}")
