from flask import Flask, render_template , url_for, request
import pandas as pd 
app = Flask(__name__)
@app.route('/')                    # (/) --> home route 
def home():
    return render_template('basic.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':

        def calculate(num1, num2, operator):
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                if num2 != 0:
                    return num1 / num2
                else:
                    return "Error: Division by zero"
            else:
                return "Error: Invalid operator"










#         brand_name = request.form['brand_name']
#         owner_name=int(request.form['owner'])
#         age_bike=int(request.form['age'])
#         power_bike= int(request.form['power'])
#         kms_driven_bike= int(request.form['kms_driven'])
#         bike_numbers={'TVS': 0,
#                         'Royal Enfield': 1,
#                         'Triumph': 2,
#                         'Yamaha': 3,
#                         'Honda': 4,
#                         'Hero': 5,
#                         'Bajaj': 6,
#                         'Suzuki': 7,
#                         'Benelli': 8,
#                         'KTM': 9,
#                         'Mahindra': 10,
#                         'Kawasaki': 11,
#                         'Ducati': 12,
#                         'Hyosung': 13,
#                         'Harley': 14,
#                         'Jawa': 15,
#                         'BMW': 16,
#                         'Indian': 17,
#                         'Rajdoot': 18,
#                         'LML': 19,
#                         'Yezdi': 20,
#                         'MV': 21,
#                         'Ideal': 22}
        
#         brand_name_encode=bike_numbers[brand_name]
#         lst=[[owner_name,brand_name_encode,kms_driven_bike,age_bike,power_bike]]  #sequence order
#         pred = model.predict(lst)
#         pred = pred[0]
#         pred = round(pred, 2)
#         user_data = (str(owner_name),str(brand_name),kms_driven_bike,age_bike,power_bike,pred)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4444,debug=True)
