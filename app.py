from flask import Flask, render_template, request
import json

        
app = Flask(__name__)

@app.route("/")
def displayMarket():
    with open('foods.json', 'r') as file:
        foods = json.load(file)

    foods = foods
    return render_template("index.html", foods = foods )

@app.route("/add", methods=["POST"])
def addToCart():
    food_id = request.json.get("id")
    food_id = int(food_id)
    
    with open('foods.json', 'r') as file:
        foods = json.load(file)
    
    def find_food_by_id(id):
        for food in foods:
            if food['id'] == id:
                return food
    
    food_item = find_food_by_id(food_id)

    with open('cart.json', 'r') as file:
        cart = json.load(file)
    
    cart.append(food_item)

    with open('cart.json', 'w') as f:
        json.dump(cart, f, indent=4)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.route(debug=True)