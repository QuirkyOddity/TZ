import sys
def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        center_line = file.readline().strip()
        radius_line = file.readline().strip()
        center = tuple(map(float, center_line.split()))
        radius = float(radius_line)
    return center, radius
def read_points(file_path):
    with open(file_path, 'r') as file:
        points = [tuple(map(float, line.strip().split())) for line in file]
    return points
def point_position(center, radius, point):
    x0, y0 = center
    x, y = point
    distance_squared = (x - x0)**2 + (y - y0)**2
    radius_squared = radius**2
    if abs(distance_squared - radius_squared) < 1e-9:
        return 0
    elif distance_squared < radius_squared:
        return 1
    else:
        return 2
def main():
    if len(sys.argv) != 3:
        sys.exit(1) 
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    try:
        center, radius = read_circle_data(circle_file)
        points = read_points(points_file)
        for point in points:
            position = point_position(center, radius, point)
            print(position)
    except FileNotFoundError:
        sys.exit(1)
    except ValueError:
        sys.exit(1)
if __name__ == "__main__":
    main()
