# Day 8 : Return instead of print in functions
# Purpose : functions should return values for better reusability

from typing import Any

def calculate_discounted_price(price: float) -> float:
    if price >100 :
        return price * 0.9  # 10% discount
    return price

def is_user_active(user: dict[str,Any]) -> bool:
    return user.get("is_active", False)

def get_full_name(user: dict[str,Any]) -> str:
    first_name = user.get("first_name", "")
    last_name = user.get("last_name", "")
    return f"{first_name} {last_name}".strip()

#Simple Test
if __name__ == "__main__":
    # Test calculate_discounted_price
    user = {"first_name" : "Kevin", "last_name" : "Li", "is_active" : True}

    print(calculate_discounted_price(120))
    print(is_user_active(user))
    print(get_full_name(user))
    
