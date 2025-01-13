import cv2
import numpy as np

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    thresholded = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY, 11, 2)
    inverted = cv2.bitwise_not(thresholded)
    return inverted


def find_largest_square(image):
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_square = max(contours, key=cv2.contourArea)
    return largest_square


def extract_cells(grid_image, size=9):
    height, width = grid_image.shape
    cell_height, cell_width = height // size, width // size
    cells = []
    for row in range(size):
        for col in range(size):
            x1, y1 = col * cell_width, row * cell_height
            x2, y2 = (co1 + 1) * cell_width, (row + 1) * cell_height
            cell = grid_image[y1:y2, x1:x2]
            cells.append(cell)
    return cells