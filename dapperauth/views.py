from dapperauth import app


@app.route('/hello')
def hello():
    return 'Hello world!'
