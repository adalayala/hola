from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    """Expone el mensaje 'EP2 UNIDA'."""
    
    return 'EP2 UNIDA'

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5005)





    