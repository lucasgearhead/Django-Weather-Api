# Weather API

This is a weather API built with Django that consumes the OpenWeatherMap API. It retrieves weather information, stores request history in a MongoDB database, and allows deletion of specific history records. It features authentication with PyJWT and is integrated with a React frontend available in the [React-Weather-Front](https://github.com/lucasgearhead/React-Weather-Front/) repository.

## Features

- **Get Weather Information**: Makes a request to the OpenWeatherMap API and returns weather data.
- **Store History**: Saves request information in MongoDB.
- **Delete History**: Allows logged-in users to delete history records.
- **Authentication**: Users can register, log in, and log out.
- **View History**: Any user can view the history, but making requests requires providing an API key.

## Endpoints

- **Get Weather Information**: `GET /weather/`
- **View Request History**: `GET /weather/history/`
- **View Specific Request Details**: `GET /weather/history/<str:weather_id>/`
- **Register User**: `POST /user/register/`
- **User Login**: `POST /user/login/`
- **User Information**: `GET /user/`
- **Update User**: `PUT /user/update/`
- **Delete User**: `DELETE /user/delete`

## How to Run the Project

1. Clone the repository:

   ```sh
   git clone https://github.com/lucasgearhead/Django-Weather-Api.git
   cd Django-Weather-Api
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Start the server:
   ```sh
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000`.

## Connecting with the Frontend

The React frontend that connects to this API is available in the [React-Weather-Front](https://github.com/lucasgearhead/React-Weather-Front/) repository.

## Dependencies

- asgiref==3.7.2
- bcrypt==4.1.3
- certifi==2024.2.2
- charset-normalizer==3.3.2
- Django==4.1.13
- django-cors-headers==4.3.1
- dnspython==2.6.1
- idna==3.6
- PyJWT==2.8.0
- pymongo==3.12.3
- pytz==2024.1
- requests==2.31.0
- sqlparse==0.2.4
- tzdata==2024.1
- urllib3==2.2.1

## Database

This API uses MongoDB, which can be managed with Mongo Compass.

## Authentication

Authentication is handled with PyJWT. To access protected endpoints, include the JWT token in the request header.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
