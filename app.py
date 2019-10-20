from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def main():
    if request.method == 'POST':
        resp_json = request.get_json()
        f =  resp_json['text']
        print(f)
    return render_template('index.html')