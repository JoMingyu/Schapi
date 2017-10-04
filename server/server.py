from flask import Flask
from flask_restful_swagger_2 import Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app, api_version='0.1')


def route():
    from routes.api.meal.meal import Meal
    from routes.api.school_data.school_codes import SchoolCode

    api.add_resource(Meal, '/meal')
    api.add_resource(SchoolCode, '/school-code')

if __name__ == '__main__':
    from support.xlsx_parser import parse

    parse()
    route()
    app.run(debug=True)
