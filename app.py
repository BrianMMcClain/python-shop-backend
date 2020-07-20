from flask import Flask, jsonify

from item import Item

app = Flask(__name__)

items = [
    Item(1, "Apple", 0.50, 33),
    Item(2, "Banana", 0.75, 41),
    Item(3, "Orange", 0.70, 41),
    Item(4, "Potato", 0.25, 83),
    Item(5, "Onion", 0.60, 12),
]

@app.route('/')
def index():
    return jsonify([i.serialize() for i in items]) # Convert list of items to a JSON array