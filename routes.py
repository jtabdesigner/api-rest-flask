from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app import db, cache
from models import User, Item
from marshmallow import Schema, fields, ValidationError
from werkzeug.security import check_password_hash

api_blueprint = Blueprint('api', __name__)

# Rota inicial para verificar se a API está funcionando
@api_blueprint.route("/", methods=["GET"])
def index():
    return jsonify(message="API está funcionando!")

# Esquema para validação de dados de entrada
class ItemSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str()

# Esquema para validação de dados de login
class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)

# Endpoint para login (Autenticação)
@api_blueprint.route('/login', methods=["POST"])
def login():
    auth = request.get_json()
    
    # Validação de dados de entrada
    try:
        validated_data = LoginSchema().load(auth)
    except ValidationError as err:
        return jsonify(err), 400
    
    # Verificar se o usuário existe e validar a senha
    user = User.query.filter_by(email=validated_data.get("email")).first()
    if user and check_password_hash(user.password, validated_data.get("password")):
        token = create_access_token(identity=user.id)
        return jsonify(token=token)
    
    return jsonify(message="Invalid credentials"), 401

# Endpoint para listar itens com paginação
@api_blueprint.route("/items", methods=["GET"])
@cache.cached(timeout=60)
def get_items():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    items = Item.query.paginate(page, per_page, False)

    return jsonify({
        "items": [item.name for item in items.items],
        "total": items.total,
        "pages": items.pages,
        "current_page": items.page
    })

# Endpoint para criar um novo item (POST)
@api_blueprint.route("/items", methods=["POST"])
@jwt_required()
def create_item():
    data = request.get_json()
    try:
        validated_data = ItemSchema().load(data)
    except ValidationError as err:
        return jsonify(err), 400

    new_item = Item(name=validated_data["name"], description=validated_data.get("description"))
    db.session.add(new_item)
    db.session.commit()

    return jsonify({
        "message": "Item created",
        "data": validated_data
    }), 201

# Endpoint para atualizar um item (PUT)
@api_blueprint.route("/items/<int:item_id>", methods=["PUT"])
@jwt_required()
def update_item(item_id):
    data = request.get_json()
    item = Item.query.get_or_404(item_id)

    item.name = data.get('name', item.name)
    item.description = data.get('description', item.description)

    db.session.commit()

    return jsonify({
        "message": "Item updated",
        "item": {
            "id": item.id,
            "name": item.name,
            "description": item.description
        }
    })

# Endpoint para deletar um item (DELETE)
@api_blueprint.route("/items/<int:item_id>", methods=["DELETE"])
@jwt_required()
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()

    return jsonify({
        "message": "Item deleted",
        "id": item.id
    })

# Endpoint de exemplo (Hello World)
@api_blueprint.route("/hello", methods=["GET"])
def hello_world():
    return jsonify(message="Hello, World!")