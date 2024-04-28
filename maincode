from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def __init__(self, username, password):
        pass

    @abstractmethod
    def get_username(self):
        pass

    @abstractmethod
    def get_password(self):
        pass
from user import User

class ConcreteUser(User):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password
from abc import ABC, abstractmethod

class BirthdayReminder(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_account(self, username, password):
        pass

    @abstractmethod
    def login(self, username, password):
        pass

    @abstractmethod
    def add_birthday(self, username):
        pass

    @abstractmethod
    def view_user_birthdays(self, username):
        pass

    @abstractmethod
    def check_birthday_today(self, username):
        pass

    @abstractmethod
    def user_interface(self):
        pass

from birthday_reminder import BirthdayReminder
from concrete_user import ConcreteUser
import datetime

class ConcreteBirthdayReminder(BirthdayReminder):
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        try:
            with open("user_accounts.txt", "r") as file:
                for line in file:
                    username, password = line.strip().split(',')
                    self.users[username] = ConcreteUser(username, password)
        except FileNotFoundError:
            pass

    def save_users(self):
        with open("user_accounts.txt", "w") as file:
            for username, user in self.users.items():
                file.write(f"{username},{user.get_password()}\n")

    def create_account(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose another one.")
            return False
        else:
            self.users[username] = ConcreteUser(username, password)
            self.save_users()
            print("Account created successfully.")
            return True

    def login(self, username, password):
        if username in self.users:
            user = self.users[username]
            if user.get_password() == password:
                print("Login successful.")
                while True:
                    print("1. Add new birthday")
                    print("2. View if anybody celebrates birthday today")
                    choice = input("Enter your choice (1 or 2): ")
                    if choice == "1":
                        self.add_birthday(username)
                    elif choice == "2":
                        self.check_birthday_today(username)
                    else:
                        print("Invalid choice. Please enter 1 or 2")
                    if input("Do you want to continue (yes/no): ").lower() != "yes":
                        break
                return True
            else:
                print("Incorrect password. Please try again.")
                return False
        else:
            print("User not found. Please check your username.")
            return False

    def add_birthday(self, username):
        name = input("Enter the name of the person: ")
        year = int(input("Enter the birth year (YYYY): "))
        month = int(input("Enter the birth month (MM): "))
        day = int(input("Enter the birth day (DD): "))
        with open("birthdays.txt", "a") as file:
            file.write(f"{username},{name},{year},{month},{day}\n")
        print("Birthday added successfully.")

    def check_birthday_today(self, username):
        today = datetime.datetime.now()
        with open("birthdays.txt", "r") as file:
            for line in file:
                user, name, year, month, day = line.strip().split(',')
                if user == username:
                    birth_date = datetime.datetime(int(year), int(month), int(day))
                    if today.strftime("%m %d") == birth_date.strftime("%m %d"):
                        print(f"{name}'s birthday is today!")
                    else:
                        print(f"No {name} birthday today :(")

    def user_interface(self):
        print("Welcome to the Birthday Reminder!")
        print("If you want to sign up, type: 1")
        print("If you want to log in, type: 2")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            self.create_account(username, password)
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
        else:
            print("Invalid choice. Please try again.")
            return
        if self.login(username, password):
          pass

from concrete_birthday_reminder import ConcreteBirthdayReminder

class BirthdayReminderFactory:
    @staticmethod
    def create_birthday_reminder():
        return ConcreteBirthdayReminder()
