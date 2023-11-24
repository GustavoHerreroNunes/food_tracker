from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', method=['GET', 'POST'])
def index():
    if(request.method == 'GET'):
        return render_template('index.html')
    else:
        print("Autenticando usuario...")
        return render_template('index.html')
