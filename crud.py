import copy
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import json

from tools.main.models.axe import Axe

with open('secret.json') as file:
    SECRET = json.load(file)

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class GardenerAxe(Axe, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, unique=False)
    name = db.Column(db.String(40), unique=False)
    weight = db.Column(db.Float, unique=False)
    handle_material = db.Column(db.String(20), unique=False)
    color = db.Column(db.String(20), unique=False)
    
    def __init__(self, price_in_dollars, name="axe", weight_in_kilos=2, handle_material="wood", color="brown"):
        super().__init__(price_in_dollars, name, weight_in_kilos, handle_material, color)


class GardenerAxeSchema(ma.Schema):
    class Meta:
        fields = ("price", "name", "weight", "handle_material", "color")


axe_schema = GardenerAxeSchema()
axes_schema = GardenerAxeSchema(many=True)


@app.route("/axes", methods=["POST"])
def add_axe():
    price = request.json['price']
    name = request.json['name']
    weight = request.json['weight']
    handle_material = request.json['handle_material']
    color = request.json['color']
    created_axe = GardenerAxe(price_in_dollars=price, name=name, weight_in_kilos=weight,
                              handle_material=handle_material, color=color)
    db.session.add(created_axe)
    db.session.commit()
    return axe_schema.jsonify(created_axe)


@app.route("/axes", methods=["GET"])
def get_axes():
    all_axes = GardenerAxe.query.all()
    result = axes_schema.dump(all_axes)
    return jsonify(result)


@app.route("/axes/<id>", methods=["GET"])
def get_axe(id):
    axe = GardenerAxe.query.get(id)
    return axe_schema.jsonify(axe)


@app.route("/axes/<id>", methods=["PUT"])
def update_axe(id):
    axe = GardenerAxe.query.get(id)
    if axe is None:
        abort(404)
    old_axe = copy.deepcopy(axe)
    axe.price = request.json['price']
    axe.name = request.json['name']
    axe.weight = request.json['weight']
    axe.handle_material = request.json['handle_material']
    axe.color = request.json['color']
    db.session.commit()
    return axe_schema.jsonify(old_axe)


@app.route("/axes/<id>", methods=["DELETE"])
def delete_axe(id):
    axe = GardenerAxe.query.get(id)
    if axe is None:
        abort(404)
    db.session.delete(axe)
    db.session.commit()
    return axe_schema.jsonify(axe)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
