import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS
from flask_migrate import Migrate

from database import db
from initializers.register_all_blueprints import RegisterBlueprints
from initializers.setup_config import SetupConfig

app = Flask(__name__)

with app.app_context():
    SetupConfig(app)
    db.init_app(app)
    migration = Migrate(app, db, directory="migrations", compare_type=True)

    cors = CORS(app)
    RegisterBlueprints(app, db)

    port = int(os.environ.get("PORT", 8002))

    app.run(host="0.0.0.0", port=port)
