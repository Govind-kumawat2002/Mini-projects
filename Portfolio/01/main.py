from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

# Email configuration
SENDER_EMAIL = "kumawatritk54@gmail.com"
PASSWORD = "xyz"

def send_email(name, email_address, mobile_number, subject, message):
    try:
        # Connecting with Gmail server
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        # Starting the security protocol
        server.starttls()
        server.login(SENDER_EMAIL, PASSWORD)
        
        # Email content
        email_subject = f"New message from {name}"
        email_body = f"Name: {name}\nEmail: {email_address}\nMobile Number: {mobile_number}\nSubject: {subject}\nMessage: {message}"
        message = f"Subject: {email_subject}\n\n{email_body}"
        
        # Sending email
        server.sendmail(SENDER_EMAIL, SENDER_EMAIL, message)
        server.quit()
        print(f"Successfully sent email to {SENDER_EMAIL} 😉🤞😉")
    except Exception as e:
        print(f"Mail was not sent please try again ! Error: {str(e)}")

@app.route('/')  # (/) --> home route
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def getvalue():
    if request.method == 'POST':
        name = request.form['full_name']
        email_address = request.form['email_address']
        mobile_number = request.form['mobile_number']
        subject = request.form['email_subject']
        message = request.form['message']
        send_email(name, email_address, mobile_number, subject, message)
    return "Form submitted successfully!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4444, debug=True)
