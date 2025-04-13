from flask import Flask, jsonify
import numpy as np
import pandas as pd
import pychartjs as cjs

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the JSON API"})

@app.route('/table', methods=['GET'])
def create_table():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df = pd.DataFrame(arr, columns=['A', 'B', 'C'])
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)