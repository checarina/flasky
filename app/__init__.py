from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


<<<<<<< HEAD
def create_app(testing = None):
=======
def create_app(testing=None):
>>>>>>> 877f0d5fee487946624ccbbff008f800d505282f
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
<<<<<<< HEAD

=======
>>>>>>> 877f0d5fee487946624ccbbff008f800d505282f
    if testing is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")

<<<<<<< HEAD
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.bike import Bike
    from app.models.cyclist import Cyclist

=======
    from app.models.bike import Bike

    db.init_app(app)
    migrate.init_app(app, db)

>>>>>>> 877f0d5fee487946624ccbbff008f800d505282f
    from .routes.bike import bike_bp
    app.register_blueprint(bike_bp)
    from .routes.cyclist import cyclist_bp
    app.register_blueprint(cyclist_bp)

    return app