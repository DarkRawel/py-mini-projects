import json
import os
from cryptography.fernet import Fernet

class Person:
    def __init__(self, name, age, gmail, password):
        self.name = name
        self.age = age
        self.gmail = gmail
        self.password = password

    def save(self):
        save_folder = os.path.join("password_manager", "save")
        os.makedirs(save_folder, exist_ok=True)

        key_path = os.path.join(save_folder, f"{self.name}_secret.key")
        data_path = os.path.join(save_folder, f"{self.name}_data.json.enc")

        key = Fernet.generate_key()
        fernet = Fernet(key)

        with open(key_path, "wb") as key_file:
            key_file.write(key)

        data = {
            "name": self.name,
            "age": self.age,
            "gmail": self.gmail,
            "password": self.password
        }

        json_data = json.dumps(data).encode()
        encrypted = fernet.encrypt(json_data)

        with open(data_path, "wb") as file:
            file.write(encrypted)

        print(f"Encrypted data saved to {data_path}")

def load_person(name):
    save_folder = os.path.join("password_manager", "save")
    key_path = os.path.join(save_folder, f"{name}_secret.key")
    data_path = os.path.join(save_folder, f"{name}_data.json.enc")

    with open(key_path, "rb") as key_file:
        key = key_file.read()

    fernet = Fernet(key)

    with open(data_path, "rb") as file:
        encrypted = file.read()

    decrypted = fernet.decrypt(encrypted)
    data = json.loads(decrypted.decode())

    return Person(**data)

def main():
    print("\nHello and welcome to password manager!")

    while True:
        print("\n1. Load file")
        print("2. Save file")
        try:
            user_input = int(input("Enter choice 1 or 2: "))
        except ValueError:
            print("Please enter a valid number (1 or 2).")
            continue

        if user_input == 1:
            name = input("\nEnter your name: ")
            try:
                loaded_person = load_person(name)
                print(f"Loaded person: {loaded_person.name}, {loaded_person.age}, {loaded_person.gmail}, {loaded_person.password}")
            except FileNotFoundError:
                print(f"No saved data found for '{name}'.")
            break

        elif user_input == 2:
            while True:
                name = input("\nEnter your name: ")

                while True:
                    try:
                        age = int(input("Enter your age: "))
                        break
                    except ValueError:
                        print("Please enter a valid number for age.")

                while True:
                    gmail = input("Enter your gmail: ")
                    if "@" in gmail and "." in gmail:
                        break
                    else:
                        print("Invalid email format. Please include '@' and '.'")

                password = input("Enter your password: ")

                person = Person(name, age, gmail, password)
                person.save()

                cont = input("Save another? (y/n): ").lower()
                if cont != 'y':
                    break
            break

        else:
            print("Please enter 1 or 2.")

if __name__ == "__main__":
    main()
