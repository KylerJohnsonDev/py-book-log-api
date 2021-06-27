#Import required packages
from flask import Flask, jsonify
from extensions import db
from blueprints.user_blueprint import user_blueprint
from blueprints.book_entries_blueprint import book_entries_blueprint

# https://tutorialwithproject.com/flask-rest-api-crud-operations/

# Init app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////home/kylerjohnson/databases/book_inventory/book_inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db.init_app(app)
    
#Create a Hello-World route
@app.route('/health', methods=['GET'])
def get_hello_world():
    return jsonify({'status': 'Healthy'})

app.register_blueprint(user_blueprint)
app.register_blueprint(book_entries_blueprint)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
