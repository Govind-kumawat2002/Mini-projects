from flask import Flask , render_template, url_for, request
app = Flask(__name__)
@app.route('/')                    # (/) --> home route 
def home():
    return render_template('index.html')

# @app.route('/predict',methods=['GET','POST'])













if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4444,debug=True)