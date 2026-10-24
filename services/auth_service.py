
import json
import os
import hashlib
import hmac
from pathlib import Path


class AuthService:
    """Manages hospital user accounts and login authentication."""

    ROLES = {"admin", "doctor", "receptionist"}

    def __init__(self, filename="data/users.json"):
        self.filename = Path(filename)
        self.filename.parent.mkdir(parents=True, exist_ok=True)
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("User data must be a JSON list.")

            return data

        except FileNotFoundError:
            return []

        except (json.JSONDecodeError, ValueError) as error:
            raise RuntimeError(
                f"Cannot safely load user accounts: {error}"
            ) from error

    def save_users(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.users, file, indent=4)

    @staticmethod
    def hash_password(password, salt=None):
        if salt is None:
            salt = os.urandom(16).hex()

        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            bytes.fromhex(salt),
            310000
        ).hex()

        return salt, password_hash

    def create_user(self, username, password, role):
        username = username.strip().lower()
        role = role.strip().lower()

        if not username or not password:
            print("Username and password cannot be empty.")
            return False

        if role not in self.ROLES:
            print("Invalid role.")
            return False

        if any(user["username"] == username for user in self.users):
            print("Username already exists.")
            return False

        if len(password) < 8:
            print("Password must contain at least 8 characters.")
            return False

        salt, password_hash = self.hash_password(password)

        self.users.append({
            "username": username,
            "salt": salt,
            "password_hash": password_hash,
            "role": role
        })

        self.save_users()
        print(f"User '{username}' created with role '{role}'.")
        return True

    def authenticate(self, username, password):
        username = username.strip().lower()

        for user in self.users:
            if user["username"] != username:
                continue

            salt, stored_hash = user["salt"], user["password_hash"]
            _, entered_hash = self.hash_password(password, salt)

            if hmac.compare_digest(entered_hash, stored_hash):
                return {
                    "username": user["username"],
                    "role": user["role"]
                }

            return None

        return None
