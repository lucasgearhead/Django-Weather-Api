# Weather API

A Django REST Framework API for retrieving weather information from the OpenWeatherMap API and storing it in a MongoDB database. This API provides endpoints to fetch current weather data, as well as historical weather data stored in the database.

## Features

- Retrieve current weather information for a specific city.
- View historical weather data stored in the database.
- Retrieve details of a specific weather history record.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/seu-usuario/weather-api.git
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Set up the MongoDB database according to the settings in `settings.py`.

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

## Usage

### Current Weather Endpoint

- **URL:** `/weather/`
- **Method:** GET
- **Query Parameters:**
  - `city`: The name of the city to retrieve weather information.
  - `units`: Units for temperature measurement. (Example: imperial, metric, or standard)
  - `appid`: Your OpenWeatherMap API key.

#### Usage Example:

To retrieve current weather information for the city of Miami in imperial units:

```
/weather/?city=Miami&units=imperial&appid=YOUR_OPENWEATHERMAP_API_KEY
```

Make sure to replace "YOUR OPENWEATHERMAP API KEY" with your actual API key.

### Weather History Endpoints

- **List Endpoint:**

  - **URL:** `/history/`
  - **Method:** GET

- **Detail Endpoint:**
  - **URL:** `/history/<id>/`
  - **Method:** GET

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or bug fixes.
