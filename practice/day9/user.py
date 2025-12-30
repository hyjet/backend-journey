def is_active(user: dict[str, object]) -> bool:
    return bool(user.get("is_active", False))

def get_full_name(user: dict[str, object]) -> str:
    first_name = user.get("first_name", "")
    last_name = user.get("last_name", "")
    return f"{first_name} {last_name}".strip()

