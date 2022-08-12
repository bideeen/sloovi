from flask import Flask, make_response, request, jsonify
from api_constant import *
from flask_mongoengine import MongoEngine
from flask_jwt_extended import *
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

# Mongo DB Database
database_name = "API"
DB_URI = f"mongodb+srv://admin:{password}@cluster0.hhav7pm.mongodb.net/{db_name}?retryWrites=true&w=majority"
app.config['MONGODB_HOST'] = DB_URI


db = MongoEngine()
db.init_app(app)

# Users Schema
class User(db.Document):
    first_name = db.StringField()
    last_name = db.StringField()
    email = db.StringField()
    password = db.StringField()
    
    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password
        }

# Template Schema
class Template(db.Document):
    template_ = db.IntField()
    template_name = db.StringField()
    subject = db.StringField()
    body = db.StringField()
    
    def to_json(self):
        return {
            'template_name': self.template_name,
            'subject': self.subject,
            'body': self.body
        }


@app.route('/register', methods=['POST'])
def register():
    content = request.get_json(force=True)
    
    check_mail = User.objects(email=content['email']).first()
    if check_mail:
        return make_response('Sorry, this email has been taken. Try Another Email.', 401)
    
    user = User(first_name=content['first_name'],
                 last_name=content["last_name"],
                 email=content["email"],
                 password=generate_password_hash(content['password']))
    user.save()
    return make_response(jsonify("User created successfully"), 201)

@app.route('/login', methods=['POST'])
def login():
    content = request.get_json(force=True)
    
    # Check database for credentials
    user_obj = User.objects(email=content['email']).first()
    if check_password_hash(user_obj['password'], content['password']):
        access_token = create_access_token(identity=content['email'])
        return make_response(jsonify(access_token), 200)
    
    return make_response(jsonify('Incorrect details'), 401)
    
    
@app.route('/template', methods=['POST', 'GET'])
@jwt_required()
def templates():
    if request.method == 'GET':
        temps = []
        for temp in Template.objects:
            temps.append(temp)
        return make_response(jsonify(temps), 200)
    elif request.method == 'POST':
        content = request.get_json(force=True)
        temp = Template(template_name=content['template_id'], subject=content['subject'], body=content['body'])
        temp.save()
        return make_response(jsonify("Data Uploaded Successfully"), 201)
        

@app.route('/template/<template_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def each_template(template_id):
    if request.method == "GET":
        template_obj = Template.objects(template_name=template_id).first()
        if template_obj:
            return make_response(jsonify(template_obj.to_json()), 200)
        else:
            return make_response('', 404)
    elif request.method == "PUT":
        content = request.get_json(force=True)
        template = Template.objects(template_name=template_id).first()
        template.update(subject=content['subject'], body=content['body'])
        return make_response(jsonify("Data Updated Successfully"), 201)
    elif request.method == "DELETE":
        template = Template.objects(template_name=template_id).first()
        template.delete()
        return make_response(jsonify("Succesfully Deleted this data"), 201)




# if __name__ == "__main__":
#     app.run(debug=True)