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
        save_folder = "save"
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
