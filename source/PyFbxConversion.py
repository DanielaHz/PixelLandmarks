import pickle
import json
import numpy as np

def convert_ndarray_to_list(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, dict):
        return {k: convert_ndarray_to_list(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_ndarray_to_list(i) for i in obj]
    else:
        return obj

def load_save_json_file():
    # upload pickle data
    with open('files/landmarks.pickle', 'rb') as f:
        landmarks = pickle.load(f)

    # convert ndarrays to list
    landmarks = convert_ndarray_to_list(landmarks)

    # save the data into a .json
    with open('files/landmarks.json', 'w') as f:
        json.dump(landmarks, f)

def convert_json_to_fbx():
    pass

if __name__ == "__main__":
    load_save_json_file()