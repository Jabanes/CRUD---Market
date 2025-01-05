from flask import Flask, jsonify, render_template, request
import json

        
app = Flask(__name__)

def find_food_by_id(id, fileToFind):
    for food in fileToFind:
        if food['id'] == id:
            return food
        
@app.route("/")
def displayMarket():
    with open('foods.json', 'r') as file:
        foods = json.load(file)

    foods = foods

    with open('cart.json', 'r') as file:
        cart = json.load(file)

    cart = cart

    return render_template("index.html", foods = foods, cart = cart )

@app.route("/add", methods=["POST"])
def addToCart():
    idToAdd = request.json.get("id")
    idToAdd = int(idToAdd)
    
    with open('foods.json', 'r') as file:
        foods = json.load(file)
    
    
    foodToAdd = find_food_by_id(idToAdd, foods)

    with open('cart.json', 'r') as file:
        cart = json.load(file)
    
    cart.append(foodToAdd)

    with open('cart.json', 'w') as f:
        json.dump(cart, f, indent=4)
    
    
    return jsonify({"cart": cart})


@app.route("/delete/<int:id>", methods=["DELETE"])
def removeFromCart(id):
    
    with open('cart.json', 'r') as file:
        cart = json.load(file)

    cart = [food for food in cart if food['id'] != id]

    with open('cart.json', 'w') as f:
        json.dump(cart, f, indent=4)

    return jsonify({"cart": cart})
    
if __name__ == "__main__":
    app.route(debug=True)