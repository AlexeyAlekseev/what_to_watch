from datetime import datetime
from random import randrange

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
app.json.ensure_ascii = False

class Opinion(db.Model):
    __tablename__ = 'opinion'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)
    source = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


@app.route('/')
def index_view():
    # quantity = Opinion.query.count()
    # if not quantity:
    #     return 'В базе данных мнений о фильмах нет.'
    # offset_value = randrange(quantity)
    # opinion = Opinion.query.offset(offset_value).first()
    # return opinion.text

    result_list = []
    stories = Opinion.query.all()
    for story in stories:
        id = story.id
        text = story.text
        result = {id: text}
        result_list.append(result)
    print(result_list)
    return jsonify(result_list)


if __name__ == '__main__':
    app.run()