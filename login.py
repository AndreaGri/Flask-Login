from flask import Flask, render_template
app = Flask(__name__)




@app.route('/csv')
def csv():
    import pandas as pd
    df = pd.read_csv('/workspace/Flask-Login/data/login.csv')











if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)