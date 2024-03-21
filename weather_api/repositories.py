from pymongo import MongoClient
from bson.objectid import ObjectId

class WeatherRepository:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['weather_database']
        self.weather_collection = self.db['weather']

    def create_weather(self, weather_data):
        weather_id = self.weather_collection.insert_one(weather_data).inserted_id
        return str(weather_id)

    def get_weather(self, weather_id):
        weather = self.weather_collection.find_one({'_id': ObjectId(weather_id)})
        return weather

    def update_weather(self, weather_id, update_data):
        result = self.weather_collection.update_one({'_id': ObjectId(weather_id)}, {'$set': update_data})
        return result.modified_count

    def delete_weather(self, weather_id):
        result = self.weather_collection.delete_one({'_id': ObjectId(weather_id)})
        return result.deleted_count

    def get_all_weather(self):
        all_weather = self.weather_collection.find()
        return all_weather