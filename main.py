import pandas as pd
import lxml
import flask
from flask import Flask

app = Flask(__name__)

data = pd.read_html('https://en.m.wikipedia.org/wiki/Lists_of_One_Piece_episodes')

table = data[0]
selist =[]
print (table['Season title'].loc[0])
  
for i in range(19):
  selist.append(table['Season title'].loc[i])

@app.route('/')
def seList():
  return selist

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug=True)
  

