import source.dataVisualization as dt

def main():
    print("Calling the data to visalize the landmarks!")
    file = 'landmarks.json'
    data =  dt.read_landmarks(file)
    dt.simple_analysis(data)
    dt.create_draf(data)
    
if __name__ == "__main__":
    main()
