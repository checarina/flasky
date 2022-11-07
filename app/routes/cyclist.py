from flask import Blueprint, jsonify, request, abort, make_response
from app import db
from app.models.cyclist import Cyclist
from app.models.bike import Bike
from .routes_helper import get_one_obj_or_abort, validate_model

cyclist_bp = Blueprint("cyclist_bp", __name__, url_prefix="/cyclist")

@cyclist_bp.route("/<cyclist_id>/bikes", methods = ["GET"])
def get_all_bikes(cyclist_id):
    cyclist = validate_model(Cyclist, cyclist_id)
    bikes = cyclist.bikes
    bikes_response = []
    for bike in bikes:
        bikes_response.append(bike.to_dict())
    return jsonify(bikes_response)
