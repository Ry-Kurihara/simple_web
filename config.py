import os, sys
import param_store as ps
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URI = ps.get_parameters('/heroku/postgres_url')
SQLALCHEMY_TRACK_MODIFICATIONS = True 

DEBUG = True
# TODO paramストアから取ってくる
SECRET_KEY = 'secret key'
SALT = 'shio'

# engine = create_engine(SQLALCHEMY_DATABASE_URI)
