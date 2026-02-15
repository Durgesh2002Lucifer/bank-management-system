import json
import random
import string
from pathlib import Path


class Bank:
    def __init__(self):
        self.database = Path(__file__).parent / "data.json"
        self.data = self.load_data()

    def load_data(self):
        if self.database.exists():
            with open(self.database, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_data(self):
        with open(self.database, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def generate_account_number(self):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        special = random.choices("@#$%^&*?", k=1)

        acc = alpha + num + special
        random.shuffle(acc)
        return "".join(acc)

    def create_account(self, name, age, pin, email):
        if age < 18 or len(str(pin)) != 4:
            return "Invalid Age or PIN"

        new_user = {
            "Name": name,
            "Age": age,
            "Pin": pin,
            "Email": email,
            "Account_No.": self.generate_account_number(),
            "Balance": 0
        }

        self.data.append(new_user)
        self.save_data()
        return new_user

    def authenticate(self, acc_no, pin):
        for user in self.data:
            if user["Account_No."] == acc_no and user["Pin"] == pin:
                return user
        return None

    def deposit(self, user, amount):
        if 0 < amount <= 10000:
            user["Balance"] += amount
            self.save_data()
            return True
        return False

    def withdraw(self, user, amount):
        if 0 < amount <= user["Balance"]:
            user["Balance"] -= amount
            self.save_data()
            return True
        return False

    def delete_account(self, user):
        self.data.remove(user)
        self.save_data()
