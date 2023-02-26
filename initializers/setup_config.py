class SetupConfig:
    def __init__(self, app):
        app.config["DEBUG"] = True

        app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "postgresql://avnadmin:AVNS_np5yB2HWuPCvhliJY3j@pg-841b05c-ethicate.aivencloud.com:19321/defaultdb?sslmode=require&sslrootcert=ca.pem"

        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["MAIL_SERVER"] = "smtp.gmail.com"
        app.config["MAIL_PORT"] = 465
        app.config["MAIL_USERNAME"] = "kaashyap.gfg@gmail.com"
        app.config["MAIL_PASSWORD"] = "Kaashyap123"
        app.config["MAIL_USE_TLS"] = False
        app.config["MAIL_USE_SSL"] = True
        app.config["SECRET_KEY"] = "kaashyap"
