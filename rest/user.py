from flask import Blueprint, request

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/create', methods=['POST'])
def create():
    data = request.json  # Get JSON data from the request body
    name = data.get('name', 'Unknown')  # Default to 'Unknown' if 'name' is not provided
    return f"Creating user {name}"


@user_blueprint.route('/delete', methods=['POST'])
def delete():
    data = request.json
    name = data.get('name', 'Unknown')
    return f"Deleting user {name}"
