import cmath
import math

# Star configuration
num_points = 5
radius = 20  # Radius of the circle containing the star
angle_step = 360 / num_points  # Evenly spaced points

# Grid dimensions (higher resolution for better detail)
grid_width = 80
grid_height = 40

# Initialize the ASCII grid
grid = [[' ' for _ in range(grid_width)] for _ in range(grid_height)]

# Generate star points using complex numbers
points = []
for k in range(num_points):
    angle = math.radians(k * angle_step - 90)  # Start from top (rotate -90°)
    z = complex(radius * math.cos(angle), radius * math.sin(angle))
    points.append(z)

# Convert complex coordinate to grid indices (with aspect ratio correction)
def complex_to_grid(z):
    x = int(round(z.real * 1.3 + grid_width // 2))  # Scale X-axis
    y = int(round(-z.imag * 0.7 + grid_height // 2))  # Scale Y-axis (taller chars)
    return x, y

# Bresenham's Line Algorithm (improved for smooth lines)
def draw_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        if 0 <= x0 < grid_width and 0 <= y0 < grid_height:
            grid[y0][x0] = '*'  # Draw star point
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

# Connect points in pentagram order: 0 → 2 → 4 → 1 → 3 → 0
connection_order = [0, 2, 4, 1, 3, 0]
for i in range(len(connection_order) - 1):
    z0 = points[connection_order[i]]
    z1 = points[connection_order[i + 1]]
    x0, y0 = complex_to_grid(z0)
    x1, y1 = complex_to_grid(z1)
    draw_line(x0, y0, x1, y1)

# Print the final ASCII grid
for row in grid:
    print(''.join(row))




# import cmath
# import math

# # Star parameters
# num_points = 5
# radius = 20  # Increased radius for better spacing
# angle_step = 360 / num_points

# # Grid dimensions (increased for higher resolution)
# grid_width = 80
# grid_height = 40

# # Initialize the grid
# grid = [[' ' for _ in range(grid_width)] for _ in range(grid_height)]

# # Generate star points in complex plane
# points = []
# for k in range(num_points):
#     angle = math.radians(k * angle_step - 90)  # Start from top
#     z = complex(radius * math.cos(angle), radius * math.sin(angle))
#     points.append(z)

# # Function to convert complex coordinate to grid index with rounding
# def complex_to_grid(z):
#     x = int(round(z.real * 1.3 + grid_width // 2))  # X-axis scaling
#     y = int(round(-z.imag * 0.7 + grid_height // 2))  # Y-axis scaling (compensate character aspect ratio)
#     return x, y

# # Improved Bresenham's Line Algorithm with anti-aliasing
# def draw_line(x0, y0, x1, y1):
#     dx = abs(x1 - x0)
#     dy = abs(y1 - y0)
#     sx = 1 if x0 < x1 else -1
#     sy = 1 if y0 < y1 else -1
#     err = dx - dy

#     while True:
#         if 0 <= x0 < grid_width and 0 <= y0 < grid_height:
#             grid[y0][x0] = '*'  # Draw star point
#         if x0 == x1 and y0 == y1:
#             break
#         e2 = 2 * err
#         if e2 > -dy:
#             err -= dy
#             x0 += sx
#         if e2 < dx:
#             err += dx
#             y0 += sy

# # Connect the star points (pentagram order)
# connection_order = [0, 2, 4, 1, 3, 0]
# for i in range(len(connection_order) - 1):
#     z0 = points[connection_order[i]]
#     z1 = points[connection_order[i + 1]]
#     x0, y0 = complex_to_grid(z0)
#     x1, y1 = complex_to_grid(z1)
#     draw_line(x0, y0, x1, y1)

# # Print the final ASCII grid
# for row in grid:
#     print(''.join(row))




# import cmath
# import math

# # Star parameters
# num_points = 5
# radius = 15  # Increased radius for better spacing
# angle_step = 360 / num_points

# # Grid dimensions (increased for higher resolution)
# grid_width = 60
# grid_height = 30

# # Initialize the grid
# grid = [[' ' for _ in range(grid_width)] for _ in range(grid_height)]

# # Generate star points in complex plane
# points = []
# for k in range(num_points):
#     angle = math.radians(k * angle_step - 90)  # Rotate to start from top
#     z = complex(radius * math.cos(angle), radius * math.sin(angle))
#     points.append(z)

# # Function to convert complex coordinate to grid index with rounding
# def complex_to_grid(z):
#     x = int(round(z.real + grid_width // 2))  # Centered horizontally
#     y = int(round(-z.imag + grid_height // 2))  # Centered vertically, flip y-axis
#     return x, y

# # Bresenham's Line Algorithm (slightly optimized)
# def draw_line(x0, y0, x1, y1):
#     dx = abs(x1 - x0)
#     dy = -abs(y1 - y0)
#     sx = 1 if x0 < x1 else -1
#     sy = 1 if y0 < y1 else -1
#     err = dx + dy

#     while True:
#         if 0 <= x0 < grid_width and 0 <= y0 < grid_height:
#             grid[y0][x0] = '*'  # Draw star point
#         if x0 == x1 and y0 == y1:
#             break
#         e2 = 2 * err
#         if e2 >= dy:
#             err += dy
#             x0 += sx
#         if e2 <= dx:
#             err += dx
#             y0 += sy

# # Connect the star points (pentagram order)
# connection_order = [0, 2, 4, 1, 3, 0]
# for i in range(len(connection_order) - 1):
#     z0 = points[connection_order[i]]
#     z1 = points[connection_order[i + 1]]
#     x0, y0 = complex_to_grid(z0)
#     x1, y1 = complex_to_grid(z1)
#     draw_line(x0, y0, x1, y1)

# # Print the final ASCII grid
# for row in grid:
#     print(''.join(row))




# import cmath
# import math

# # Star parameters
# num_points = 5
# radius = 10
# angle_step = 360 / num_points

# # Grid dimensions
# grid_width = 40
# grid_height = 20

# # Initialize the grid
# grid = [[' ' for _ in range(grid_width)] for _ in range(grid_height)]

# # Generate star points in complex plane
# points = []
# for k in range(num_points):
#     angle = math.radians(k * angle_step)
#     # Generate point on circle using complex number
#     z = complex(radius * math.cos(angle), radius * math.sin(angle))
#     points.append(z)

# # Function to convert complex coordinate to grid index
# def complex_to_grid(z):
#     x = int(z.real + grid_width // 2)
#     y = int(-z.imag + grid_height // 2)  # Flip y-axis for screen
#     return x, y

# # Function to draw a line between two points using Bresenham's algorithm
# def draw_line(x0, y0, x1, y1):
#     dx = abs(x1 - x0)
#     dy = -abs(y1 - y0)
#     sx = 1 if x0 < x1 else -1
#     sy = 1 if y0 < y1 else -1
#     err = dx + dy

#     while True:
#         if 0 <= x0 < grid_width and 0 <= y0 < grid_height:
#             grid[y0][x0] = '*'
#         if x0 == x1 and y0 == y1:
#             break
#         e2 = 2 * err
#         if e2 >= dy:
#             err += dy
#             x0 += sx
#         if e2 <= dx:
#             err += dx
#             y0 += sy

# # Connect the star points
# connection_order = [0, 2, 4, 1, 3, 0]
# for i in range(len(connection_order) - 1):
#     z0 = points[connection_order[i]]
#     z1 = points[connection_order[i + 1]]
#     x0, y0 = complex_to_grid(z0)
#     x1, y1 = complex_to_grid(z1)
#     draw_line(x0, y0, x1, y1)

# # Print the final ASCII grid
# for row in grid:
#     print(''.join(row))