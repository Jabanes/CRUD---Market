from flask import Flask, render_template
import json

file_path = 'foods.json'
def read_file():
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data

def write_file(data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        
app = Flask(__name__)

@app.route("/")
def displayMarket():
    foods = read_file()
    return render_template("index.html", foods = foods )

if __name__ == "__main__":
    app.route(debug=True)