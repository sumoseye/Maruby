import gradio as gr
import folium
from src.pathfinder import predict_30_day_path

# Global storage for the generated path
current_path = []

def run_simulation(lat, lon):
    global current_path
    current_path = predict_30_day_path(lat, lon)
    return update_map(0)

def update_map(day):
    if not current_path:
        return "Initialize a path first!"
    
    coords = current_path[int(day)]
    m = folium.Map(location=coords, zoom_start=4, tiles="OpenStreetMap")
    
    # Draw full path forecast
    folium.PolyLine(current_path, color="cyan", weight=3, opacity=0.6).add_to(m)
    
    # Place Tuna icon at current day step
    folium.Marker(
    location=coords, 
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(m)
    
    return m._repr_html_()

with gr.Blocks(title="Tuna Migration predictor") as demo:
    gr.Markdown("# Tuna Migration XGBoost Predictor")
    
    with gr.Row():
        with gr.Column(scale=1):
            lat = gr.Number(label="Start Latitude", value=35.0)
            lon = gr.Number(label="Start Longitude", value=-140.0)
            btn = gr.Button("Generate 30-Day Forecast", variant="primary")
            slider = gr.Slider(0, 30, step=1, label="Time Step (Days)")
            
        with gr.Column(scale=3):
            map_view = gr.HTML(label="Migration Map")

    btn.click(run_simulation, [lat, lon], map_view)
    slider.change(update_map, slider, map_view)

if __name__ == "__main__":
    demo.launch()