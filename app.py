from flask import Flask, jsonify, render_template, request, redirect, url_for
from service import note
from bson import ObjectId
from datetime import datetime
from routs import notes_bp
app = Flask(__name__)

app.register_blueprint(notes_bp)



if __name__ == "__main__":
    app.run(debug=True)
