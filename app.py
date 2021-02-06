from flask import Flask
import os
from backend import main_backend

album_names = main_backend()

def main_frontend():
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        return album_names[0]
        
    app.run(
        port = int(os.getenv('PORT', 8080))
        )
        
main_frontend()