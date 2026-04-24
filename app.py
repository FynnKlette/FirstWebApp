import os
from flask import Flask
import db

app = Flask(__name__)

app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
)
app.cli.add_command(db.init_db)
app.teardown_appcontext(db.close_db_con)


@app.route('/')
def index():
    return 'Hello, World!'
@app.route('/lists/')
def lists():
    return 'Todo: implement business logic to show all to-do lists'

@app.route('/lists/<int:id>')
def list(id):
    return 'Todo: implement business logic to show all to-dos of a particular list'
@app.route('/insert/sample')
def run_insert_sample():
    db.insert_sample()
    return 'Database flushed and populated with some sample data.'
