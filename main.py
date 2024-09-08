import numpy as np
import matplotlib.pyplot as plt
import cv2

# Define grid size
width, height = 100, 100
grid = np.zeros((height, width), dtype=np.uint8)

# Add obstacles
grid[30:40, 30:40] = 1  # Example obstacle

# Define car start position
car_position = [10, 10]

# Define car movement (simple)
def move_car(position, direction):
    if direction == 'up':
        position[1] -= 1
    elif direction == 'down':
        position[1] += 1
    elif direction == 'left':
        position[0] -= 1
    elif direction == 'right':
        position[0] += 1
    return position

def visualize(grid, car_position):
    grid[car_position[1], car_position[0]] = 2  # Mark car position
    plt.imshow(grid, cmap='gray')
    plt.show()

visualize(grid, car_position)

def follow_path(position, path):
    for step in path:
        position = move_car(position, step)
        visualize(grid, position)
        cv2.waitKey(500)  # Pause to visualize movement

path = ['right', 'right', 'down', 'down', 'left', 'left']
follow_path(car_position, path)

def is_obstacle(position, grid):
    return grid[position[1], position[0]] == 1

def move_car_safely(position, direction, grid):
    new_position = move_car(position, direction)
    if is_obstacle(new_position, grid):
        print("Obstacle detected, changing direction")
        return position  # Return original position if obstacle is detected
    return new_position
