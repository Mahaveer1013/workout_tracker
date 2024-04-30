from flask import Flask, session
from flask_cors import CORS
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager,unset_jwt_cookies, get_jwt, set_access_cookies
from datetime import datetime , timedelta

app=Flask(__name__)
CORS(app)

app.config['secret_key']='idhu_epdi_irukku-->indha_secret_key😂😎'
app.config["JWT_SECRET_KEY"] = "qwertyu1234567890poiuytrewqgdc"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
jwt = JWTManager(app)

if __name__=='__main__':
    app.run(debug=True)