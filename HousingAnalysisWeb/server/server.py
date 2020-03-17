from flask import Flask,request, jsonify,redirect, url_for,request,render_template
import util
app = Flask(__name__)
app.templates_auto_reload = True

@app.route('/')
def investmentForm():
     return render_template('formpage.html')


@app.route('/get_location_name')
def get_location_name():
    response = jsonify(
        {
         'locations' : util.get_location_names()   
        }
    )
    response.headers.add('Access-Controll-Allow-Origib','*')
    return response


@app.route('/predict', methods = ['POST'])
def predictHomePrice():
    sqft = float(request.form['sqft'])
    location = request.form['location']
    balcony = (request.form['balcony'])
    bath = (request.form['bath'])
    bhk = (request.form['bhk'])
    # response = jsonify(
    #     {
    #      'response' : util.get_estimated_price(bath,balcony,bhk,sqft, location) 
    #     }
    # )
    # response.headers.add('Access-Controll-Allow-Origib','*')
    # return response
    predictVal = util.get_estimated_price(bath,balcony,bhk,sqft, location) 
    return render_template('predict.html', profit = predictVal)   

if __name__ == "__main__":
    print("server is runnign")
    app.run()