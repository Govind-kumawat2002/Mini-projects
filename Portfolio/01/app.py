from flask import Flask , render_template, url_for, request
import smtplib
try:
    # connecting with gmail server
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    # starting the security protocol
    server.starttls()
    sender_email = "kumawatritk54@gmail.com"
    password = "xyz"
    server.login(sender_email, password=password)   
    



    app = Flask(__name__)
    @app.route('/')                    # (/) --> home route 
    def home():
        return render_template('index.html')

    # @app.route('/predict',methods=['GET','POST'])
    @app.route('/predict',methods=['GET','POST'])
    def getvalue():
        if request.method=='POST':
            name = request.form['text']
            Email_add=(request.form['email'])
            number=int(request.form['number'])
            text= int(request.form['text'])
        lst=[[name,Email_add,number,text]] 
        server.sendmail(sender_email, lst)
        print(f"Successfully mail has been sent to {lst}😉🤞😉")
        server.quit()
except Exception as e:
    print('Mail was not sent 😒😒!')





if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4444,debug=True)