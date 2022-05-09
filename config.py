from distutils.debug import DEBUG
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())



class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') # 'postgresql://localhost/postgres'
    DEBUG = os.getenv('DEBUG')
    
    breakpoint()