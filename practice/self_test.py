# =========================
# Imports
# =========================
import json

# =========================
# Configuration
# =========================
DB_FILE = "users.json"

# =========================
# Business Logic
# =========================
def create_user(users: dict, username: str, password: str) -> tuple[bool, str]:
    username = username.strip().lower()
    password = password.strip()

    if not username:
        return False, "Username cannot be empty."
    if username in users:
        return False, "Username already exists."
    if len(password) < 8:
        return False, "Password too short (min 8 chars)."

    users[username] = {"password": password, "failed_attempts": 0}
    return True, "Registration successful."

def register_cli(users: dict) -> None:
    username = input("New username: ")
    password = input("New password (min 8 chars): ")

    ok, msg = create_user(users, username, password)
    print(msg)

def authenticate_user(users: dict, username: str, password: str) -> tuple[bool, str]:
    username = username.strip().lower()
    password = password.strip()

    user = users.get(username)
    if not user:
        return False, "Invalid username or password."

    if user["failed_attempts"] >= 3:
        return False, "Account locked due to too many failed attempts."

    if user["password"] == password:
        user["failed_attempts"] = 0
        return True, "Login successful."
    else:
        user["failed_attempts"] += 1
        return False, "Invalid username or password."
    
def login_cli(users: dict) -> None:
    username = input("Username: ")
    password = input("Password: ")

    ok, msg = authenticate_user(users, username, password)
    print(msg)



def save_data(filename: str,data: dict) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_data(filename: str) -> dict:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def main(DB_FILE :str) -> None:
    users = load_data(DB_FILE)

    while True:
        print("\n1) Register\n2) Login\n3) Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            register_cli(users)
            save_data(DB_FILE, users)
        elif choice == "2":
            login_cli(users)
            save_data(DB_FILE, users)
        elif choice == "3":
            save_data(DB_FILE, users)
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main(DB_FILE)

