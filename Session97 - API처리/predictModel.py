from flask import Flask, request, json, jsonify
#입력 받기 경량화 웹!!!
import sys
import pandas as pd
import pickle
import time

with open('./modelCalsList.pkl', 'rb') as f:
    loadedModel = pickle.load(f)
    
app = Flask(__name__)

@app.route("/predictSlaveGCnt", methods=['POST'])
def predictMlCnt():
    
    params = request.get_json()
    print("받은 Json 데이터 ", params)
    
    param1 = params["g_cnt"]

    inData = pd.DataFrame([[param1]])

    predictValue = int( loadedModel[0].predict(inData ) )

    predictValue

    response = {
        "result": predictValue
    }

    return jsonify(response)

@app.route("/predictSlaveGGap", methods=['POST'])
def predictMlGap():

    params = request.get_json()
    print("받은 Json 데이터 ", params)
    
    param1 = params["g_gap"]

    inData = pd.DataFrame([[param1]])

    predictValue = int( loadedModel[1].predict(inData ) )

    predictValue

    response = {
        "result": predictValue
    }

    return jsonify(response)

@app.route("/predictSlaveGAll", methods=['POST'])
def predictMlAll():

    params = request.get_json()
    print("받은 Json 데이터 ", params)
    
    param1 = params["g_cnt"]
    param2 = params["g_gap"]

    inData = pd.DataFrame([[param1,param2]])

    predictValue = int( loadedModel[2].predict(inData ) )

    predictValue

    response = {
        "result": predictValue
    }
    time.sleep(5)
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=2000)