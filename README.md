#  Tuna Migration Predictor (AI Prototype)

A machine learning-powered tool that predicts 30-day tuna migration paths based on environmental suitability. This prototype uses an **XGBoost Classifier** to evaluate ocean conditions and a pathfinding algorithm to simulate movement.

##  Features
* **AI Engine:** XGBoost model trained on temperature, oxygen, chlorophyll, and noise levels.
* **Interactive Map:** Built with Folium, allowing users to select any starting coordinate in the ocean.
* **Time-Step Navigation:** A slider UI that lets you visualize the predicted location of the species day-by-day.
* **Environmental Logic:** Simulated data layers for $O_2$ thresholds and thermal preference.

##  Tech Stack
* **Language:** Python 3.13
* **AI/ML:** XGBoost, Scikit-Learn, NumPy
* **Frontend:** Gradio
* **Mapping:** Folium

##  Installation & Setup

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/sumoseye/Maruby.git](https://github.com/sumoseye/Maruby.git)
   cd Maruby
