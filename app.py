from flask import Flask, render_template, request, redirect, url_for, jsonify
import numpy as np
from werkzeug import secure_filename

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

def picked_up():
    messages = [
        "まさか、逆さま？",
        "内科では薬のリスクはでかいな",
        "なんてしつけいい子、いいケツしてんな",
        "任天堂うどん店に",
        "ロリコン外科医いい加減懲りろ"
    ]
    return np.random.choice(messages)

@app.route('/')
def index():
    title = "回文の世界へようこそ"
    message = picked_up()
    return render_template('index.html',
                           message=message, title=title)

@app.route('/api')
def api():
   kaibun = picked_up()
   result = {
       "message": kaibun
   }
   return jsonify(ResultSet=result) 

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save("/home/mofumofuchan/public/"+filename)
        return jsonify({"result":"file upload successfully",
                        "url":"http://v150-95-173-128.a0d3.g.tyo1.static.cnode.io/"+filename })

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")


