# Import Flask.
from flask import Flask 

# This will create a Flask App Instance.
app = Flask(__name__)

#Define Route and View Function.
@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

# This will run Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)
