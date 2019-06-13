from app import app
from flask import render_template
import pandas as pd 



work_df = pd.read_csv('app/data/looking_for_work.csv')
talent_df = pd.read_csv('app/data/looking_for_talent.csv')
collab_df = pd.read_csv('app/data/looking_to_collab.csv')

month = 'June'
@app.route('/work')
def work():
    posts = []
    for i,j in zip(work_df['description'],work_df['contact']):
        posts.append({'description': i, 'contact': j})
    return render_template('board.html', title = 'Looking for Work',posts=posts, month=month)

@app.route('/collab')
def collab():
    posts = []
    for i,j in zip(collab_df['description'],collab_df['contact']):
        posts.append({'description': i, 'contact': j})
    return render_template('board.html', title = 'Looking to Collaborate',posts=posts, month=month)

@app.route('/talent')
def talent():
    posts = []
    for i,j in zip(talent_df['description'],talent_df['contact']):
        posts.append({'description': i, 'contact': j})
    return render_template('board.html', title = 'Looking for talent',posts=posts,month=month)
