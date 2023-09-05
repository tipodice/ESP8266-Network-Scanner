import ujson  # Import the MicroPython JSON module

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.database = self.initialize_database()

    def initialize_database(self):
        try:
            # Attempt to open and load data from the JSON file
            with open(self.db_file, "r") as file:
                return ujson.load(file)
        except Exception as e:
            # If the file doesn't exist or an error occurs, return an empty dictionary
            return {}

    def save_database(self):
        # Save the current database to the JSON file
        with open(self.db_file, "w") as file:
            ujson.dump(self.database, file)

    def add_record(self, key, value):
        # Add a new record to the database and save it
        self.database[key] = value
        self.save_database()

    def get_record_by_bssid(self, name):
        # Search for a record by BSSID (MAC address) and return the BSSID
        for key, value in self.database.items():
            if "bssid" in value and value["bssid"] == name:
                return value["bssid"]
        return None

    def remove_record(self, key):
        # Remove a record from the database by key and save the updated database
        if key in self.database:
            del self.database[key]
            self.save_database()

    def get_last_record_key(self):
        # Get the key of the last record in the database
        if not self.database:
            return None
        max_key = max(self.database.keys(), key=int)
        return max_key
