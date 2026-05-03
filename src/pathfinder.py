from .engine import get_suitability_score
from .data_manager import get_simulated_env

def predict_30_day_path(start_lat, start_lon):
    path = [[start_lat, start_lon]]
    
    for _ in range(30):
        curr_lat, curr_lon = path[-1]
        best_score = -1
        best_coord = [curr_lat, curr_lon]
        
        # Look in 8 directions (N, S, E, W + diagonals)
        for d_lat in [-0.2, 0, 0.2]:
            for d_lon in [-0.2, 0, 0.2]:
                check_lat = curr_lat + d_lat
                check_lon = curr_lon + d_lon
                
                env = get_simulated_env(check_lat, check_lon)
                score = get_suitability_score(env['temp'], env['o2'], env['chl'], env['noise'])
                
                if score > best_score:
                    best_score = score
                    best_coord = [check_lat, check_lon]
        
        path.append(best_coord)
    return path