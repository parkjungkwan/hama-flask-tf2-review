# from flask import Flask
# from config import config

# def create_app(config_name):
#    app = Flask(__name__)
#    app.config.from_object(config[config_name])
#    config[config_name].init_app(app)

#    from .foo import foo_bp
#    from .boo import boo_bp

#    app.register_blueprint(foo_bp)
#    app.register_blueprint(boo_bp)

#    return app