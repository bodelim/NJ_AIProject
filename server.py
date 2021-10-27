from flask import Flask
from PyApi import mealData_Parsing

app = Flask(__name__)

@app.route('/lunch')
def mealLunch():
    return mealData_Parsing.mealSearch('Lunch')

@app.route('/Dinner')
def mealDinner():
    return mealData_Parsing.mealSearch('Dinner')
    

if __name__ == '__main__':
    app.run(debug=True)