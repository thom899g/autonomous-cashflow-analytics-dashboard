from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Replace with actual data retrieval logic
    data = {'cashflow': [1000, 2000, 1500]}
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)