"""
Day 2 (Upgraded)
Backend-style Python Basics
"""

# --- 1. Variable & Type ---
name: str = "Kevin"
age: int = 25
height: float = 179.5
is_active: bool = True


# --- 2. Function with clear responsibilities ---
def get_user_profile(name: str, age: int, height: float, is_active: bool) -> dict:
    """
    Returns user profile datain dictionary form.
    Backend-friendly Structure.
    """
    return {"name": name, "age": age, "height": height, "is_active": is_active}


# --- 3. Function with simple validation ---
def is_adult(age: int) -> bool:
    """
    Check if the user is an adult.
    """
    return age >= 18

# --- 4. Execution (like a main flow) ---
profile = get_user_profile(name, age, height, is_active)
adult_status = is_adult(age)

print("User Profile:", profile)
print("Is Adult:", adult_status)