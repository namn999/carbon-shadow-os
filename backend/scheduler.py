from carbon_data import carbon_intensity

def calculate_emission(runtime, intensity):
    return runtime * intensity

def optimize_task(runtime, deadline):
    best = None
    lowest = float("inf")

    for region, values in carbon_intensity.items():
        for hour, intensity in enumerate(values):
            if hour <= deadline:
                emission = calculate_emission(runtime, intensity)
                if emission < lowest:
                    lowest = emission
                    best = {
                        "region": region,
                        "hour": hour,
                        "emission": emission
                    }
    return best
