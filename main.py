import math,graph

def input_data() -> None:
    data:list = []
    File = open("locations.csv",mode = "r") 
    for each in File:
        each = each.rstrip("\n")
        each = each.split(",")
        entry:list = []
        for i in each:
                if each.index(i) == 0:
                     entry.append(6-float(i))
                else:
                     entry.append(float(i))
                
        data.append(tuple(entry))
        entry = []
    File.close()

    
    
    path,cost = dijkstra_travel(data)
    print(path)
    graph.showData(path)
    
    

def calculate_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def find_top_leftmost_point(points):
    """Find the top-leftmost point (smallest y, then smallest x if tied)."""
    
    return min(points, key=lambda point: (point[1], point[0]))

def dijkstra_travel(points):
    # Find the top-leftmost point as the starting point
    start_point = find_top_leftmost_point(points)
    
    # Initialize list of visited points
    visited_points = [start_point]
    unvisited_points = points[:]
    unvisited_points.remove(start_point)
    
    total_distance = 0
    current_point = start_point
    
    # Keep visiting the nearest unvisited point
    while unvisited_points:
        # Find the closest unvisited point
        nearest_point = min(unvisited_points, key=lambda point: calculate_distance(current_point, point))
        distance = calculate_distance(current_point, nearest_point)
        total_distance += distance
        
        # Move to the nearest point
        visited_points.append(nearest_point)
        unvisited_points.remove(nearest_point)
        current_point = nearest_point
    
    return visited_points, total_distance




    
                

    
    


        


         














if __name__ == "__main__":
    input_data()
    
