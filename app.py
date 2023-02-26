import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS
from flask_migrate import Migrate

from database import db
from initializers.register_all_blueprints import RegisterBlueprints
from initializers.setup_config import SetupConfig

# from initializers.engine import engine
from sqlalchemy import create_engine

db_uri = "postgresql://avnadmin:AVNS_np5yB2HWuPCvhliJY3j@pg-841b05c-ethicate.aivencloud.com:19321/defaultdb?sslmode=require&sslrootcert=ca.pem"


app = Flask(__name__)

with app.app_context():
    SetupConfig(app)
    # engine = create_engine(db_uri)
    db.init_app(app)
    # db.engine = engine

    migration = Migrate(app, db, directory="migrations", compare_type=True)

    cors = CORS(app)
    RegisterBlueprints(app, db)

    port = int(os.environ.get("PORT", 8002))

    app.run(host="0.0.0.0", port=port)
