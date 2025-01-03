from live_weather import get_weather
from tyre_wear_model import tyre_wear_model

def race_strategy(driver: str, driver_style: str, tyre_type: str, total_laps: int, pit_stop_lap: int = None):
    """Generates an optimized race strategy for a driver."""
    
    # Get real-time weather data
    weather = get_weather()
    track_temp = weather["temperature"]
    
    # Default pit stop strategy (mid-race)
    if pit_stop_lap is None:
        pit_stop_lap = total_laps // 2  

    # Calculate tyre wear before and after pit stop
    wear_before_pit = tyre_wear_model(driver_style, track_temp, tyre_type, pit_stop_lap)
    wear_after_pit = tyre_wear_model(driver_style, track_temp, tyre_type, total_laps - pit_stop_lap)

    # Generate race strategy
    strategy = {
        "Driver": driver,
        "Tyre Type": tyre_type,
        "Weather": weather,
        "Pit Stop Lap": pit_stop_lap,
        "Wear Before Pit": f"{wear_before_pit:.2f}%",
        "Wear After Pit": f"{wear_after_pit:.2f}%",
        "Recommended Strategy": "One-stop strategy" if wear_after_pit < 80 else "Two-stop strategy"
    }

    return strategy

if __name__ == "__main__":
    result = race_strategy("Verstappen", "Aggressive", "Soft", 50)
    print(result)  # Example output
