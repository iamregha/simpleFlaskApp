from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

#create a configuration for using sqlite db
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///simpleApp.db'


#create an Sqlalchemy instance
db = SQLAlchemy(app)

@app.route('/')
def check():
    return 'Flask is working'


if __name__ == '__main__':
    app.run()