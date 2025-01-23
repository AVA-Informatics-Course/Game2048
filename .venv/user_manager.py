import json

class UserManager:
    """
    Handles user-related functionalities such as saving and fetching user data.
    """

    def __init__(self, file_name='user_info.json'):
        self.file_name = file_name

    def fetch_user_data(self, first_name, last_name):
        """
        Fetches user data from a JSON file, adds the current user if not present,
        and updates the file with the latest data.
        """
        try:
            with open(self.file_name, 'r') as file:
                user_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            user_data = {}

        user_key = f"{first_name} {last_name}"

        if user_key not in user_data:
            user_data[user_key] = {
                "first name": first_name,
                "last name": last_name,
                "scores": 0
            }

        self._save_user_data(user_data)
        return user_data[user_key]

    def save_user_score(self, first_name, last_name, score):
        """
        Saves the current user's score to a JSON file, adding their data if not already present.
        """
        try:
            with open(self.file_name, 'r') as file:
                user_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            user_data = {}

        user_key = f"{first_name} {last_name}"

        if user_key not in user_data:
            user_data[user_key] = {
                "first name": first_name,
                "last name": last_name,
                "scores": 0
            }

        user_data[user_key]["scores"] = score
        self._save_user_data(user_data)

    def _save_user_data(self, user_data):
        """
        Saves the user data dictionary back to the JSON file.
        """
        with open(self.file_name, 'w') as file:
            json.dump(user_data, file, indent=4)
