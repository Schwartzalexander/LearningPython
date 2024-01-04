from flask import Blueprint

order_blueprint = Blueprint('orders', __name__)


@order_blueprint.route('/create/<number>')
def create(number):
    return f"Creating order {number}"
