# Day 4 : Functions & Control Flow
# Purpose : write clean logic that can become backend services

def is_valid_age(age: int) -> bool:
    if age < 0:
        return False
    if age < 18:
        return False
    return True

def get_user_status(age: int) -> str:
    if not is_valid_age(age):
        return "Invalid"
    return "Adult"

# Simple Test
if __name__ == "__main__":
    ages = [25,16,-1]

    for age in ages:
        status = get_user_status(age)
        print(f"Age {age}: {status}")