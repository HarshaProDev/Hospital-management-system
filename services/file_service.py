import json


class FileService:
    """
    Handles reading and writing JSON files.
    """

    @staticmethod
    def save_data(filename, data):
        """
        Save Python data into a JSON file.

        Args:
            filename (str): JSON file path.
            data (list): Data to save.

        Returns:
            bool: True if successful, otherwise False.
        """

        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)

            return True

        except OSError as error:
            print(f"File writing error: {error}")
            return False

    @staticmethod
    def load_data(filename):
        """
        Load data from a JSON file.

        Returns:
            list: Loaded data.
        """

        try:
            with open(filename, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty data.")
            return []

        except json.JSONDecodeError:
            print(f"{filename} contains invalid JSON.")
            return []

        except OSError as error:
            print(f"File reading error: {error}")
            return []