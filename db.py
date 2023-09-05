import ujson

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.database = self.initialize_database()

    def initialize_database(self):
        try:
            with open(self.db_file, "r") as file:
                return ujson.load(file)
        except Exception as e:
            return {}

    def save_database(self):
        with open(self.db_file, "w") as file:
            ujson.dump(self.database, file)

    def add_record(self, key, value):
        self.database[key] = value
        self.save_database()

    def get_record_by_bssid(self, name):
        for key, value in self.database.items():
            if "bssid" in value and value["bssid"] == name:
                return value["bssid"]
        return None

    def remove_record(self, key):
        if key in self.database:
            del self.database[key]
            self.save_database()

    def get_last_record_key(self):
        if not self.database:
            return None

        max_key = max(self.database.keys(), key=int)
        return max_key
    
