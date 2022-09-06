from flask import Flask
from dapperauth.database import init_db, shutdown_db_session

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    shutdown_db_session()


init_db()

import dapperauth.views