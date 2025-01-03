from fastapi import FastAPI
from live_weather import get_weather
from tyre_wear_model import tyre_wear_model
from race_simulator import race_strategy

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the F1 Race Strategy API!"}

@app.get("/weather")
def get_weather_data():
    """Returns real-time weather conditions."""
    return get_weather()

@app.get("/tyre_wear")
def get_tyre_wear(driver_style: str, track_temp: float, tyre_type: str, laps_completed: int):
    """Calculates tyre wear based on driving style and conditions."""
    wear = tyre_wear_model(driver_style, track_temp, tyre_type, laps_completed)
    return {"Tyre Wear": f"{wear:.2f}%"}

@app.get("/strategy")
def get_race_strategy(driver: str, driver_style: str, tyre_type: str, total_laps: int, pit_stop_lap: int = None):
    """Generates an optimal race strategy for a driver."""
    strategy = race_strategy(driver, driver_style, tyre_type, total_laps, pit_stop_lap)
    return strategy

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
