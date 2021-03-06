# Import libraries
import io
import pickle
import pandas as pd
from flask import Flask, request
from joblib import load

app = Flask(__name__)


@app.route('/predictor', methods=['POST'])
def predictor():
    """model = pickle.load(open("final_prediction_clf.pickle", "rb"))"""
    model = load('filename.joblib')
    req = io.StringIO(request.data.decode('utf-8'))
    df = pd.read_csv(req, sep=',', header=0)
    prediction = model.predict(df)
    response = pd.DataFrame(prediction, index=df.index, columns=["The predicted decade of production with CLF"])
    json_response = response.to_json(orient='table', indent=2)
    return json_response, 201


@app.route("/")
def greeting():
    return "Hello" \
           " let's predict the year of the production of your desired song!"


if __name__ == '__main__':
    app.run(debug=True)
