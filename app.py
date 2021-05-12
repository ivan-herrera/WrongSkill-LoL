from flask import Flask, render_template, request
from routes import WrongSkill

app = Flask(__name__)
app.register_blueprint(WrongSkill) 

# Settings
app.secret_key = 'secretkey'

if __name__ == '__main__':
    app.run(port = 2000, debug = True)