from flask import Flask, render_template
from datetime import datetime
import json
from flask_sqlalchemy import SQLAlchemy


app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Players.db'
db=SQLAlchemy(app)

Players=db.Table('players21',db.metadata,autoload=True, autoload_with=db.engine)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/explore')
def explore():
    results=db.session.query(Players).all()
    #for r in results:
    #    print(r.last_name)
    return render_template('explore.html', results=results)

@app.route('/compare')
def compare():
    return render_template('compare.html')

@app.route('/recommend')
def recommend():
    return render_template('recommend.html')

if __name__ == '__main__':
    app.run()

