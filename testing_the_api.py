import requests
import pandas as pd


def scale_func(music):
    music.iloc[:, 1:] = (music.iloc[:, 1:] - music.iloc[:, 1:].min()) / (
            music.iloc[:, 1:].max() - music.iloc[:, 1:].min())
    return music


def random_sample(filename="YearPredictionMSD.csv", num_samples=10):
    base_for_samples = pd.read_csv(filename, header=None)

    print("Shape of the original dataset : ", base_for_samples.shape, end='\n\n\n')

    base_for_samples = base_for_samples[base_for_samples[0] > 1950]
    print("Shape of the dataset after getting cleaned : ", base_for_samples.shape, end='\n\n\n')

    samples = base_for_samples.sample(num_samples, axis=0)
    print("what our sample looks like : ", samples, end='\n\n\n')
    return scale_func(samples)


data = random_sample(num_samples=5)
data = data.drop(axis=1, columns=0)

print(data, end="\n\n\n")
req = data.to_csv(index=0)

resp = requests.post("http://127.0.0.1:5000/predictor", req).json()
print(resp, end="\n\n\n")

resp = requests.post("http://127.0.0.1:5000/clf", req).json()
print(resp, end="\n\n\n")

resp = requests.post("http://127.0.0.1:5000/xgb", req).json()
print(resp)
