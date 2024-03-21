from pymongo import MongoClient
from bson.objectid import ObjectId

class WeatherRepository:
    def __init__(self):
        # Initialize the MongoDB client and connect to the local MongoDB instance
        self.client = MongoClient('mongodb://localhost:27017/')
        # Access the 'weather_database' database
        self.db = self.client['weather_database']
        # Access the 'weather' collection within the 'weather_database' database
        self.weather_collection = self.db['weather']

    def create_weather(self, weather_data):
        """
        Insert a new weather document into the 'weather' collection.

        Args:
        - weather_data (dict): A dictionary containing weather data to be inserted.

        Returns:
        - str: The ObjectId of the inserted document converted to a string.
        """
        # Insert the weather data into the 'weather' collection and get the inserted ObjectId
        weather_id = self.weather_collection.insert_one(weather_data).inserted_id
        # Convert the ObjectId to a string and return it
        return str(weather_id)

    def get_weather(self, weather_id):
        """
        Retrieve a weather document from the 'weather' collection based on its ObjectId.

        Args:
        - weather_id (str): The ObjectId of the weather document to retrieve.

        Returns:
        - dict: The weather document retrieved from the collection.
        """
        # Find and return the weather document using its ObjectId (converted from string)
        weather = self.weather_collection.find_one({'_id': ObjectId(weather_id)})
        return weather

    def update_weather(self, weather_id, update_data):
        """
        Update an existing weather document in the 'weather' collection.

        Args:
        - weather_id (str): The ObjectId of the weather document to update.
        - update_data (dict): A dictionary containing the updated weather data.

        Returns:
        - int: The count of modified documents (usually 1 if the update is successful).
        """
        # Update the weather document using its ObjectId and the provided update data
        result = self.weather_collection.update_one({'_id': ObjectId(weather_id)}, {'$set': update_data})
        # Return the count of modified documents
        return result.modified_count

    def delete_weather(self, weather_id):
        """
        Delete a weather document from the 'weather' collection.

        Args:
        - weather_id (str): The ObjectId of the weather document to delete.

        Returns:
        - int: The count of deleted documents (usually 1 if the deletion is successful).
        """
        # Delete the weather document using its ObjectId
        result = self.weather_collection.delete_one({'_id': ObjectId(weather_id)})
        # Return the count of deleted documents
        return result.deleted_count

    def get_all_weather(self):
        """
        Retrieve all weather documents from the 'weather' collection.

        Returns:
        - pymongo.cursor.Cursor: A cursor object containing all weather documents.
        """
        # Retrieve and return all weather documents from the 'weather' collection
        all_weather = self.weather_collection.find()
        return all_weather
