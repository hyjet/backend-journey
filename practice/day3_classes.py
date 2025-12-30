# Day 3: Classes (Backend-style Python)
#  Purpose: prepare for data models & services

class Users:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def is_adult(self) -> bool:
        """
        Check if the user is an adult.
        """
        return self.age >= 18
if __name__ == "__main__":
    user1 = Users("Kevin", 25)
    user2 = Users("ALex", 17)

    print(f"User: {user1.name}, Age: {user1.age}, Is Adult: {user1.is_adult()}")
    print(f"User: {user2.name}, Age: {user2.age}, Is Adult: {user2.is_adult()}")
        
                      