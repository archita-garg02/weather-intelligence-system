# Weather Intelligence System

A FastAPI-powered Weather Intelligence System that integrates with external weather APIs to provide real-time weather insights, forecasts, and weather analytics.

## Features

- Current weather information
- Temperature monitoring
- Humidity tracking
- Weather condition analysis
- Wind speed information
- RESTful API endpoints
- Interactive API documentation
- Streamlit dashboard for visualization

## Tech Stack

### Backend
- Python
- FastAPI
- Requests
- Uvicorn

### Frontend
- Streamlit

### External APIs
- OpenWeather API

---

## Project Structure

```text
weather-intelligence-system/
│
├── backend/
│   ├── main.py
│   ├── weather_service.py
│   ├── config.py
│   ├── requirements.txt
│   └── app.py
│
├── .gitignore
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/archita-garg02/weather-intelligence-system.git

cd weather-intelligence-system/backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Linux / Ubuntu

```bash
source venv/bin/activate
```

Windows

```powershell
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
WEATHER_API_KEY=your_openweather_api_key
```

Get your API key from:

https://openweathermap.org/api

---

## Run FastAPI Server

```bash
uvicorn main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Available Endpoints

### Health Check

```http
GET /
```

### Current Weather

```http
GET /weather/{city}
```

Example:

```http
GET /weather/Delhi
```

### Temperature

```http
GET /temperature/{city}
```

### Humidity

```http
GET /humidity/{city}
```

### Weather Condition

```http
GET /condition/{city}
```

### Wind Speed

```http
GET /wind/{city}
```

---

## Streamlit Dashboard

Run:

```bash
streamlit run app.py
```

Dashboard:

```text
http://localhost:8501
```

---

## Future Enhancements

- 5-Day Forecast
- Air Quality Monitoring
- Weather Alerts
- Weather Comparison Between Cities
- Historical Weather Analysis
- Weather Recommendation Engine
- AI-powered Weather Insights

---

## Author

Archita Garg

GitHub:
https://github.com/archita-garg02
