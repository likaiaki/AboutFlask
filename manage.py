# import logging
import os
from flask_migrate import MigrateCommand
from flask_script import Manager
from App import create_app, models
from flask import render_template


env = os.environ.get("FLASK_ENV", "development")
app = create_app(env)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@app.route("/")
def index():
    return render_template("news/index.html")

if __name__ == '__main__':
    manager.run()