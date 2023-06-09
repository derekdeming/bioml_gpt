from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/db_name' # Replace with your DB details
db = SQLAlchemy(app)
api = Api(app)

class ProteinModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    sequence = db.Column(db.String(5000))

    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'sequence': self.sequence
        }


class Protein(Resource):
    def get(self, id):
        protein = ProteinModel.query.filter_by(id=id).first()
        if protein:
            return {"protein": protein.serialize()}, 200
        else:
            return {"message": "Protein not found"}, 404

api.add_resource(Protein, '/protein/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)


























# from flask import Flask, request, jsonify

# app = Flask(__name__)

# #get-root 
# @app.route("/get-user/<user_id>")
# def get_user(user_id):
#     user_data = {
#         "user_id": user_id,
#         "name": "Derek Deming",
#         "email": "derekdeming17@gmail.com"
#     }
    
#     extra = request.args.get("extra")
#     if extra: 
#         user_data["extra"] = extra
        
#     return jsonify(user_data), 200 


# @app.route("/create-user", methods=["POST"])
# def create_user():
#     data =  request.get_json()
    
#     return jsonify(data), 201

# if __name__ == "__main__":
#     app.run(debug=True)