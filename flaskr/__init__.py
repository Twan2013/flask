import os

from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='CHANGEME',
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/test')
    def test():
        name = request.cookies.get('user_username')
        print(name)
        return render_template('test.html')

    @app.route('/main')
    def main():
        name = request.cookies.get('user_username')
        print(name)
        return render_template('base.html')



    return app