import numpy as np

def get_simulated_env(lat, lon):
    # Simulated geography-based rules
    temp = 25 - (abs(lat) * 0.5) + np.random.normal(0, 0.5)
    o2 = 6.0 - (temp * 0.1)
    chl = abs(np.sin(lon)) * 0.5
    noise = 90 if 38 < abs(lat) < 42 else 45 # Shipping lane simulation
    
    return {"temp": temp, "o2": o2, "chl": chl, "noise": noise}