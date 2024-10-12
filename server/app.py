#!/usr/bin/env python3

from flask import Flask, jsonify, session
from flask_migrate import Migrate
from models import db, Article, User
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/clear')
def clear_session():
    session.clear()  # Clear all session data
    return {'message': 'Session cleared successfully.'}, 200

@app.route('/articles')
def index_articles():
    # Optionally implement this to list articles
    return jsonify({'message': 'List of articles can be implemented here.'})

@app.route('/articles/<int:id>')
def show_article(id):
    # Initialize session['page_views'] if it doesn't exist
    session['page_views'] = session.get('page_views', 0)
    
    # Increment the page view count
    session['page_views'] += 1
    
    # Check if the user has exceeded the maximum page views
    if session['page_views'] > 3:
        return jsonify({'message': 'Maximum pageview limit reached'}), 401
    
    # Here you would normally fetch the article from the database
    # For demonstration purposes, returning a mock article
    article = {'id': id, 'title': f'Article {id}', 'author': 'Author Name','content': f'Content of Article {id}','preview': f'Preview of Article {id}','minutes_to_read': 5 ,'date': datetime.now().strftime('%Y-%m-%d')}
    
    return jsonify(article)

if __name__ == '__main__':
    app.run(port=5555)
