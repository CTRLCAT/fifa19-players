from flask import Flask, render_template, request
from datetime import datetime
import json
from flask_sqlalchemy import SQLAlchemy
import pandas as pd


app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Players.db'
db=SQLAlchemy(app)

Players=db.Table('players19',db.metadata,autoload=True, autoload_with=db.engine)
print('OK')

Recommendations=db.Table('recommendations',db.metadata,autoload=True, autoload_with=db.engine)
print('OK')

#results=db.session.query(Recommendations).all()
#results=pd.DataFrame(results)
#colnames = ["ID","Name","Age","Overall","Potential","Club","Value","Wage","Special","PreferredFoot","InternationalReputation","WeakFoot","SkillMoves","WorkRateUp","WorkRateDown","BodyType","RealFace","Position","JerseyNumber","Joined","LoanedFrom","ContractValidUntil","Height","Weight","LS","ST","RS","LW","LF","CF","RF","RW","LAM","CAM","RAM","LM","LCM","CM","RCM","RM","LWB","LDM","CDM","RDM","RWB","LB","LCB","CB","RCB","RB","Crossing","Finishing","HeadingAccuracy","ShortPassing","Volleys","Dribbling","Curve","FKAccuracy","LongPassing","BallControl","Acceleration","SprintSpeed","Agility","Reactions","Balance","ShotPower","Jumping","Stamina","Strength","LongShots","Aggression","Interceptions","Positioning","Vision","Penalties","Composure","Marking","StandingTackle","SlidingTackle","GKDiving","GKHandling","GKKicking","GKPositioning","GKReflexes","ReleaseClause"]
#results.columns=colnames
#print(results)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/explore', methods=['GET','POST'])
def explore():
    results=db.session.query(Players).all()
    names=[]
    for player in results:
        names.append(player[1])
    return render_template('explore.html', names=names)

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method =='POST':
        form=request.form
        search_value=form['search_string']
        #search='%{}%'.format(search_value)

        results=db.session.query(Players).filter_by(Name=search_value)
        #print(results)
        return render_template('search.html', results=results)

    else:
        return redirect('/')

    #results=db.session.query(Players).filter_by(name='Cristiano Ronaldo')
    #return render_template('explore.html', results=results)
    

@app.route('/recommend', methods=['GET','POST'])
def recommend():
    results=db.session.query(Players).all()
    names=[]
    for player in results:
        names.append(player[1])
    return render_template('recommend.html', names=names)


@app.route('/recommendations', methods=['GET','POST'])
def recommendations():
    if request.method =='POST':
        form=request.form
        recommend_string=form['recommend_string']
        search='%{}%'.format(recommend_string)
        results=db.session.query(Recommendations).filter_by(name=recommend_string)
        return render_template('recommendations.html', results=results)

    else:
        return redirect('/')


@app.route('/compare', methods=['GET','POST'])
def compare():
    results=db.session.query(Players).all()
    names=[]
    for player in results:
        names.append(player[1])
    return render_template('compare.html', names=names)

@app.route('/compareresults', methods=['GET','POST'])
def compareresults():
    if request.method =='POST':
        form=request.form
        search_value1=form['compare_string1']
        search_value2=form['compare_string2']
        #search='%{}%'.format(search_value)

        results1=db.session.query(Players).filter_by(Name=search_value1)
        results2=db.session.query(Players).filter_by(Name=search_value2)
        #print(results)
        return render_template('compareresults.html', results1=results1, results2=results2)

    else:
        return redirect('/')


if __name__ == '__main__':
    app.run()

