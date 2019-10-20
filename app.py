from flask import Flask, render_template, request
import webbrowser, json

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def main():
    return render_template('index.html')

    
@app.route('/url',methods=['POST','GET'])
def url():
    if request.method == 'POST':
        resp_json = request.get_json()
        f =  resp_json['text'] #link
        print(f)

        return json.dumps({"response": "please wait"}), 200

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run(debug=False)

        