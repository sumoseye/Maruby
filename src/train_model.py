import xgboost as xgb
import pandas as pd
import numpy as np
import os

def train():
    # Simulate historical data: Temp, O2, Chl, Noise
    np.random.seed(42)
    data = {
        'temp': np.random.uniform(10, 30, 2000),
        'o2': np.random.uniform(2, 6, 2000),
        'chl': np.random.uniform(0, 1, 2000),
        'noise': np.random.uniform(30, 100, 2000)
    }
    df = pd.DataFrame(data)

    # Label data: 1 if conditions are "Tuna-friendly", 0 if not
    df['presence'] = ((df['temp'] > 17) & (df['temp'] < 23) & 
                      (df['o2'] > 3.8) & (df['noise'] < 75)).astype(int)

    model = xgb.XGBClassifier(n_estimators=100, max_depth=5, learning_rate=0.1)
    model.fit(df[['temp', 'o2', 'chl', 'noise']], df['presence'])

    os.makedirs('models', exist_ok=True)
    model.save_model('models/tuna_model.json')
    print("✅ Model trained and saved to models/tuna_model.json")

if __name__ == "__main__":
    train()