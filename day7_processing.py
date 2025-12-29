# Day 7 : Processing collection safely
# Purpose : handle lists of data like real backend services

from typing import Dict, Any, List

def validate_user(user: Dict[str, Any]) -> None:
    if "age" not in user:
        raise KeyError("User missing age")
    
    if not isinstance(user["age"], int):
        raise ValueError("Age must be an integer")
    
    if user["age"] < 0:
        raise ValueError("Age cannot be negative")
    
def is_adult(user: Dict[str, Any]) -> bool:
    return user["age"] >= 18


def get_adult_users(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    adult_users = []
    for user in users:
        try:
            validate_user(user)
            if is_adult(user):
                adult_users.append(user)
        except Exception:
            # Skip invalid user
            continue
    return adult_users

# Simple Test
if __name__ == "__main__":
    test_users = [
        {"name": "Kevin", "age": 30},
        {"name": "Bob", "age": 15},
        {"name": "Charlie", "age": -5},  # Invalid age
        {"name": "Max", "age": "eighteen"},  # Invalid type
        {"name": "Alice"}  # Missing age
    ]

    result = get_adult_users(test_users)
    for user in result:
        print(f"Adult User: {user['name']}, Age: {user['age']}")