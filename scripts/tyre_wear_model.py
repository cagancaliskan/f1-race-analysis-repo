def tyre_wear_model(driver_style: str, track_temp: float, tyre_type: str, laps_completed: int) -> float:
    """
    Calculates tyre degradation based on:
    - Driver's style (Aggressive, Balanced, Conservative)
    - Track temperature
    - Tyre type (Soft, Medium, Hard, Intermediate, Wet)
    - Number of laps completed
    """

    # Base wear rates for each tyre type
    wear_rate = {
        "Soft": 0.1,
        "Medium": 0.07,
        "Hard": 0.05,
        "Intermediate": 0.08,
        "Wet": 0.06
    }

    # Driver aggressiveness factor
    style_factor = {
        "Aggressive": 1.3,
        "Balanced": 1.0,
        "Conservative": 0.7
    }

    # Temperature impact: Higher temperature increases tyre degradation
    temp_factor = 1 + ((track_temp - 25) * 0.01)  # Baseline at 25°C

    # Calculate degradation
    degradation = laps_completed * wear_rate[tyre_type] * style_factor[driver_style] * temp_factor

    return min(100, degradation)  # Max degradation capped at 100%

if __name__ == "__main__":
    wear = tyre_wear_model("Aggressive", 30, "Soft", 20)
    print(f"Tyre Wear: {wear:.2f}%")  # Example usage
