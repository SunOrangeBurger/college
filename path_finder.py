import numpy as np
import pygame
import cv2
import time
from sklearn.neighbors import KNeighborsClassifier

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Path Finder")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

class Maze:
    def __init__(self, image_path):
        self.image_path = image_path
        self.maze = self.load_maze()

    def load_maze(self):
        # Load the maze image
        image = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            # Create a default maze if no image is found
            maze = np.ones((20, 20), dtype=int)
            maze[1:-1, 1:-1] = 0
            maze[1, 1] = 0
            maze[-2, -2] = 0
        else:
            # Convert to binary image
            _, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
            # Convert to numpy array with 0s and 1s
            maze = (binary_image == 0).astype(int)
        return maze

class PathFinder:
    def __init__(self, maze):
        self.maze = maze
        self.height, self.width = maze.shape
        self.start = (0, 0)
        self.end = (self.height - 1, self.width - 1)
        self.model = KNeighborsClassifier(n_neighbors=1)

    def train_model(self):
        X, y = [], []
        for y_coord in range(self.height):
            for x_coord in range(self.width):
                if self.maze[y_coord, x_coord] == 0:
                    X.append([y_coord, x_coord])
                    y.append(self.get_label(y_coord, x_coord))
        self.model.fit(X, y)

    def get_label(self, y, x):
        if (y, x) == self.end:
            return 1
        return 0

    def find_path(self):
        self.train_model()
        path = [self.start]
        current = self.start

        while current != self.end:
            neighbors = self.get_neighbors(current)
            if not neighbors:
                raise ValueError("No path found")
            next_step = self.model.predict([neighbors[0]])
            current = neighbors[next_step[0]]
            path.append(current)

        return path

    def get_neighbors(self, pos):
        y, x = pos
        neighbors = []
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < self.height and 0 <= nx < self.width and self.maze[ny, nx] == 0:
                neighbors.append((ny, nx))
        return neighbors

def main():
    # Initialize Pygame
    pygame.init()

    # Set up display
    cell_size = 30
    maze_image_path = input("Please enter the path to the maze image: ")
    maze = Maze(maze_image_path)
    maze_width, maze_height = maze.maze.shape[1], maze.maze.shape[0]
    screen_width = maze_width * cell_size
    screen_height = maze_height * cell_size
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Maze Path Finder")

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    # Create maze and find path
    path_finder = PathFinder(maze.maze)
    try:
        path = path_finder.find_path()
    except ValueError as e:
        print(e)
        path = []

    # Main game loop
    running = True
    path_index = 0
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Draw maze
        for y in range(maze_height):
            for x in range(maze_width):
                color = BLACK if maze.maze[y, x] == 1 else WHITE
                pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

        # Draw start and end points
        pygame.draw.rect(screen, GREEN, (0, 0, cell_size, cell_size))
        pygame.draw.rect(screen, RED, ((maze_width-1) * cell_size, (maze_height-1) * cell_size, cell_size, cell_size))

        # Draw path
        if path:
            for i, (y, x) in enumerate(path[:path_index+1]):
                color = BLUE
                pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

        pygame.display.flip()

        # Move along the path
        if path and path_index < len(path) - 1:
            path_index += 1
        
        clock.tick(5)  # Slow down the frame rate to make the navigation visible

    pygame.quit()

if __name__ == "__main__":
    main()
