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
    results=db.session.query(Players).all()
    for r in results:
        print(r.last_name)

    return render_template('index.html')

@app.route('/base')
def base():
    #results=db.session.query(Players).all()
    #for r in results:
    #    print(r.last_name)

    return render_template('base.html')

if __name__ == '__main__':
    app.run()

