from user import is_active, get_full_name
from utils import calculate_discount

def main() -> None:
    user ={
        "first_name": "Kevin",
        "last_name" : "Li",
        "is_active" : True
    }

    print(get_full_name(user))
    print("Is user active?", is_active(user))
    print("Price: ", calculate_discount(150))

if __name__ == "__main__":
    main()