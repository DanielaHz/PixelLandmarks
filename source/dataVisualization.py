import matplotlib.pyplot as plt 
import numpy as np
import json

def read_landmarks(file_path):
    try:
        with open(file_path, 'r') as file:
            print("Reading file:", file_path)
            landmarks_data = json.load(file)
            return landmarks_data
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' does not contain valid JSON.")
        return None


def create_draf(landmarks_data):
    x_coordinates =  [point[0] for sublist in landmarks_data for point in sublist]
    y_coordinates =  [point[1] for sublist in landmarks_data for point in sublist]
    z_coordinates =  [point[2] for sublist in landmarks_data for point in sublist]

    figure =  plt.figure()
    ax = figure.add_subplot(111, projection='3d')

    scatter = ax.scatter(x_coordinates, y_coordinates, z_coordinates, cmap ='viridis')
    ax.set_xlabel('axis x')
    ax.set_ylabel('axis y')
    ax.set_zlabel('axis z')
    ax.set_title('landmark data graph')

    plt.show()