import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'yoursecret'
    MONGODB_URI = os.environ.get('MONGODB_URI') or "mongodb+srv://2022eeb1147:abhi1234@cluster0.n1uu7cg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    DEBUG = True