import xgboost as xgb
import numpy as np

# Load model globally for efficiency
model = xgb.XGBClassifier()
try:
    model.load_model('models/tuna_model.json')
except:
    print("⚠️ Model not found. Run train_model.py first!")

def get_suitability_score(temp, oxygen, chlorophyll, noise):
    features = np.array([[temp, oxygen, chlorophyll, noise]])
    # Predict probability of Tuna presence
    probs = model.predict_proba(features)
    return float(probs[0][1])
