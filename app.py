import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Hello from Flask & Docker.</h2>'+'<h3>Application running on port '+request.host+'</h3>'+\
              f"<h3>This is Instance: {os.environ.get('INSTANCE_ID')}</h3>"


if __name__ == "__main__":
    app.run(debug=True)