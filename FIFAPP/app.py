from flask import Flask, render_template, request
from datetime import datetime
import json
from flask_sqlalchemy import SQLAlchemy


app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Players.db'
db=SQLAlchemy(app)

Players=db.Table('players21',db.metadata,autoload=True, autoload_with=db.engine)
print('HELLO')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def explore():
    if request.method =='POST':
        form=request.form
        search_value=form['search_string']
        search='%{}%'.format(search_value)
        results=db.session.query(Players).filter_by(name=search_value)
        return render_template('search.html', results=results)

    else:
        return redirect('/')


    #results=db.session.query(Players).all()
    #results=db.session.query(Players).filter_by(name='Cristiano Ronaldo')
 

    #for r in results:
    #    print(r.last_name)
    #return render_template('explore.html', results=results)
    

@app.route('/compare')
def compare():
    return render_template('compare.html')

@app.route('/recommend')
def recommend():
    return render_template('recommend.html')

@app.route('/explore')
def trying():
    return render_template('explore.html')



if __name__ == '__main__':
    app.run()

