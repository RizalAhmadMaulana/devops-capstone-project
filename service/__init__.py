from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Konfigurasi Keamanan Talisman (Tugas 22)
talisman = Talisman(app, force_https=False)

# Konfigurasi CORS
CORS(app)

from service import routes, models