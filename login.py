from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def home():
  return render_template('home.html')

@app.route('/csv')
def csv():
    import pandas as pd
    df = pd.read_csv('/workspace/Flask-Login/data/login.csv')
    info=df
    
    return '''mettere true e false con return'''


@app.route('/login/it')
def login():
  return render_template('homeLogin.html', Title='Login', h1='Login', login='Login')




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)