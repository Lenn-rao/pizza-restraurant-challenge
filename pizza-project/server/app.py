from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models to ensure they are registered with SQLAlchemy
from server.models import restaurant, pizza, restaurant_pizza

# Import controllers to register routes
from server.controllers import restaurant_controller, pizza_controller, restaurant_pizza_controller

if __name__ == '__main__':
    app.run(debug=True)