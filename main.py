import pandas as pd
import lxml
import flask
from flask import Flask, render_template

app = Flask(__name__)

data = pd.read_html('https://en.m.wikipedia.org/wiki/Lists_of_One_Piece_episodes')

table = data[0]
selist =[]
print (table['Season title'].loc[0])
  

selist = table['Season title'].values.tolist()


@app.route('/')
def seList():
  return render_template('index.html', data = selist)

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug=True)
  

