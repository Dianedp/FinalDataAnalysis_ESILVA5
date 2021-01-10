# Import libraries
import io
import pickle
import pandas as pd
from flask import Flask, request

app = Flask(__name__)


@app.route('/xgb', methods=['POST'])
def xgb():
    xgb_model = pickle.load(open("final_prediction_XGB.pickle", "rb"))
    req = io.StringIO(request.data.decode('utf-8'))
    df = pd.read_csv(req, sep=',', header=0)
    prediction = xgb_model.predict(df)
    response = pd.DataFrame(prediction, index=df.index, columns=["The predicted decade of production with XGB"])
    json_response = response.to_json(orient='table', indent=2)
    return json_response, 201


@app.route('/clf', methods=['POST'])
def clf():
    xgb_model = pickle.load(open("final_prediction_clf.pickle", "rb"))
    req = io.StringIO(request.data.decode('utf-8'))
    df = pd.read_csv(req, sep=',', header=0)
    prediction = xgb_model.predict(df)
    response = pd.DataFrame(prediction, index=df.index, columns=["The predicted decade of production with CLF"])
    json_response = response.to_json(orient='table', indent=2)
    return json_response, 201


@app.route("/")
def greeting():
    return "Hello" \
           " let's predict the year of the production of your desired song!", 201


if __name__ == '__main__':
    app.run(debug=True)
