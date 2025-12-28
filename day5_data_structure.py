#Day 5 : Dictionary & Lists
#Purpose : represent and process structured data

from typing import Dict,Any,List

def create_user_profile(name: str, age: int) -> Dict[str, Any]:
    user = {
        "name": name,
        "age": age,
        "is_active": True
    }
    return user

def is_adult(user: Dict[str, Any]) -> bool:
    return user.get("age", 0) >= 18

def get_active_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    active_adults = []
    for user in users:
        if(user.get("is_active") and is_adult(user)):
            active_adults.append(user)
    return active_adults

# Simple Test
if __name__ == "__main__":
    users = [
        create_user_profile("Kevin", 30),
        create_user_profile("Bob", 15),
        create_user_profile("Charlie", 22),
        create_user_profile("Max", 17)
    ]
    users[1]["is_active"] = False  # Deactivate Bob

    active_adults = get_active_adults(users)
    for user in active_adults:
        print(f"Active Adult: {user['name']}, Age: {user['age']}")