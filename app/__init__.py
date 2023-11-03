from flask import Flask

app = Flask(__name__)

# Register the main blueprint
from app.views.main import main_blueprint
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run()
