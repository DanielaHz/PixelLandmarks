import matplotlib.pyplot as plt 
import json
import numpy as np

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

def simple_analysis(landmarks_data):
    x_coordinates =  [point[0] for sublist in landmarks_data for point in sublist]
    y_coordinates =  [point[1] for sublist in landmarks_data for point in sublist]
    z_coordinates =  [point[2] for sublist in landmarks_data for point in sublist]

    array_data_x =  np.array(x_coordinates)
    array_data_y =  np.array(y_coordinates)
    array_data_z =  np.array(z_coordinates)

    print(" min and max values using numpy")
    min_X = np.min(array_data_x)
    print("minimum value to X:" , min_X)
    max_X= np.max(array_data_x)
    print("maximum value to X", max_X )
    min_Y = np.min(array_data_y)
    print("minimum value to Y:" , min_Y)
    max_Y= np.max(array_data_y)
    print("maximum value to Y", max_Y )
    min_Z = np.min(array_data_z)
    print("minimum value to Z:" , min_Z)
    max_Z= np.max(array_data_z)
    print("maximum value to Z", max_Z )
    

    