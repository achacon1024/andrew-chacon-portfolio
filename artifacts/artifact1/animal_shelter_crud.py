from pymongo import MongoClient

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, user, password, host, port, db_name, collection_name):
        try:
            # Build connection string and create a MongoClient instance
            connection_string = f"mongodb://{user}:{password}@{host}:{port}/?authSource=admin"
            self.client = MongoClient(connection_string)
            self.database = self.client[db_name]
            self.collection = self.database[collection_name]
            print("Connected to MongoDB successfully.")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")

    def create(self, data):
        """
        Inserts a document into the collection.
        """
        if data is not None:
            try:
                result = self.collection.insert_one(data)
                if result.inserted_id:
                    return True
                else:
                    return False
            except Exception as e:
                print(f"An error occurred during insert: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):
        """
        Queries for documents matching the provided key/value pair.
        """
        try:
            cursor = self.collection.find(query)
            results = list(cursor)  # Convert cursor to a list
            return results
        except Exception as e:
            print(f"An error occurred during read: {e}")
            return []

