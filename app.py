from flask import Flask, render_template, jsonify, request
import plotly
import plotly.express as px
import pandas as pd
import numpy as np
import json
import random

app = Flask(__name__)

@app.route('/')
def index():
    dates = pd.date_range(start='2024-01-01', end='2024-04-30', freq='D')
    values = np.cumsum(np.random.normal(0, 1, len(dates))) + 100  # Random walk starting at 100
    
    line_df = pd.DataFrame({
        'Date': dates,
        'Value': values
    })
    line_fig = px.line(line_df, x='Date', y='Value', title='Daily Random Values (January-April 2024)')
    line_fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Value',
        template='plotly_white'
    )
    
    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
    bar_values = [random.randint(10, 100) for _ in range(len(categories))]
    
    bar_df = pd.DataFrame({
        'Category': categories,
        'Value': bar_values
    })
    bar_fig = px.bar(bar_df, x='Category', y='Value', title='Random Values by Category')
    bar_fig.update_layout(
        xaxis_title='Category',
        yaxis_title='Value',
        template='plotly_white'
    )
    
    line_chart_json = json.dumps(line_fig, cls=plotly.utils.PlotlyJSONEncoder)
    bar_chart_json = json.dumps(bar_fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('index.html', 
                           line_chart_json=line_chart_json,
                           bar_chart_json=bar_chart_json)

@app.route('/recieve', methods=['POST'])
def receive():
    if request.is_json:
            try:
                data = request.get_json()
                processed_data = {'received': data, 'status': 'success'}
                return jsonify(processed_data), 201
            except Exception as e:
                return jsonify({'error': 'Invalid JSON'}), 400
    else:
         return jsonify({'error': 'Method Not Allowed'}), 405




if __name__ == '__main__':
    app.run(port=1234, debug=True)