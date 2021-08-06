from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_cors import CORS



# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    CORS(app)
    login_manager.init_app(app)
    bootstrap =Bootstrap(app)
    
    
    app.config.from_object('config')
    
    db.init_app(app)
    
    
    import models.Usuario

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        
        
        return models.Usuario.User.query.get(int(user_id))
      

    # blueprint for non-auth parts of app
    from routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for auth routes in our app
    from routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from routes.adm.dashboard_adm import admin_dash as dashboard_blue
    app.register_blueprint(dashboard_blue)

    from routes.vendedor.dashboard import dash as dash_blueprint
    app.register_blueprint(dash_blueprint)

    
    return app